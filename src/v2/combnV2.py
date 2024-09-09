import sqlite3
from hashlib import sha256
from multiprocessing import Pool, cpu_count
from json import load
from time import sleep
from colorama import init, Fore, Style
from os import system, listdir


# Author: hunter discord: (kontragerillagdu)
# Colorama initialization
init(autoreset=True)

def load_config(config_file):
    try:
        with open(config_file, 'r') as file:
            config = load(file)
        return config
    except FileNotFoundError:
        print(Fore.RED + "Config file not found!");sleep(2)
        print(Fore.RED + "Exiting...")
        exit()
def save_combination(db_name, combination_data):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''INSERT INTO combinations (password, length, symbol, space, sha256) VALUES (?, ?, ?, ?, ?)''', combination_data)
    conn.commit()
    conn.close()
    

def generate_combinations(letters, length):
    if length == 0:
        return ['']
    smaller_combinations = generate_combinations(letters, length - 1)
    combinations = []
    line = 0
    for char in letters:
        for comb in smaller_combinations:
            line += 1
            print(Fore.GREEN +str(char) + str(comb), Fore.YELLOW+ f"{sha256((str(char) + str(comb)).encode()).hexdigest()}", Fore.MAGENTA + f"{line}. Progress", Style.RESET_ALL)
            combinations.append(str(char) + str(comb))
    return combinations

def process_combination(password):
    length = len(password)
    symbol = any(char in "!@#$%^&*()_+-=[]{}|;':\",./<>?" for char in password)
    space = ' ' in password
    sha256_ = sha256(password.encode()).hexdigest()

    return (password, length, symbol, space, sha256_)

def generate_and_save_combinations(config):

    lower_letters = config['lower_letters']
    upper_letters = config['upper_letters']
    digits = config['digits']
    symbols = config['symbols']
    if config['symbol']:
        letters = lower_letters + upper_letters + digits + symbols
    else:
        letters = lower_letters + upper_letters + digits
    if config['space']:
        letters.append(' ')

    length = config['length']
    db_name = config['db_name']

    with Pool(cpu_count()) as pool:
        combination_data = pool.map(process_combination, generate_combinations(letters, length))

    for data in combination_data:
        save_combination(db_name, data)


config = load_config('config.json')
def is_config_ready():
        if "config.json" not in listdir():return False
        if 'lower_letters' in config and 'upper_letters' in config \
        and 'digits' in config and 'symbols' in config and 'symbol' in config\
        and 'space' in config and 'length' in config and 'db_name' in config:return True
        else:return False
if __name__ == "__main__":
    try:
        if not is_config_ready():
            print(Fore.RED + "Config is not ready! Please edit config.json and try again...");sleep(2)
            print(Fore.RED + "Exiting...");sleep(1)
            exit()
        print(Fore.BLUE + "Author: hunter discord (kontragerillagdu)");sleep(2)
        print(Fore.GREEN+ f"config.json is ready and all combinations will be saved in {config['db_name']} ");sleep(2)
        print(Fore.RED+"Attention!", Fore.MAGENTA + ": If you close the program will lost all progress. Pls wait for finishing...");sleep(2)
        print(Fore.BLUE + "If you want to stop the program, press Ctrl+C");sleep(2)
        print(Fore.GREEN + "Generating combinations...");sleep(1)
        generate_and_save_combinations(config); print("Done!");sleep(10000)
    except KeyboardInterrupt:
        print("Exiting...")
