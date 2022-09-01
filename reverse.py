def reverse(myList = []):
    if len(myList) == 0:
        return myList
    else:
        length = len(myList)
        fIndex = length-1
        switch = 0;
        for i in range(0, length/2):
            switch = myList[fIndex]
            myList[fIndex] = myList[i]
            myList[i] = switch
            fIndex -= 1
        return myList

# Test Data
td1 = [1,2,3,4,5,6,7,8,9,10,11,12]
td2 = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
td3 = []
print("Original arrays: ")
print(td1)
print(td2)
print(td3)
print("---------------------")
print(reverse(td1))
print(reverse(td2))
print(reverse(td3))

try:
    more = str(raw_input("Would you like to input your own data? (y or n): "))
    choice = str(raw_input("Are you entering strings or ints? ('string', 'int'): "))
    if(more == 'y'):
        if(choice == 'string'):
            newList = []
            size = int(raw_input("How many elements? "))
            for i in range(0,size):
                element = str(raw_input())
                newList.append(element)
            print(reverse(newList))
        elif(choice == "int"):
            newList = []
            size = int(raw_input("How many elements? "))
            for i in range(0,size):
                element = int(raw_input())
                newList.append(element)
            print(reverse(newList))
        else:
            print("Neither option selected")
    else:
        print("Have a good day.")
except:
    print("Error: wrong input")
