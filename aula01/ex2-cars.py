def sumStringNumbers(text):
    sum = 0 
    for c in text:
        if c != " ":
            sum += int(c)
    return sum


carsNumber = int(input())
people = input()
integerDivision = sumStringNumbers(people)//5
if sumStringNumbers(people)%5 != 0:
    integerDivision += 1
print(integerDivision)

"""
Input: 
- the first one is a number of cars available (important for C programs, for example)
- the second is a list of numbers, separated by a space (" "). It contains the quantity of people
  that came in each car

Ex.:
3
1 2 4 

"""
