# 🍽 Boilerplate

## Table of Contents

- [Project Title & Description](#-boilerplate-generator)
- [Feature Highlights](#feature-highlights-)
- [Directory Structure](#directory-structure-)
- [Architecture & Data Flow](#architecture--data-flow-)
- [Filters & Controls](#filters--controls-)
- [Installation Guide](#installation-guide-)
- [Environment Configuration](#environment-configuration-)
- [Usage Examples](#usage-examples-)
- [API Reference](#api-reference-)
- [Testing](#testing-)
- [Contributing Guidelines](#contributing-guidelines-)
- [Authors and Maintainers](#authors-and-maintainers-)

## Project Title & Comprehensive Description

### What It Does

The Boilerplate Generator is a Python application that automates the creation of PyPA (Python Packaging Authority) compliant project structures. It generates a complete project skeleton with preconfigured development and testing environments, eliminating the tedious manual setup process when starting new Python projects.

### Problem It Solves

Developers often spend valuable time setting up project directories, configuration files, and development environments before writing actual code. This tool solves that problem by providing an automated solution that creates a professional project structure in seconds, allowing developers to focus on implementing their ideas rather than boilerplate setup.

### Why It Was Built

The Boilerplate Generator was built to streamline the Python project initialization process. It standardizes project structures, ensures best practices are followed from the start, and provides a consistent foundation for all Python projects. This tool embodies the "convention over configuration" principle, reducing cognitive load and setup time.

## Feature Highlights ✨

- **Automated Project Structure Creation**: Generates a standardized Python project layout with `src` and `test` directories
- **Interactive Command-Line Interface**: Uses `InquirerPy` to guide users through project setup with intuitive prompts
- **Template-Based File Generation**: Creates essential files like `pyproject.toml`, `setup.py`, `.gitignore`, and `README.md` with user-specific content
- **Virtual Environment Setup**: Automatically creates isolated Python environments and installs selected packages
- **Package Selection System**: Allows users to choose from popular static code analysis tools, linters, formatters, and testing frameworks
- **Cross-Platform Compatibility**: Works seamlessly on Windows, macOS, and Linux operating systems
- **PyPA Compliance**: Generates projects that follow Python Packaging Authority standards
- **Extensible Architecture**: Modular design makes it easy to add new features and templates

## Directory Structure 📁

```
boilerplate/
├── src/
│   └── boilerplate/
│       ├── __init__.py          # Entry point that initializes the application
│       ├── boilerplate.py       # Core logic for project generation and setup
│       ├── cli.py               # Interactive command-line interface functions
│       ├── constants.py         # Configuration constants and package lists
│       ├── file_content.py      # Template strings for generated files
│       ├── helper.py            # Utility functions for file/directory operations
│       └── messages.py          # User-facing messages and prompts
├── test/
│   └── test_cli.py              # Unit tests for CLI functionality
├── htmlcov/                     # Code coverage reports (generated)
├── pyproject.toml               # Project metadata and build configuration
├── README.md                    # Project documentation
└── uv.lock                      # UV package lock file
```

## Architecture & Data Flow 🔧

```
┌─────────────────────────────────────────────────────────────┐
│                    User Interaction Layer                   │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐     Prompt User      ┌─────────────────┐  │
│  │             │ ───────────────────→ │                 │  │
│  │   __init__  │                       │       CLI       │  │
│  │             │ ◄──────────────────── │                 │  │
│  └─────────────┘    Gather Inputs      └─────────────────┘  │
├─────────────────────────────────────────────────────────────┤
│                    Processing Layer                         │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────────┐                                        │
│  │                 │                                        │
│  │  boilerplate.py │                                        │
│  │                 │                                        │
│  └─────────────────┘                                        │
│           │                                                 │
│           │ Execute Steps                                   │
│           ▼                                                 │
│  ┌─────────────────┐    Create Directories   ┌────────────┐│
│  │                 │ ──────────────────────→ │            ││
│  │    helper.py    │                         │   Paths    ││
│  │                 │ ◄────────────────────── │            ││
│  └─────────────────┘    Return Status        └────────────┘│
│           │                                                 │
│           │ Create Files                                    │
│           ▼                                                 │
│  ┌─────────────────┐    Generate Content     ┌────────────┐│
│  │                 │ ──────────────────────→ │            ││
│  │ file_content.py │                         │ Templates  ││
│  │                 │ ◄────────────────────── │            ││
│  └─────────────────┘    Substituted Files    └────────────┘│
│           │                                                 │
│           │ Setup Environment                               │
│           ▼                                                 │
│  ┌─────────────────┐                                        │
│  │                 │                                        │
│  │    helper.py    │                                        │
│  │                 │                                        │
│  └─────────────────┘                                        │
└─────────────────────────────────────────────────────────────┘
           │
           │ Install Packages
           ▼
┌─────────────────────────────────────────────────────────────┐
│                    System Integration Layer                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Virtual Environment ←→ Package Managers (pip/uv)           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Filters & Controls 🎛️

| Parameter     | Type           | Description                            | Options                      |
| ------------- | -------------- | -------------------------------------- | ---------------------------- |
| BASE_DIR      | Directory Path | Location where project will be created | Any valid directory path     |
| ROOT_DIR_NAME | String         | Name of the project root folder        | User-defined string          |
| AUTHOR_NAME   | String         | Project author's name                  | User-defined string          |
| AUTHOR_EMAIL  | String         | Project author's email                 | User-defined string          |
| APP_NAME      | String         | Name of the application                | User-defined string          |
| SCA           | Multi-select   | Static Code Analysis tools             | flake8, mypy, vulture        |
| LINTER        | Boolean        | Install PyLint                         | Yes/No                       |
| FORMATTER     | Single-select  | Python code formatter                  | autopep8, black, isort, yapf |
| UNIT_TEST     | Boolean        | Install PyTest                         | Yes/No                       |
| FINAL_CONF    | Boolean        | Confirm installation                   | Yes/No                       |

## Detailed Installation Guide 🚀

### Prerequisites

- Python version 3.10 or higher
- pip package manager (usually comes with Python)
- Optional: [UV](https://github.com/astral-sh/uv) for faster installations

### Python Version Requirements

The application requires Python 3.10 or higher. Check your Python version:

```bash
python --version
```

### Virtual Environment Creation

The application automatically creates a virtual environment during setup, but you can also create one manually:

```bash
# Create virtual environment
python -m venv boilerplate-env

# Activate virtual environment
# On Windows:
boilerplate-env\Scripts\activate
# On macOS/Linux:
source boilerplate-env/bin/activate
```

### Dependency Installation

#### With UV (Recommended)

UV is a Python package installer that is significantly faster than pip:

```bash
# Install the application and dependencies
uv pip install -e .

# Install the Extras for Dev and Test
uv pip install -e ".[dev,test]"
```

#### Traditional pip

```bash
# Install the application
pip install -e .

# Install the Extras for Dev and Test
pip install -e ".[dev,test]"
```

### Dependencies Explained

- **Core Dependencies**:
  - `virtualenv`: For creating isolated Python environments
  - `inquirerpy`: For interactive command-line prompts
- **Development Dependencies** (`dev` group):
  - `black`: Code formatter
  - `flake8`: Style guide enforcement
  - `pylint`: Code analysis
  - `virtualenv`: Duplicate for environment management
- **Testing Dependencies** (`test` group):
  - `pytest`: Testing framework
  - `mypy`: Static type checker
  - `flake8`: Style guide enforcement
  - `coverage`: Code coverage measurement
  - `pytest-cov`: Pytest plugin for coverage reporting
  - `pylint`: Code analysis
  - `black`: Code formatter

## Environment Configuration ⚙️

### Required Environment Variables

No specific environment variables are required for basic operation.

### Configuration Files

The application generates several configuration files in created projects:

- `pyproject.toml`: Build system requirements and project metadata
- `setup.py`: Legacy setup script (for compatibility)
- `setup.cfg`: Project metadata and configuration
- `.gitignore`: Specifies files to ignore in Git

### System Requirements

- Minimum 50MB free disk space for virtual environment and dependencies
- Internet connection for downloading packages
- Write permissions to installation directory

## Usage Examples 📖

### Basic Usage

1. Run the application:

   ```bash
   boilerplate
   ```

2. Follow the interactive prompts:

   ```
   Thanks for choosing Boiler plate. Now let's get you started 🚀
   ? Provide the Path of the directory where the project Root folder and other items will be placed :  ~/projects
   ? Provide the Project Root folder name 🌳 ? :  my-awesome-project
   ? Who is the Author ✍ ? :  Jane Developer
   ? Author's Email ID 💌 ? :  jane@example.com
   ? Name of the Project 🗿 ? :  awesome-app
   ? Install Static Code Analysis Tools 🕵️‍♀️ ? :  flake8, mypy
   ? Install 'PyLint' 🧹 ? :  Yes
   ? Install 'Python Code Formatter' 💘 ? :  black
   ? Install `PyTest` 🧪 ? :  Yes
   ? Proceed with Installation 🚅 ? :  Yes
   ```

3. The application will:
   - Create project directory structure
   - Generate configuration files
   - Set up virtual environment
   - Install selected packages
   - Display success message

### Advanced Usage Example

Creating a minimal project with only essential features:

```bash
boilerplate
# Select only base directory, project name, author info
# Skip SCA, linter, formatter, and unit test installation
# Confirm to create minimal project structure
```

### Expected Output Structure

After successful execution, the generated project structure will look like:

```
my-awesome-project/
├── src/
│   └── awesome-app/
│       └── __init__.py
├── test/
├── venv/                    # Virtual environment (created during setup)
├── .gitignore
├── pyproject.toml
├── setup.py
├── setup.cfg
└── README.md
```

## API Reference 📘

### Main Module

#### `boilerplate.__init__:main() -> None`

Entry point for the application. Clears screen, displays welcome message, gathers requirements, and executes setup steps.

### Core Logic

#### `boilerplate.boilerplate:gather_requirements() -> dict[str, str]`

Collects user requirements through interactive prompts.

Parameters: None

Returns: Dictionary containing user inputs for project setup

#### `boilerplate.boilerplate:execute_steps(user_inputs: dict[str, str]) -> None`

Executes project creation steps based on user inputs.

Parameters:

- `user_inputs`: Dictionary of user preferences collected by `gather_requirements()`

### CLI Functions

#### `boilerplate.cli:get_location(message: str) -> Path`

Prompts user for directory path input.

Parameters:

- `message`: Prompt message to display to user

Returns: Path object representing user-selected directory

#### `boilerplate.cli:get_input(message: str) -> str`

Prompts user for text input.

Parameters:

- `message`: Prompt message to display to user

Returns: String input provided by user

#### `boilerplate.cli:get_confirmation(message: str) -> bool`

Prompts user for yes/no confirmation.

Parameters:

- `message`: Prompt message to display to user

Returns: Boolean representing user's choice

#### `boilerplate.cli:get_selection_from_choices(message: str, choices: list[str]) -> str`

Prompts user to select one option from a list.

Parameters:

- `message`: Prompt message to display to user
- `choices`: List of available options

Returns: String representing user's selection

#### `boilerplate.cli:get_multi_select_choices(message: str, choices: list[str]) -> list[str]`

Prompts user to select multiple options from a list.

Parameters:

- `message`: Prompt message to display to user
- `choices`: List of available options

Returns: List of strings representing user's selections

### Helper Functions

#### `boilerplate.helper:create_directory(path: Path) -> None`

Creates a directory at the specified path.

Parameters:

- `path`: Path where directory should be created

#### `boilerplate.helper:touch_file(path: Path) -> None`

Creates an empty file at the specified path.

Parameters:

- `path`: Path where file should be created

#### `boilerplate.helper:create_repo_files(file_type: str, file: Path, substitution_dict: dict[str, str]) -> None`

Creates project files with substituted content.

Parameters:

- `file_type`: Type of file to create (key in FILE_CONTENT_DICT)
- `file`: Path where file should be created
- `substitution_dict`: Dictionary of key-value pairs for content substitution

#### `boilerplate.helper:create_vitual_env_with_packages(venv_path: Path, packages: list[str]) -> int`

Creates virtual environment and installs specified packages.

Parameters:

- `venv_path`: Path where virtual environment should be created
- `packages`: List of package names to install

Returns: Integer return code (0 for success)

### Constants

#### `boilerplate.constants:FILE_CONTENT_DICT`

Dictionary mapping file types to template content strings.

#### `boilerplate.constants:REQUIREMENTS_SEQUENCE`

List defining the sequence of user requirements collection.

#### `boilerplate.constants:packages`

Dictionary of available packages grouped by category (SCA, LINTER, FORMATTER, UNIT_TEST).

#### `boilerplate.constants:requirement_steps`

Dictionary mapping requirement keys to (function, arguments) tuples for execution.

## Testing 🧪

### Running Tests

Execute the test suite using pytest:

```bash
# With UV (recommended)
uv run pytest -v

# Or traditional pip
pytest -v
```

### Running Specific Test Categories

#### Flake8 Style Checking

```bash
# With UV (recommended)
uv run flake8 src test

# Or traditional pip
flake8 src test
```

#### Pytest Unit Tests

```bash
# With UV (recommended)
uv run pytest -v

# Or traditional pip
pytest -v
```

#### Mypy Type Checking

```bash
# With UV (recommended)
uv run mypy src test

# Or traditional pip
mypy src test
```

#### Pylint Code Analysis

```bash
# With UV (recommended)
uv run pylint src test

# Or traditional pip
pylint src test
```

### Test Coverage

Coverage reports are automatically generated when running tests:

```bash
# Run tests with coverage
pytest -v --cov=boilerplate --cov-report=html

# Open HTML coverage report
# On Windows:
start htmlcov/index.html
# On macOS:
open htmlcov/index.html
# On Linux:
xdg-open htmlcov/index.html
```

### Writing New Tests

Tests are located in the `test/` directory. To add new tests:

1. Create a new test file in the `test/` directory
2. Follow the naming convention `test_*.py`
3. Use unittest framework with mock objects for isolation
4. Run tests to verify functionality

## Contributing Guidelines 🤝

We welcome contributions to the Boilerplate Generator! Here's how you can help:

### Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/your-username/boiler-plate.git
   cd boiler-plate
   ```
3. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -e ".[dev,test]"
   ```

### Making Changes

1. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Make your changes, following the existing code style
3. Add tests for any new functionality
4. Ensure all tests pass:
   ```bash
   pytest -v
   ```
5. Check code style:
   ```bash
   flake8 src test
   black src test
   ```

### Submitting Pull Requests

1. Push your changes to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
2. Open a pull request against the main repository
3. Include a clear description of your changes
4. Reference any related issues

### Code Standards

- Follow PEP 8 style guidelines
- Include docstrings for all public functions and classes
- Write unit tests for new functionality
- Keep commits focused and atomic
- Use descriptive commit messages

### Reporting Issues

- Check if the issue already exists
- Include steps to reproduce
- Specify your environment (OS, Python version)
- Provide error messages and stack traces when relevant

## Authors and Maintainers 👥

**Author**: Adarsh Battu <adarsh.battu109@gmail.com>

**Maintainer**: Adarsh Battu <adarsh.battu109@gmail.com>

For questions, suggestions, or issues, please contact the maintainer or open an issue on GitHub.
