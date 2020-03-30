"""Taking string and returning simple bar chart with letters."""
import pprint
import string
from collections import defaultdict


def main():
    """Create defaultdict from user input."""
    while True:
        user_input = input("Please, enter sentence:\n").lower()
        if user_input:
            user_input = [i for i in user_input if i in string.ascii_lowercase]
            letters = defaultdict(list, {i: [] for i in user_input},)
            for i in user_input:
                letters[i].append(i)
            pprint.pp(letters, sort_dicts=True)
        else:
            break


if __name__ == "__main__":
    main()
