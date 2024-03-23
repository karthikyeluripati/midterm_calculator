# core.py

import pandas as pd
import os
import importlib.util


class CalculatorREPL:
    def __init__(self):
        self.history = []
        self.history_file = 'history.csv'
        if os.path.exists(self.history_file):
            self.history_df = pd.read_csv(self.history_file)
        else:
            self.history_df = pd.DataFrame(columns=['Expression', 'Result'])

    def start(self):
        print("Welcome to Calculator!")
        while True:
            user_input = input(">>> ")
            if user_input.lower() == 'exit':
                self.save_history()
                print("Exiting Calculator. Goodbye!")
                break
            elif user_input.lower() == 'plugins':
                self.list_plugins()
            elif user_input.lower() == 'load history':
                self.load_history()
            elif user_input.lower() == 'save history':
                self.save_history()
            elif user_input.lower() == 'clear history':
                self.clear_history()
            elif user_input.lower().startswith('delete'):
                index = int(user_input.split(' ')[1])
                self.delete_history_record(index)
            elif user_input.lower().startswith('load'):
                plugin_name = user_input.split(' ')[1]
                self.load_plugin(plugin_name)
            else:
                result = self.evaluate_expression(user_input)
                print(result)
                self.history.append((user_input, result))
                self.update_history_df(user_input, result)

    def evaluate_expression(self, expression):
        try:
            tokens = expression.split()
            operation = tokens[0]
            operands = list(map(float, tokens[1:]))
            return self.perform_operation(operation, *operands)
        except Exception as e:
            return f"Error: {e}"

    def perform_operation(self, operation, *operands):
        try:
            plugin_module = self.load_plugin(operation + "_plugin")
            return plugin_module.perform_operation(*operands)
        except AttributeError:
            return f"Error: Plugin '{operation}' not found"
    

    # Loading Plugins

    def load_plugin(self, plugin_name):
        spec = importlib.util.spec_from_file_location(plugin_name, f"calculator/plugins/{plugin_name}.py")
        plugin_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(plugin_module)
        return plugin_module

    # History

    def load_history(self):
        try:
            self.history_df = pd.read_csv(self.history_file)
            print("History loaded successfully.")
            print("Loaded history:")
            print(self.history_df)
        except FileNotFoundError:
            print("No history file found.")

    def save_history(self):
        self.history_df.to_csv(self.history_file, index=False)

    def list_plugins(self):
        plugin_dir = os.path.join(os.path.dirname(__file__), 'plugins')
        if os.path.exists(plugin_dir):
            print("Available plugins:")
            plugin_files = [f for f in os.listdir(plugin_dir) if f.endswith('.py') and f != '__init__.py']
            for plugin_file in plugin_files:
                plugin_name = plugin_file[:-3]  # Remove the '.py' extension
                print(f"- {plugin_name}")
        else:
            print("Error: Plugins directory not found.")

    def update_history_df(self, user_input, result):
        new_entry = pd.DataFrame({'Expression': [user_input], 'Result': [result]})
        self.history_df = pd.concat([self.history_df, new_entry], ignore_index=True)