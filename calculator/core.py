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
                result = self.evaluate(user_input)
                print(result)
                self.history.append((user_input, result))
                self.update_history_df(user_input, result)

    def evaluate(self, expression):
        try:
            result = eval(expression)
            return result
        except Exception as e:
            return f"Error: {e}"

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

    def load_plugin(self, plugin_name):
        spec = importlib.util.spec_from_file_location(plugin_name, f"calculator/plugins/{plugin_name}.py")
        plugin_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(plugin_module)
        setattr(self, plugin_name, plugin_module)
        return plugin_module

    def update_history_df(self, user_input, result):
        new_entry = pd.DataFrame({'Expression': [user_input], 'Result': [result]})
        self.history_df = pd.concat([self.history_df, new_entry], ignore_index=True)

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
        print("History saved successfully.")

    def clear_history(self):
        self.history_df = pd.DataFrame(columns=['Expression', 'Result'])
        print("History cleared.")

    def delete_history_record(self, index):
        try:
            self.history_df.drop(index=index, inplace=True)
            print("History record deleted successfully.")
        except KeyError:
            print("Invalid index. No record found.")
