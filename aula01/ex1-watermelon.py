def verifyEvenDivision(num):
    for i in range(2, num, 2):
        if (num-i)%2 == 0:
            print("YES")
            return
    print("NO")
    

watermelonWeight = int(input())
verifyEvenDivision(watermelonWeight)
