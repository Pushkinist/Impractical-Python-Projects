"""Recursive palindrome solution."""

import load_dictionary

WORDS_LIST = load_dictionary.load("2of4brif.txt")


def searcher(word):
    if len(word) == 0 or len(word) == 1:
        return True
    else:
        if word[0] == word[-1]:
            return searcher(word[1:-1])


if __name__ == "__main__":
    for word in WORDS_LIST:
        if searcher(word):
            print(word)
