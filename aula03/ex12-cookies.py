def separate_nums(text):
    split_text = text.split(" ")
    total_sum = 0
    num_array = []
    for num in split_text:
        num_array.append(int(num))
        total_sum += int(num)
    return {"total_sum": total_sum, "num_array": num_array,}


def main():
    total_of_bags = int(input())
    cookies_in_each_bag = input()
    num_of_ways = 0
    separate_nums_result = separate_nums(cookies_in_each_bag)
    for num in separate_nums_result["num_array"]:
        if(separate_nums_result["total_sum"] - num)%2 == 0:
            num_of_ways+=1
    print(num_of_ways)


if __name__ == "__main__":
    main()
