# ### Write a program that can map() to make a list whose elements are squares of numbers between 1 and 20 (both included). 
# Hints: Use map() to generate a list.<br> Use Lambda to define anonymous functions

# ## With map() function
#defining the function
def square(x):
    return x**2
#list of numbers whose squres is to be calculated
numbers = range(1,21)

#using map() function to generate squares
num_squares = map(square, numbers)

#printing the result of map function
print(list(num_squares))


# ## With lambda function
#defining the lambda function
f = lambda x: x**2

#applying on numbers
squares=[f(x) for x in range(1,21)]
print(squares)
