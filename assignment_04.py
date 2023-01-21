#Reid Witte
#Referencing W3Schools for assistance

inputList = [0,0,0,0,0]
for x in range(5):
    inputList[x] = input("Enter int #" + str(x+1) + ": ")
    if(inputList[x].count('.') > 0):
        print("Invalid input. Please enter an int")
        x -= 1

sum = 0
for x in inputList:
    sum += int(x)

print("Your sum is " + str(sum))