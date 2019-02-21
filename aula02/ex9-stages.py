def convert_text_to_array(text):
    result_array = []
    for char in text:
        result_array.append(char)
    return result_array


def get_char_weight(char):
    return ord(char) - 96


def main():
    first_input = input()
    second_input = input()
    max_quantity = int(first_input.split(" ")[1])
    array = convert_text_to_array(second_input)
    array.sort()
    last_stage = " "
    weight_sum = 0
    stage_flow = ""
    stages_number = 0
    for index, stage in enumerate(array):
        if get_char_weight(stage) - get_char_weight(last_stage) > 1:
            last_stage = stage
            weight_sum += get_char_weight(stage)
            stages_number += 1
            stage_flow += stage
        if stages_number >= max_quantity:
            break
        if index == len(array) - 1 and stages_number != max_quantity:
            weight_sum = -1
    print(weight_sum)
    return


if __name__ == '__main__':
    main()
