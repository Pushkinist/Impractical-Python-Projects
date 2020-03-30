"""Making Pig Latin words from input."""


def main():
    """Asking for input and returning Pig Latin version."""
    vowels = ("a", "e", "i", "o", "u", "y")
    while True:
        user_input = input("Please, enter the word:\n")
        if user_input:
            print(
                "".join(
                    [
                        i[1:] + i[0] + "ay" + " "
                        if user_input[0] not in vowels
                        else i + "way" + " "
                        for i in user_input.split(" ")
                    ]
                )
            )
        else:
            break


if __name__ == "__main__":
    main()
