# combn.py

# Combination Generator

This project is a Python application that generates all possible combinations of a certain length using a specific character set. The combinations are saved to a file and the program can resume from where it left off when reopened.

## Requirements

- Python 3.x
- `itertools` module (standard library in Python)

## Installation

To run this project, you don't need to install any additional dependencies. Just make sure that Python 3.x is installed.

## Usage

1. Download or clone the project files.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the `main.py` file:


## Structure

- `main.py`: The main program that generates and saves combinations to a file. It can resume from where it left off.
- `combinations.json`: The file where combinations are saved.
- `progress.json`: The file that keeps track of the program's progress.

## Warning

This program may require a lot of RAM to generate a large number of combinations. Make sure you have enough RAM on your system. Otherwise, the program may slow down or crash. The RAM usage will increase as the combination length increases. Therefore, be careful when running long combinations and limit the n value if necessary.

### Example:

1. For a combination of a certain length, there are 72 combinations (26 lowercase letters + 26 uppercase letters + 10 digits + 10 symbols).
2. For a combination of a certain length, there are 5184 combinations (26 lowercase letters + 26 uppercase letters + 10 digits + 10 symbols)^2.
3. For a combination of a certain length, there are 373248 combinations (26 lowercase letters + 26 uppercase letters + 10 digits + 10 symbols)^3.

The RAM usage will increase as the combination length increases. Therefore, be careful when running long combinations and limit the n value if necessary.

# combnV2.py


### Combination Generator V2

The project is a Python application that generates all possible combinations of a certain length using a specific character set. The combinations are saved to a SQLite database. The program can resume from where it left off when reopened.

#### Setup

1. Download or clone the project files.
2. Open a terminal or command prompt and navigate to the project directory.
3. Create a new database using `setup.py` or edit the `config.json` file.
4. Run `python setup.py` to create the database.
5. Run `python main.py` to generate combinations.

#### Config.json

The `config.json` is used to configure the application. It contains the following fields:

- `lower_letters`: List of lowercase letters.
- `upper_letters`: List of uppercase letters.
- `digits`: List of digits.
- `symbols`: List of symbols.
- `symbol`: Boolean value indicating whether symbols are included in the combinations.
- `digit`: Boolean value indicating whether digits are included in the combinations.
- `space`: Boolean value indicating whether spaces are included in the combinations.
- `length`: The length of the combinations.
- `db_name`: The name of the SQLite database file.

#### Setup.py

The `setup.py` file is used to create the database. It has the following functionality:

- It prompts the user to enter a database name.
- It creates a new SQLite database with the specified name.
- It saves the database name to the `config.json` file.

#### RAM Usage

The RAM usage optimized

#### Progress

The program keeps track of its progress in the `progress.json` file. It is not necessary to edit this file manually.

#### Combinations

The combinations are saved to a SQLite database. The database has two tables: `combinations` and `config`. The `combinations` table stores the combinations, and the `config` table stores the configuration values.


#### Checking for duplicates

The program checks for duplicates by generating the SHA256 hash of each combination and comparing it with the hashes of existing combinations in the database.

#### Multiprocessing

The program uses multiprocessing to generate combinations in parallel. It creates a pool of worker processes and assigns each process a portion of the combinations to generate.

#### Limiting the number of worker processes

The number of worker processes is limited to the number of CPU cores available on the system.

#### Saving combinations to the database

The program saves each combination to the `combinations` table in the database. It also saves the configuration values to the `config` table.
