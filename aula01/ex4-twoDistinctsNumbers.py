def get_first_line_first_number(text):
    numbers = text.split(" ")
    return int(numbers[0])


def get_second_line_first_number(text):
    numbers = text.split(" ")
    return int(numbers[2])


linesNumber = int(input())
results = []
for i in range(0, linesNumber):
    linesRange = input()
    fLfN = get_first_line_first_number(linesRange)
    sLfN = get_second_line_first_number(linesRange)
    if fLfN == sLfN:
        sLfN += 1
    results.append(str(fLfN) + " " + str(sLfN))
for item in results:
    print(item)
