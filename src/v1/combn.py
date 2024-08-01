import json
from itertools import product


# by hunter


# All comb
def combiner(v, n, pre='', suf=''):
    """
    A function that generates all combinations of a certain length from a given set of elements.

    Parameters:
    v (list): The list of elements to generate combinations from.
    n (int): The length of combinations to generate.
    pre (str): The prefix to add to each combination (default '').
    suf (str): The suffix to add to each combination (default '').

    Returns:
    list: A list of combinations with prefix and suffix added.
    """
    # Generating all combinations of length n from elements in v
    r = [''.join(combination) for combination in product(v, repeat=n)]
    # Adding prefix and suffix to each combination
    r = [pre + item + suf for item in r]
    return r

def save_combinations_to_file(filename, combinations):
    with open(filename, 'w') as file:
        json.dump(combinations, file)

def load_combinations_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_progress(filename, progress):
    with open(filename, 'w') as file:
        json.dump(progress, file)

def load_progress(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"n": 1, "index": 0}

def main():
    """
    The main function that generates combinations of characters from lowercase letters, uppercase letters, digits, and symbols.
    It saves the combinations to a file and keeps track of the progress in a separate file.

    Parameters:
    None

    Returns:
    None
    """
    lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    sum_of = lower_letters + upper_letters + digits + symbols

    progress_file = 'progress.json'
    combinations_file = 'combinations.json'

    # Load progress
    progress = load_progress(progress_file)
    n = progress["n"]
    index = progress["index"]

    while n < 10:
        combinations = combiner(sum_of, n)
        # If continuing from a previous run, only save the remaining combinations
        combinations = combinations[index:]
        save_combinations_to_file(combinations_file, combinations)

        print(f'Saved {len(combinations)} combinations of length {n}.')

        # Reset index and move to next length
        index = 0
        n += 1
        progress = {"n": n, "index": index}
        save_progress(progress_file, progress)

if __name__ == "__main__":
    main()
