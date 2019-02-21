def main():
    """
    Input:
    - the first one is the number of words that will be input (important for C programs, for example)
    - the next following lines contain the words to be transformed

    Ex.:
    4
    word
    internationalization
    communication
    world
    """
    def substitute_text(text):
        new_text = ""
        letters_sum = 0
        text_size = len(text)
        if text_size > 10:
            for index, c in enumerate(text):
                if index == 0:
                    new_text += c
                elif index < text_size -1:
                    letters_sum += 1
                elif index == text_size-1:
                    new_text += str(letters_sum) + c
            return new_text
        else:
            return text

    wordsQuantity = int(input())
    wordsListResult = []
    for i in range(0, wordsQuantity):
        text = input()
        wordsListResult.append(substitute_text(text))
    for item in wordsListResult:
        print(item)


if __name__ == '__main__':
    main()
