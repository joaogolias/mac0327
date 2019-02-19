def verifyEvenDivision(input):
    for i in range(2, watermelonWeight, 2):
        if ((watermelonWeight-i)%2 == 0):
            print("YES")
            return
    print("NO")
    
watermelonWeight = int(input())
verifyEvenDivision(watermelonWeight)
