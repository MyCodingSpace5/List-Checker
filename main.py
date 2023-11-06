inputarray = []
enterelements = input("Enter data elements into the array seperate data entries by using commas")
inputarray = enterelements.split(",")
whatelementtocheck = input("What do you want to check for")
def checkforcharacter(char, array):
    charcount = 0
    for i in range(len(array)):
        if(inputarray[i] == char):
            charcount+=1
        else:
            continue
    if(charcount >= 2):
        return charcount
    else:
        return charcount
print("There is  " + str(checkforcharacter(whatelementtocheck, inputarray)) + " of  " + str(whatelementtocheck))#Test statement for the first mechanism
for i in inputarray:
    result = checkforcharacter(inputarray[i], inputarray)
    if(result >= 2):
        print("There are duplicate versions of " + inputarray[i])
    else:
        continue
