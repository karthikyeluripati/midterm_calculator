# Midterm - Calculator

# Introduction

Implemented a REPL and directly interactable calculator. This interface supports the following

1. Execution of arithmetic operations (Add, Subtract, Multiply, and Divide)
2. Management of calculation history.
3. Access to extended functionalities through dynamically loaded plugins.

# Setup

## Setup Instructions
1. Clone the repo
2. CD into the project folder
3. Create a virtual environment
4. Activate the virtual environment (VE)
5. Install Requirements

## Test Commands
- `pytest` run all tests
- `pytest --pylint --cov` <- Run Pylint and Coverage (Can be run independently)

# Usage

## Functionlity

### Calculator Operations:

Basic arithmetic operations like add, subtract, multiply, and divide can be performed. With the help of the plugin architecture and dynamic loading design, we can add new features dynamically in the plugins folder without any hardcoding.

commands for the specific operation:

- `add` - Addition
- `subtract` - Subtraction
- `multiply` - Multiplication
- `divide` - Division
- `menu` - Shows the list of commands
- `exit` - Exit the application

menu command is to show all the available commands and will append the list if any new plugin is added in the future. The plugin names are parsed directly to show the list.

### History Management:

Effective data management methods are employed to handle the data.

commands to handle the data:

- `load` - Loads the history of operations performed
- `clear` - Clears the history
- `delete` - Deletes only specified index data 

history.csv contains the history of operations. The system effectively reads and writes the CSV file.

### Configuration via Environment Variables:

The application configuration details, development, and testing environment variables are stored in .env file.

### REPL Interface:

This application works on the Read-Evaluate-Print-Loop pattern.

![image](https://github.com/karthikyeluripati/midterm_calculator/assets/64483756/c41ae706-6414-404c-9507-23563622237b)


## Design Patterns

### Implementation and Application:

This application used and implemented various design patterns. *Facade pattern* was used for the Pandas data manipulation. The *Command pattern* is the REPL structure the application has and the application's code structure is flexible and scalable using *Factory Method*, *Singleton*, and *Strategy Patterns*.

## Testing and Code Quality

### Comprehensive tests using pytest:

The test cases are in the folder tests. Majorly used unit testing and assertions to check all possible outcomes. These test cases helped to increase the application's robustness.

- `pytest` run all tests
- `pytest --pylint --cov` <- Run Pylint and Coverage (Can be run independently)

test coverage = 91%

![alt text](image.png)

## Version Control, Documentation, and Logging

GitHub Actions performs all the tests while pushing or merging the code.

### Commit History:

This repo has kept a sequential and informative commit history for any reference

### Logging Practices:

Dynamic logging configuration through environment variables is performed. A professional logging system is designed and logs will contain all the critical steps while performing any operation. Detailed application operations, data manipulations, errors, and informational messages are provided using Logging. This system also retrieves and displays errors and handles exceptions without crashing the applications. Logging is majorly used in this application rather than print statements.

- `logging.info`- logs what happened in the line of code
- `logging.error` - logs the error that occurred after the line of code

![image](https://github.com/karthikyeluripati/midterm_calculator/assets/64483756/b5df1b9a-e83f-44a9-ae6b-1c18d25e2f88)
