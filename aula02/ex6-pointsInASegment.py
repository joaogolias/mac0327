def parse_input(text):
    split_text = text.split(" ")
    return {'quantity': split_text[0], 'maximum': split_text[1]}


def populate_numbers_array(array, start_value, final_value):
    for num in range(start_value, final_value+1):
        if num not in array:
            array.append(num)
    array.sort()

def main():
    first_input = input()
    parsed_input = parse_input(first_input)
    lines_quantity = int(parsed_input['quantity'])
    maximum_value = int(parsed_input['maximum'])
    numbers_array = []
    for index in range(0, lines_quantity):
        second_input = input()
        split_second_input = second_input.split(" ")
        start_value = int(split_second_input[0])
        final_value = int(split_second_input[1])
        populate_numbers_array(numbers_array, start_value, final_value)
    all_numbers_in_range  = []
    populate_numbers_array(all_numbers_in_range, 1, maximum_value)
    result = ""
    numbers_missing_quantity = 0
    for num in all_numbers_in_range:
        if num not in numbers_array:
            numbers_missing_quantity += 1
            result += str(num) + " "
    print(numbers_missing_quantity)
    print(result)
    return


if __name__ == '__main__':
    main()
