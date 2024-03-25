import pkgutil
import importlib
from app.commands import CommandHandler
from app.commands import Command
import pandas as pd
import os
from dotenv import load_dotenv
import logging
import logging.config

class App:
    def __init__(self): # Constructor
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.command_handler = CommandHandler()
        self.history = []
        self.history_file = './app/history.csv'
        if os.path.exists(self.history_file) and os.path.getsize(self.history_file) > 0:
            self.history_df = pd.read_csv(self.history_file)
        else:
            self.history_df = pd.DataFrame(columns=['Expression', 'Result'])

    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings
    
    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        return self.settings.get(env_var, None)

    def load_plugins(self):
        # Dynamically load all plugins in the plugins directory
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
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
    # Register commands here
        self.load_plugins()
        print("Type 'exit' to exit.")
        logging.info("Application started. Type 'exit' to exit.")
        while True:  #REPL Read, Evaluate, Print, Loop
            user_input = input(">>> ")
            self.command_handler.execute_command(user_input.strip())
            self.history.append((user_input))
            self.update_history_df(user_input)
            self.save_history()  # Save history after each update

    def save_history(self):
        self.history_df.to_csv(self.history_file, index=False)

    def update_history_df(self, user_input):
        new_entry = pd.DataFrame({'Expression': [user_input]})
        self.history_df = pd.concat([self.history_df, new_entry], ignore_index=True)
        logging.info("Updated History")
