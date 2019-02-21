def verify_even_division(num):
    for i in range(2, num, 2):
        if (num-i)%2 == 0:
            print("YES")
            return
    print("NO")
    

watermelonWeight = int(input())
verify_even_division(watermelonWeight)

"""
Input: a single number that represents watermelon weight
ex: 8
"""
