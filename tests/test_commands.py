"""Test cases for commands"""
import unittest
from unittest.mock import MagicMock
from app.commands import Command, CommandHandler

class MockCommand(Command):
    """Test command execution"""
    def execute(self):
        pass

class TestCommandHandler(unittest.TestCase):
    """Test commands and commandhandler"""
    def setUp(self):
        self.command_handler = CommandHandler()

    def test_register_command(self):
        """Test Registering a command"""
        command_name = "test_command"
        mock_command = MockCommand()
        self.command_handler.register_command(command_name, mock_command)
        self.assertIn(command_name, self.command_handler.commands)

    def test_execute_command_valid(self):
        """Test Execute command"""
        command_name = "test_command"
        mock_command = MockCommand()
        mock_command.execute = MagicMock()
        self.command_handler.register_command(command_name, mock_command)
        self.command_handler.execute_command(command_name)
        mock_command.execute.assert_called_once()

    def test_execute_command_invalid(self):
        """Test Execute command"""
        command_name = "invalid_command"
        with self.assertLogs(level='ERROR') as cm:
            self.command_handler.execute_command(command_name)
        self.assertEqual(cm.output, ['ERROR:root:Invalid input provided'])

if __name__ == "__main__":
    unittest.main()
