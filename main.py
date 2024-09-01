def text_to_binary(text):
    """
    Translate text into binary code using my program made in Python!

    (made by jxshuaa on dc)

    Args:
        text (str): The text to be translated.

    Returns:
        str: The binary representation of the text.
    """

    binary = ' '.join(format(ord(char), '08b') for char in text)
    return binary

def binary_to_text(binary):
    """
    Translate binary code to text.

    (made by jxshuaa on dc)

    Args:
        binary (str): The binary code to be translated to text.
    
    Returns:
        str: The text representation of the binary code.
    """

    text = ''
    binary_values = binary.split()
    for value in binary_values:
        text += chr(int(value, 2))
    return text


def main():
    while True:
        print("Binary Translator Program")
        print("ppst this was made by jxshuaa")
        print("1. Text to Binary")
        print("2. Binary to Text")
        print("3. Quit")
        choice = input("Enter your choice:  ")

        if choice == '1':

            text = input("Enter the text to translate: ")

            binary = text_to_binary(text)

            print(f"Binary representation: {binary}")

        elif choice == '2':

            binary = input("Enter the binary code to translate: ")

            text = binary_to_text(binary)

            print(f"Text representation: {text}")

        elif choice == '3':

            break

        else:

            print("Invalid choice. Please try again.")


if __name__ == "__main__":

    main()
