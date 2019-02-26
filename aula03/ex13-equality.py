def separate_first_input(text):
    split_text = text.split(" ")
    total = int(split_text[0])
    last_letter = int(split_text[1])
    return total, last_letter


def get_all_chars_until(i):
    letters = []
    for k in range(97, i+97):
        letters.append(chr(k).upper())
    return letters


def get_letter_frequency(letter, text):
    freq = 0
    for c in text:
        if c == letter:
            freq += 1
    return freq


def main():
    first_input = input()
    (total, last_letter) = separate_first_input(first_input)
    text = input()
    letters_array = get_all_chars_until(last_letter)
    min_value = total
    for letter in letters_array:
        freq = get_letter_frequency(letter, text)
        if freq < min_value:
            min_value = freq
    print(min_value*last_letter)


if __name__ == "__main__":
    main()
