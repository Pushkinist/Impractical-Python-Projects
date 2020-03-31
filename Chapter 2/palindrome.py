import load_dictionary

word_list = load_dictionary.load("2of4brif.txt")

pali_list = [i for i in word_list if i == i[::-1]]

print(*pali_list, sep="\n")
