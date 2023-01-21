#Reid Witte
#Referencing W3Schools for assistance

def get_unique_list(inputList):
    outputList = []
    for x in inputList:
        if(outputList.count(x) == 0):
            outputList.append(x)
    return outputList

my_list = [1,2,3,2,1,4]
unique_list = get_unique_list(my_list)
print(unique_list)