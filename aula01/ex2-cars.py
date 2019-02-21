def sum_string_numbers(text):
    sum = 0 
    for c in text:
        if c != " ":
            sum += int(c)
    return sum


cars_number = int(input())
people = input()
integer_division = sum_string_numbers(people)//5
if sum_string_numbers(people) % 5 != 0:
    integer_division += 1
print(integer_division)

"""
Input: 
- the first one is a number of cars available (important for C programs, for example)
- the second is a list of numbers, separated by a space (" "). It contains the quantity of people
  that came in each car

Ex.:
3
1 2 4 

"""
