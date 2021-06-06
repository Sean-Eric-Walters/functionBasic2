#Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
def countDown(num):
    newList = []
    for i in range(num, 0, -1):
        newList.append(i)
    return newList
print(countDown(5))

#Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
def printReturn(list):
    print(list[0])
    return(list[1])
print(printReturn([5,10]))

#First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
def firstPlusLength(list):
    sum = list[0] + len(list)
    return (sum)
print(firstPlusLength([1,2,3,4,5,6,7,8,9]))

#Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
def valuesGreaterThenSecond(list):
    list2=[]
    if  len(list)<2:
        return False
    for i in range(len(list)):
        if list[i]>list[1]:
            list2.append(list[i])
    return list2
print(valuesGreaterThenSecond([1,2,3,4,5,6,7,8,9]))
print(valuesGreaterThenSecond([1]))

#This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
def thisLengthThatValue(size, value):
    length = []
    for i in range(size):
        length.append(value)
    return list
print(thisLengthThatValue(2,4))


    
