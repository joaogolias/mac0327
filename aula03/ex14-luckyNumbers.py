def pot_of_two (p):
    return 2**p


def factorial(n):
    if n <= 1:
        return 1
    return n*factorial(n-1)


def main():
    num_digits = int(input())
    total = 0
    for i in range(1, num_digits+1):
        total += pot_of_two(i)
    print(total)
    return


if __name__ == "__main__":
    main()
