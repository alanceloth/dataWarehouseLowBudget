
Welcome to my default Data Project Repo.

To use this project structure you will need to follow the steps below.

# Requirements
To use this project properly, you will need to install:
- [python](https://www.python.org/downloads/)
- [git](https://git-scm.com/downloads)
- [pyenv](https://pypi.org/project/pyenv/)
- [poetry](https://python-poetry.org/)

To install and configure Pyenv and Poetry in Windows, check [this video](https://www.youtube.com/watch?v=547Jr26duHQ&pp=ygUgaG93IHRvIGluc3RhbGwgcG9ldHJ5IGluIHdpbmRvd3M%3D).
To learn how to manage multiple python versions using pyenv, check [this article](https://realpython.com/intro-to-pyenv/).

# Installation Steps

## Git Clone
Open a terminal window (cmd, bash, or anything with git commands) and type:
```bash
git clone https://github.com/alanceloth/myDefaultDataProject.git
cd myDefaultDataProject
```

## Setting up the environment
We will need python 3.11.5, and to get this version we will use pyenv.
In the same terminal window, type:

```bash
pyenv update
pyenv install --list
```
If you find the 3.11.5, then it's everithing correct.

```bash
pyenv install -v 3.11.5
```

To check the python versions installed, use this:
```bash
pyenv versions
```
You will notice that one of the versions will have a * symbol. This indicates that the system is using this version.
You can also check the default python version used by the system with this:
```bash
python -v
```
Or:
```bash
which python
```

To use the project python version (3.11.5), use the command below:

```bash
pyenv local 3.11.5
```

## Poetry

To initialize the poetry in the project, type in the terminal:

```bash
poetry shell
poetry env use 3.11.5
poetry install
```

## Testing

In the terminal:
```bash
duckdb
```

# Folder Structure

The basic project folder structure are shown below.
```bash
.
├── .vscode
├── docs
├── scripts
├── src
└── tests
```

.vscode: VSCODE setting to the project session, like font size.
docs: documentation folder, will store the mkdocs index.md
scripts: any script related to automation, instalation, compilation, test execution.
src: the source code folder
tests: the automated test folder to check the source code


# Contact

LinkedIn: [Alan Lanceloth Rodrigues Silva](https://www.linkedin.com/in/alanlanceloth/)

E-mail: [alan.lanceloth@gmail.com](mailto:alan.lanceloth@gmail.com)
