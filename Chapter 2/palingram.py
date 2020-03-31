"""Two-word palingram solution."""

import load_dictionary

WORD_LIST = load_dictionary.load("2of4brif.txt")

# Palingram search func
def main():
    """Find palingrams."""
    pali_list = []
    for word in WORD_LIST:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[: end - i] and rev_word[end - i :] in WORD_LIST:
                    pali_list.append((word, rev_word[end - i :]))
                if word[i:] == rev_word[end - i :] and rev_word[: end - i] in WORD_LIST:
                    pali_list.append((rev_word[: end - i], word))
    return pali_list


PALINGRAMS = main()

# Sort palingrams
PALINGRAMS_SORTED = sorted(PALINGRAMS)

# Prety printing palingrams
print("\nNumber of palingrams = {}\n".format(len(PALINGRAMS_SORTED)))

for first, second in PALINGRAMS_SORTED:
    print("{} {}".format(first, second))
