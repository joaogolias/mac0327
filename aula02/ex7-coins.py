def minimum_quantity(maximum_value, required_value):
    integer_result = required_value // maximum_value
    if required_value % maximum_value > 0:
        return integer_result+1
    else:
        return integer_result


def main():
    text_input = input()
    split_text = text_input.split(" ")
    coin_maximum_value = int(split_text[0])
    required_value = int(split_text[1])
    print(minimum_quantity(coin_maximum_value, required_value))
    return


if __name__ == '__main__':
    main()
