# 🍽 `Boilerplate`

## Authors

- [@Adarsh Battu](https://github.com/adarshbattu109)
- [@Vaibhav Bakliwal](https://github.com/bakliwalvaibhav1)

## Description

Do you ever had an awesome ✨ idea that you just wanted to get started with ?

But setting up the project and associated files taking too much of your time 😕.

Then 🍽 `Boilerplate` is just for your.

`Boilerplate` is a project to create all projects.

It creates 🐍 PyPA compatible folder structure 👍 and adds all the necessary project files like `pyproject.toml`, `setup.cfg` etc.

Also it will help you get started with a fully working 👨‍💻 `Dev` & 🧪`Test` Environment with all the necessary python modules to get that extra time ⌛ boost.

## Installation

💻 Create a Virtual Environment

```bash
  # Install the virtualenv module
  pip install virtualenv

  # Create the virtual Environment named venv
  python -m venv venv
  or
  virtualenv venv

  # Activate the Virtual Environment
  venv\Scripts\activate
```

🚀 Install the Application

```bash
  # Install the testing app
  pip install -e .
```

😎 Install the Extras

```bash
  # Install the Extras for Dev and Test
  pip install -e ".[dev, test]"
```

## ✔ Running Tests

To run the tests, refer the following

- ❄ Flake8

```bash
flake8 src test
```

- 🧪 Pytest

```bash
pytest -v
```

- 💘 mypy

```bash
mypy src test
```

- 🧹 pylint

```bash
pylint src test
```

- 🦅 vulture

```bash
vulture src test
```
