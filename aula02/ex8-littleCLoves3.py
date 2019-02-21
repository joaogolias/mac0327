def main():
    n = int(input())
    first_value = 1
    second_value = 1
    third_value = n - first_value - second_value
    while third_value % 3 == 0 or second_value % 3 == 0:
        second_value = second_value + 1
        third_value = third_value - 1
    print(str(first_value) + " " + str(second_value) + " " + str(third_value))
    return


if __name__ == '__main__':
    main()
