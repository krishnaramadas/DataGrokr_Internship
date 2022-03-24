# ### With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.
# Hint: Use set() to store a number of values without duplicates

# initializing list
test_list = [12,24,35,24,88,120,155,88,120,155]
print("The original list is :" + str(test_list))

#Initializing an emty list and a empty set
unique_list=[]
unique_elements = set()

#for loop
for i in test_list:
    if i not in unique_elements:
        unique_elements.add(i)
        unique_list.append(i)
        
# printing list after removal and preserved ordering
print ("The list after removing duplicates : " + str(unique_list))
