
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

## Testing the project set up
Before test the project, make sure that you have installed duckdb properly. To do that, check if you have the duckdb in your terminal.

In the terminal:
```bash
duckdb
```
If the above code don't work properly, go to the [duckdb download page](https://duckdb.org/docs/installation/index?version=latest&environment=cli&installer=binary&platform=win) and get the latest zip file. Extract the duckdb.exe and put inside your project folder. This will allow you to use the duckdb in the terminal.
Another option is to do the winget installation step recomended in the documentation (for windows, for other OS check the documentation).

```bash
winget install DuckDB.cli
```

# The project

This project uses the duckdb as a local database and to serve as a developer ambience. The raw data of this project was some .csv files (2GB of csv files) that have been loaded inside the duckdb database. The purpose of the duckdb is to get the csv files, create a table in a local database file, and then export this table to a .parquet file in a AWS S3 Bucket.

Then, we use the dbt to get this data from AWS S3 Bucket and do some transformations, and load in a database local file.

The dbt also build a local documentation for all the transformations, schemas, testing and everithing related to this layer of the project.


# Contact

LinkedIn: [Alan Lanceloth Rodrigues Silva](https://www.linkedin.com/in/alanlanceloth/)

E-mail: [alan.lanceloth@gmail.com](mailto:alan.lanceloth@gmail.com)
