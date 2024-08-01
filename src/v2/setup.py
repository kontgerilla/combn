from json import dump
from os import path
def create_database(db_name):
    from sqlite3 import connect
    conn = connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS combinations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        password TEXT NOT NULL,
        length INTEGER NOT NULL,
        symbol BOOLEAN NOT NULL,
        space BOOLEAN NOT NULL,
        sha256 TEXT NOT NULL
    )''')
    c.close()
    return True


def create_config():
    default_config = {
        "lower_letters": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
        "upper_letters": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"],
        "digits": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
        "symbols": ["!", "#", "$", "%", "&", "(", ")", "*", "+"],
        "symbol": True,
        "digit": True,
        "space": True,
        "length": 5,
        "db_name": "combinations.db"
    }
    while True:
        config_file = "config.json"
        if not path.isfile(config_file):
            with open(config_file, 'w') as file:
                dump(default_config, file)
            print("Config file created.")
            break
        else:
            print("Config file already exists.")
# run this func if you want to create a new database
while True:
    db_name = input("Enter database name: ")
    db_name += ".db"
    if create_database(db_name):
        break

