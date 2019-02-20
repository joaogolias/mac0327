def substituteText(text):
    newText=""
    lettersSum = 0
    textSize = len(text)
    if textSize > 10:
        for i,c in enumerate(text):
            if(i==0):
                newText+=c
            elif (i < textSize -1):
                lettersSum+=1
            elif (i == textSize-1):
                newText += str(lettersSum) + c
        return newText
    else:
        return text

wordsQuantity = int(input())
wordsListResult = []
for i in range(0,wordsQuantity):
    text = input()
    wordsListResult.append(substituteText(text))
for item in wordsListResult:
    print(item)
    
            
