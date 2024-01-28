
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

# Project Overview

This project utilizes DuckDB as a local database for development purposes. The raw data for this project comprises several .csv files, totaling 2GB, which have been loaded into the DuckDB database. The primary objective of DuckDB is to take the .csv files, create a table in a local database file, and subsequently export this table to a .parquet file in an AWS S3 Bucket.

Following this, the project leverages dbt (data build tool) to retrieve data from the AWS S3 Bucket, perform transformations, and load it into a local database file. Additionally, dbt is responsible for generating a local documentation covering all transformations, schemas, tests, and other relevant information within this layer of the project.

## TODO List

- [x] Extract data from .csv files into DuckDB
- [x] Create the transactions table from the appended files
- [x] Export the transactions table to a local .parquet file
- [x] Export the transactions table to a .parquet file in the AWS S3 Bucket
- [x] Establish the dbt project
- [x] Retrieve data from the AWS S3 Bucket into dbt
- [x] Create the transaction table within the dbt project
- [x] Define the transaction table schema in the dbt project (including tests for each column)
- [x] Initial testing and building of the dbt project
- [ ] Decompose the transaction table into Fact and Dimension tables
- [ ] Create schemas for Fact and Dimension tables in the dbt project (including tests for each column)
- [ ] Second round of testing and building for the dbt project
- [ ] Update dbt documentation with comprehensive details related to the project
- [ ] Publish the dbt documentation on GitHub Pages



# Contact

LinkedIn: [Alan Lanceloth Rodrigues Silva](https://www.linkedin.com/in/alanlanceloth/)

E-mail: [alan.lanceloth@gmail.com](mailto:alan.lanceloth@gmail.com)
