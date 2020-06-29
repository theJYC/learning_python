# Arithmetic Operators:

# Addition
print(3 + 2)

# Subtraction
print(3 - 2)

# Multiplication
print(3 * 2)

# Division
print(3 / 2)
#returns: 1.5

# Floor Division (drops the decimal)
print(3 // 2)
#returns: 1
# Exponent (x to the power of y)
print(3 ** 2)
# returns: 9

# Modulus (to get the remainder after a division)
print(3 % 2)
#returns: 1

# ^: 2 goes into 3 once, with 1 leftover
# Common use case for the modulus operator is to tell if number is even or odd
# (Everytime you divide a number by 2 you're getting two remainders: 0 or 1)
# i.e. If you do a % 2 on any number, the number would be even if the remainder is 0,
# and odd if the remainder is 1.

###################################################################

# Difference between integer and float
# integer: whole number; float: decimal

num = 3
print(type(num))
# returns: <class 'int'>

num1 = 3.14
print(type(num1))
# returns: <class 'float'>

###################################################################

# Another common operation is 'INCREMENTING A VARIABLE'

# if
num = 1

# There are two ways to increment the value (num) by 1:

# a)
num = num + 1
print(num)

# Incrementing values is such a common operation that there is a SHORTHAND for this:

# b)
num += 1
print(num)

# You can apply this shorthand for other artithmatic operators:

num *= 10
print(num)
# This is the result of num (which was previously incremented by 1 twice (hence + 1 + 1 )),
# incremented by (* 10)

###################################################################

# We also have some built-in functions that are available to us

# One of these functions is abs()
# Which will just remove the sign from any negative number

print(abs(-3))

# Another function is round()
# Which will round the number to its integer value

print(round(3.75))

# We can also add a second argument to indicate up to how many digits we want to round to
# In this example we round to the first digit after the decimal

print(round(3.75, 1))

###################################################################

# Another thing we want to do with numbers is to use Comparison OPERATORS

# These comparisons are going to return booleans;
# booleans are true/false values

# Using the two variables--
num_1 = 3
num_2 = 2

# Comparison OPERATORS:

# Equal (x equals y)
print(num_1 == num_2)

# Not Equal (x does not equal y)
print(num_1 != num_2)

# Greater Than (x is greater than y)
print(num_1 > num_2)

# Less Than (x is less than y)
print(num_1 < num_2)

# Greater or Equal (x is greater than or equal to y)
print(num_1 >= num_2)

# Less or Equal (x is less than or equal to y)
print(num_1 <= num_2)

###################################################################

# Now, sometimes we run into strings which look like numbers (or vice versa)

num_a = '100'
num_b = '200'

# Given that the variables are enclosed within the quotes, these are classified as strings (text)
# So when num_a and num_b are added, the two strings are concatenated instead of added:
print(num_a + num_b)

# In order to turn these into integers, we have 'cast' these values.
# Casting is super easy; all that it takes is to wrap the variable into int() function:
num_a = int(num_a)
num_b = int(num_b)

print(num_a + num_b)
