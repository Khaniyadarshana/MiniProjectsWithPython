#Make a new list with the sum of digits of given numbers in a list

#Function to calculate sum
def digitSum(n):
    dsum = 0
    for items in str(n):
        dsum += int(items)
    return dsum

#Initialising list
List1 = [123, 456, 789, 245, 555]

#Using the function on all elements of list1
newList = [digitSum(i) for i in List1]

#Using the function on odd elements of the list
newList1 = [digitSum(i) for i in List1 if i & 1]

#Display new list
print(newList)
print(newList1)