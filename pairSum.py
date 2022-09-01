
def pairsum(myList = []):
    try:
        if myList:
            sums = []
            length = len(myList)
            if length%2 == 0:
                for i in range(0,length, 2):
                    sums.append(myList[i]+myList[i+1])
            else:
                for i in range(0,length, 2):
                    if i == length-1:
                        sums.append(myList[i]+0)
                    else:
                        sums.append(myList[i]+myList[i+1])
            return sums
        else:
            return myList
    except:
        print("An error occurred... Terminating")

# Test Data
oddList = [1,2,3,4,5,6,7]
evenList = [-1,0,2,3,4,5,6,-7,8,9]
empList = []
print("Original data:")
print(oddList)
print(evenList)
print(empList)

print("-------------------")

print (pairsum(empList))
print(pairsum(oddList))
print (pairsum(evenList))

# User input
more = str(raw_input("Would you like to input your own data? (y or n): "))
try:
    if(more == 'y'):
        newList = []
        size = int(input("How many elements? "))
        for i in range(0,size):
            element = int(input())
            newList.append(element)
        print(pairsum(newList))
    else:
        print("Have a good day.")
except:
    print("Error: int not detected")
