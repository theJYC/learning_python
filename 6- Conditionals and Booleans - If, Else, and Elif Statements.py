# How we can control what statements get executed depending on whether certain values valuate to true or false;
# these true/false values are called booleans.

if True:
    print('Conditional was True')
# returns: Conditional was True

# This print statement will only be executed if the condition after the if statement
# values to be true

if False:
    print('Conditional was True')
# doesn't return anything since the condition after the if statement values to be true

# Conditionals are usually not hard coded to true/false values like the above.

# if we have a language variable,
language = 'Python'

# and if we run the if statement with the == (test for equality):
if language == 'Python':
    print('Conditional was True')
# returns: Conditional was True

###############################

# N.B. when the variable is predefined, e.g.:

variable = 'hi'
# the if conditional can just be expressed as [if variable:] (instead of [if variable == x:]),

# Note that a) and b) are the essentially the same codes,
# although expressed differently:

# a)
if variable == 'hi':
    print('hi')
#returns: hi

# b)
if variable:
    print('hi')
#returns: hi

##############################

# a quick refresher on the numerical comparisons operators:

# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=

# Object Identity:  is
# to check if the values have the same ID, or if the values are the same object in memory

##############################

# What if we wanted to run one portion of our code if language equals to Python,
# and run another portion of our code if it doesn't equal to Python?

# We're going to use an else statement.
language = 'Python'

if language == 'Python':
    print('Language is Python')
# We run the else statement
# (making sure that it is NOT indented since it is not a part of the if statement)
else:
    print('No Match')
#returns: Language is Python

# Language is Python is returned,
# and the code of our else block is not executed since the conditional is met.

language = 'Java'

if language == 'Python':
    print('Language is Python')
else:
    print('No Match')
# returns: No Match

###################################################################

# What if we wanted to check for multiple languages,
# and execute different code for each one we encounter?

# i.e. first check for if variable == x,
# if not, then if variable == y,
# if not, then 'no match'

language = 'Java'

if language == 'Python':
    print('Language is Python')
# We use the elif statement:
elif language == 'Java':
    print('Language is Java')
else:
    print('No Match')
#returns: Language is Java

# N.B. Compared to other languages, which have the switchcase operator,
# Python does not have that because the elif statement is plenty clean enough.
# If we wanted to add more elif conditionals, we can do so by simply adding more below:

language = 'Java'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
# 2nd elif
elif language == 'SQL':
    print('Language is SQL')
# 3rd elif
elif language == 'JavaScript':
    print('Language is JavaScript')
else:
    print('No Match')
#returns: Language is Java

###################################################################

# In addition to the above comparison operators,
# we also have some boolean operators/keywords:

# and
# or
# not

# Say we have two variables:
user = 'Admin'
logged_in = True

# Now, say we only wanted to execute code only if user = Admin AND logged_in = True,
# To do this, we use the 'and' keyword:
if user == 'Admin' and logged_in == True:
    print('Admin Page')
else:
    print('Bad Creds')
# returns: Admin Page

# Admin Page statement is printed since both the conditions are true;
# But if one of the condition weren't true:
user = 'Admin'
# This time logged_in is False
logged_in = False

if user == 'Admin' and logged_in == True:
    print('Admin Page')
else:
    print('Bad Creds')
# returns: Bad Creds

###################################################################

# the 'and' keyword means that BOTH the conditionals have to be true.
# If we just need one conditional to be true,
# we use the 'or' keyword:

user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in == False:
    print('Admin Page')
else:
    print('Bad Creds')
# returns: Admin Page

###################################################################

# the 'not' operation is just used to switch a boolean
# i.e. swtich a True to a False, or a False to a True.

if not logged_in:
    print('Please Log In')
else:
    print('Welcome')
# returns: Please Log In

# explanation: We can see that currently our logged_in variable is equal to False.
# when we say not logged_in, it will evaluate to True.
# i.e. saying Not False, which would evaulate to True.

# So if logged_in were defined as True:

user = 'Admin'
logged_in = True

if not logged_in:
    print('Please Log In')
else:
    print('Welcome')
#returns: Welcome

###################################################################

# Now, two objects can actually be equal,
# and not be the same object in memory.

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
#returns: True

# But if we use the is (object identity) operator:

print(a is b)
#returns: False

# The reason is because these are two different objects IN MEMORY.
# We can print out the different locations of each a and b,
# with the built in id() function:

print(id(a))
#returns: 140275371019200
print(id(b))
#returns: 140275371034048

# So, behind the scenes, print(a is b) is the same thing as print(id(a) is id(b));
print(id(a) == id(b))

###################################################################

# All the conditionals we looked at depend on what Python evaulates as True or False.
# Essentially, its easy to say, that,
# All things Python evaluates as False, is False,
# And the opposite is True.

# Here's a list of things Python evaluates as False:

# False Values:
# a) False
# b) None
# c) Zero of any numeric type
# d) Any empty sequence. e.g. '',(),[].
# e) Any empty mapping. e.g. {}.

# To illustrate:

##############################

# a)
condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
# returns: Evaluated to False

##############################

# b)
condition = None

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
# returns: Evaluated to False

##############################

# c)
condition = 0

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
# returns: Evaluated to False

# N.B. since c) shows 0 is evaluated as False,
# this means that any other number will be evaluated as True:

condition = 10

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
# returns: Evaluated to True

# N.B.2. this is something to be mindful of when working with numbers,
# since we don't want to accidently pass in a 0,
# that you think would be True, but evaluates to be False

##############################

# d)
condition = []

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
# returns: Evaluated to False

##############################

# e)
condition = {}

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
# returns: Evaluated to False

###################################################################

# So, now that we know what evaluates to False,
# we can conclude that the opposite of each of these a) b) c) would be evaluated as True!
