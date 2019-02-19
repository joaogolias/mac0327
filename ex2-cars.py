def sumStringNumbers(text):
    sum = 0 
    for c in text:
        if(c != " "):
            sum+=int(c)
    return sum

carsNumber=int(input())
people = input()
integerDivision = sumStringNumbers(people)//5
if (sumStringNumbers(people)%5 != 0):
    integerDivision += 1
print(integerDivision)
    
