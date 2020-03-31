"""Simple palindrome solution."""

import load_dictionary

WORD_LIST = load_dictionary.load("2of4brif.txt")

PALI_LIST = [i for i in WORD_LIST if i == i[::-1]]

print(*PALI_LIST, sep="\n")
