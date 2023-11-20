# List Comprehension
myList=[1,2,3,4,5,6]
print(myList)
updatedList=[2*item for item in myList]
print(updatedList)

# List comprehension with Filters
myList2=list(range(20))
filteredList=[item for item in myList2 if item % 2==0]
print(filteredList)

# List Comprehension with Functions
myList3="I am new to Python Course!! Wish me Good Luck."
print(myList3)
updatedList3 = myList3.split("!")
print(updatedList3)
