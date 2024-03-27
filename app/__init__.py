"""Importing necessary libraries"""
import os
import pkgutil
import importlib
import logging
import logging.config
from dotenv import load_dotenv
from app.commands import CommandHandler
from app.commands import Command

class App:
    """Initialize and Logging Configuration"""

    def __init__(self): # Constructor
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.command_handler = CommandHandler()

    def configure_logging(self):
        """Logging Configuration"""
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(levelname)s-%(message)s')
        logging.info("Logging configured.")


    def load_environment_variables(self):
        """Load Environment Variables"""
        settings = dict(os.environ.items())
        logging.info("Environment variables loaded.")
        return settings


    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        """Get Environment Variables"""
        return self.settings.get(env_var, None)


    def load_plugins(self):
        """Load the Plugins"""
        # Dynamically load all plugins in the plugins directory
        plugins_package = 'app.plugins'
        plugins_path = plugins_package.replace('.', '/')
        if not os.path.exists(plugins_path):
            logging.warning(f"Plugins directory '{plugins_path}' not found.")
            return
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
            if is_pkg:  # Ensure it's a package
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command)):  # Assuming a BaseCommand class exists
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue  # If item is not a class or unrelated class, just ignore


    def start(self):
        """Intialize the application"""
    # Register commands here
        self.load_plugins()
        logging.info("Application started. Type 'exit' to exit.")
        while True:  #REPL Read, Evaluate, Print, Loop
            user_input = input(">>> ")
            self.command_handler.execute_command(user_input.strip())
