def getFirstLineFirstNumber(text):
    numbers = text.split(" ")
    return int(numbers[0])

def getSecondLineFirstNumber(text):
    numbers = text.split(" ")
    return int(numbers[3])

linesNumber = int(input())
results = []
for i in range(0, linesNumber):
    linesRange = input()
    fLfN = getFirstLineFirstNumber(linesRange)
    sLfN = getSecondLineFirstNumber(linesRange)
    if(fLfN == sLfN):
        sLfN += 1
    results.append(str(fLfN) + " " + str(sLfN))
for item in results:
    print(item)
