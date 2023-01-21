#Reid Witte
#Referencing W3Schools for assistance

def count_letters(inputString):
    outputDict = {}
    inputString = inputString.lower()
    for x in inputString:
        if(outputDict.get(x, -1) == -1):
            outputDict.update({x:1})
        else:
            tempNum = outputDict.get(x)
            outputDict.pop(x)
            outputDict.update({x: tempNum+1})
    if(outputDict.get(' ', -1) != -1):
        outputDict.pop(' ');
    return outputDict

userInput = input("Enter a string: ")
print(count_letters(userInput))