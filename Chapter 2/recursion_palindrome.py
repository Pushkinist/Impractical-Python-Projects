"""Recursive palindrome solution."""

import load_dictionary

WORDS_LIST = load_dictionary.load("2of4brif.txt")


def searcher(word):
    """Recusrsion search of palindromes."""
    if len(word) <= 1:
        return word
    if word[0] == word[-1]:
        return searcher(word[1:-1])


if __name__ == "__main__":
    for i in WORDS_LIST:
        if searcher(i):
            print(i)
