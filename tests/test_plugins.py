"""Test cases for plugins"""
import unittest
from unittest.mock import patch, mock_open
import pandas as pd
from app.plugins.add import AddCommand
from app.plugins.clear import ClearCommand
from app.plugins.delete import DeleteHistoryCommand
from app.plugins.divide import DivideCommand
from app.plugins.exit import ExitCommand
from app.plugins.load import LoadHistoryCommand
from app.plugins.menu import MenuCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.subtract import SubtractCommand

class TestAddCommand(unittest.TestCase):
    """Test cases for Add command"""
    @patch('builtins.input', side_effect=['abc', '5'])
    @patch('logging.info')
    @patch('logging.error')
    @patch('pandas.DataFrame.to_csv')
    def test_execute_invalid_input(self, mock_to_csv, mock_error, mock_info, mock_input):
        """Test invalid input"""
        command = AddCommand()
        command.execute()
        mock_error.assert_called_once_with("Invalid input. Enter only numbers")
        mock_to_csv.assert_not_called()
        mock_info.assert_not_called()

    @patch('builtins.input', side_effect=[Exception('Mocked exception'), '5'])
    @patch('logging.info')
    @patch('logging.error')
    @patch('pandas.DataFrame.to_csv')
    def test_execute_exception(self, mock_to_csv, mock_error, mock_info, mock_input):
        """Test Exception"""
        command = AddCommand()
        command.execute()
        mock_error.assert_called_once_with("Invalid input. Enter only numbers")
        mock_to_csv.assert_not_called()
        mock_info.assert_not_called()

class TestClearCommand(unittest.TestCase):
    """Test Clear Command"""
    @patch('logging.info')
    @patch('pandas.DataFrame.to_csv')
    @patch('builtins.open', new_callable=mock_open)
    def test_execute(self, mock_open, mock_to_csv, mock_info):
        """Test Execute"""
        command = ClearCommand()
        command.execute()

        # Ensure file is opened in write mode and truncated
        mock_open.assert_called_once_with("./app/history.csv", "w")
        mock_open.return_value.truncate.assert_called_once()
        mock_open.return_value.close.assert_called_once()

        # Ensure history deletion and header update are logged
        mock_info.assert_any_call("History Deleted")
        mock_info.assert_any_call("History Header updated")

        # Ensure DataFrame is written to CSV file with updated header
        mock_to_csv.assert_called_once_with("./app/history.csv", index=False)

class TestDeleteHistoryCommand(unittest.TestCase):
    """Test Delete Command"""
    @patch('logging.error')
    @patch('pandas.read_csv', side_effect=pd.errors.ParserError())  # Simulate an error while reading CSV
    def test_execute_exception(self, mock_read_csv, mock_error):
        """Test exeception"""
        command = DeleteHistoryCommand()
        command.execute()

        # Ensure error is logged for invalid input (error during CSV reading)
        mock_error.assert_called_once_with("Invalid input")

class TestDivideCommand(unittest.TestCase):
    """Test divide command"""
    @patch('builtins.input', side_effect=['10', '2'])
    @patch('logging.info')
    @patch('pandas.DataFrame.to_csv')
    def test_execute_valid_input(self, mock_to_csv, mock_info, mock_input):
        """Test execute valid input"""
        command = DivideCommand()
        command.execute()
        #mock_info.assert_called_once_with("Performing division with 10.0 and 2.0")
        mock_to_csv.assert_called_once()

    @patch('builtins.input', side_effect=['10', '0'])
    @patch('logging.error')
    @patch('pandas.DataFrame.to_csv')
    def test_execute_division_by_zero(self, mock_to_csv, mock_error, mock_input):
        """Test Zero Division"""
        command = DivideCommand()
        command.execute()
        mock_error.assert_called_once_with("Error: Cannot divide by zero.")
        mock_to_csv.assert_not_called()

    @patch('builtins.input', side_effect=['abc', '2'])
    @patch('logging.error')
    @patch('pandas.DataFrame.to_csv')
    def test_execute_invalid_input(self, mock_to_csv, mock_error, mock_input):
        """Test invalid input"""
        command = DivideCommand()
        command.execute()
        mock_error.assert_called_once_with("Invalid input. Enter only numbers")
        mock_to_csv.assert_not_called()

class TestExitCommand(unittest.TestCase):
    """Test Exit command"""
    @patch('sys.exit')
    @patch('logging.info')
    def test_execute(self, mock_logging_info, mock_sys_exit):
        """Test execute"""
        command = ExitCommand()
        command.execute()
        mock_logging_info.assert_called_once_with("Application exit.")
        mock_sys_exit.assert_called_once_with("Exiting...")


class TestLoadHistoryCommand(unittest.TestCase):
    """Test Load command"""
    @patch('pandas.read_csv')
    @patch('logging.info')
    @patch('builtins.print')
    def test_execute_successful(self, mock_print, mock_logging_info, mock_read_csv):
        """Test execute"""
        # Create a mock DataFrame to simulate history data
        mock_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

        # Configure the read_csv mock to return the mock DataFrame
        mock_read_csv.return_value = mock_df

        command = LoadHistoryCommand()
        command.execute()

        # Assert that read_csv is called with the correct path
        mock_read_csv.assert_called_once_with("./app/history.csv")

        # Assert that the logging messages are generated
        # mock_logging_info.assert_called_with("Loading history...")
        mock_logging_info.assert_called_with("History Loaded")

        # Assert that the DataFrame is printed
        mock_print.assert_called_once_with(mock_df)

    @patch('pandas.read_csv', side_effect=pd.errors.ParserError('Mocked parser error'))
    @patch('logging.error')
    def test_execute_parsing_error(self, mock_logging_error, mock_read_csv):
        """Test execute with a parsing error"""
        command = LoadHistoryCommand()
        command.execute()

        # Assert that the error message is logged
        mock_logging_error.assert_called_once_with("Parsing data error")

class TestMenuCommand(unittest.TestCase):
    """Test Menu command"""
    @patch('builtins.print')
    @patch('os.listdir')
    @patch('logging.info')
    def test_execute(self, mock_logging_info, mock_os_listdir, mock_print):
        """Test Execute"""
        # Configure the mock to return a list of plugin files
        mock_os_listdir.return_value = ['plugin1.py', 'plugin2.py']

        command = MenuCommand()
        command.execute()

        # Assert that os.listdir is called with the correct path
        mock_os_listdir.assert_called_once_with("./app/plugins")

        # Assert that the logging messages are generated
        # mock_logging_info.assert_called_with("All plugins Collected")
        mock_logging_info.assert_called_with("Displayed All plugins")

        # Assert that the plugin files are printed
        mock_print.assert_has_calls([
            unittest.mock.call("Available Plugins:"),
            unittest.mock.call("- plugin1.py"),
            unittest.mock.call("- plugin2.py")
        ])

class TestMultiplyCommand(unittest.TestCase):
    """Test Multiply command"""
    @patch('builtins.input', side_effect=['10', '5'])
    @patch('logging.info')
    @patch('pandas.DataFrame.to_csv')
    def test_execute_valid_input(self, mock_to_csv, mock_info, mock_input):
        """Test Execute"""
        command = MultiplyCommand()
        command.execute()
        # mock_info.assert_called_once_with("Performing Multiplication with 10.0 and 5.0")
        mock_to_csv.assert_called_once()

    @patch('builtins.input', side_effect=['abc', '5'])
    @patch('logging.error')
    @patch('pandas.DataFrame.to_csv')
    def test_execute_invalid_input(self, mock_to_csv, mock_error, mock_input):
        """Test execute invalid input"""
        command = MultiplyCommand()
        command.execute()
        mock_error.assert_called_once_with("Invalid input. Enter only numbers")
        mock_to_csv.assert_not_called()

    @patch('builtins.input', side_effect=[Exception('Mocked exception'), '5'])
    @patch('logging.error')
    @patch('pandas.DataFrame.to_csv')
    def test_execute_exception(self, mock_to_csv, mock_error, mock_input):
        """Test execute exception"""
        command = MultiplyCommand()
        command.execute()
        mock_error.assert_called_once_with("Invalid input. Enter only numbers")
        mock_to_csv.assert_not_called()

class TestSubtractCommand(unittest.TestCase):
    """Text subtract command"""
    @patch('builtins.input', side_effect=['10', '5'])
    @patch('logging.info')
    @patch('pandas.DataFrame.to_csv')
    def test_execute_valid_input(self, mock_to_csv, mock_info, mock_input):
        """Test valid input"""
        command = SubtractCommand()
        command.execute()
        #mock_info.assert_called_once_with("Performing Subtraction with 10.0 and 5.0")
        mock_to_csv.assert_called_once()

    @patch('builtins.input', side_effect=['abc', '5'])
    @patch('logging.error')
    @patch('pandas.DataFrame.to_csv')
    def test_execute_invalid_input(self, mock_to_csv, mock_error, mock_input):
        """Test invalid input"""
        command = SubtractCommand()
        command.execute()
        mock_error.assert_called_once_with("Invalid input. Enter only numbers")
        mock_to_csv.assert_not_called()

    @patch('builtins.input', side_effect=[Exception('Mocked exception'), '5'])
    @patch('logging.error')
    @patch('pandas.DataFrame.to_csv')
    def test_execute_exception(self, mock_to_csv, mock_error, mock_input):
        """Test execute exception"""
        command = SubtractCommand()
        command.execute()
        mock_error.assert_called_once_with("Invalid input. Enter only numbers")
        mock_to_csv.assert_not_called()

if __name__ == "__main__":
    unittest.main()
