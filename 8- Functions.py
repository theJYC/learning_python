# Functions are instuctions packaged together that perform a specific task.

# Let's create our first function and see why these are so beneficial.
# We use the def keyword (which stands for definition),
# and let's make a simple function to get started, calling it hello_func.:
def hello_func():
    # see '***'
    pass

    # We have parentheses here,
    # because that is where our parameters will go when they're added in.

    # But we don't have any parameters just yet, so that will be empty for now.

    # '***' Now it is possible to write a function and not have any code in it,
    # but we can't have it completely blank.

    # '***' If we want to fill this function in later, we can use this pass keyword.
    # pass is saying that we don't want to do anything for now,
    # but it won't throw any errors for leaving it blank.


hello_func()
# We need to ^add the parentheses after the function in order to execute it;
# if we dont have the parentheses there, it will be equal to the function itself.

# Let's actually see what that looks like,
# Printing out hello_func without the parentheses in place:
print(hello_func)
# returns: <function hello_func at 0x7f90e6afe550>

# This shows that this is a function in a certain location in memory.
# But it didn't execute the function.

# To execute, we add the parentheses:
print(hello_func())
# returns: None

# None is given because we're not doing anything with the function yet,
# and it doesn't have a return value.


# Let's go ahead and put some code into the function:

def hello_func():
    print('Hello Function!')

# Now that we're actually running that print statement from within the function,
# we don't need to print out to execute the function.


# If we just execute the function, it should run that print statement
hello_func()
# returns: Hello Function!

###################################################################
print('###################################################################')

# One benefit of functions is that they allow us to reuse code without repeating ourselves.

# Say we had to print out text in several locations within our program.


def hello_func():
    print('Hello Function!')


print('Hello Function!')
print('Hello Function!')
print('Hello Function!')
print('Hello Function!')
# returns: Hello Function!
#          Hello Function!
#          Hello Function!
#          Hello Function!

# Imagine our boss came to us and told us that the text was a little bit off,
# and we didn't want to have an exclamation point at the end of the string.

# The way we have it now, we'd have to come in and change all of those manually:
print('Hello Function.')
print('Hello Function.')
print('Hello Function.')
print('Hello Function.')

# Now, that was just manually changing exclamation mark to a period in just four locations,
# But imagine if we had to make that change in hundreds of locations in multiple diff. files.

# That's the first benefit of functions.
# it allows us to put code with a specific purpose into a single location.

# So, instead of printing those four statements, what we can do:
# is to run our function four times.


def hello_func():
    print('Hello Function!')


hello_func()
hello_func()
hello_func()
hello_func()

# If we were to remove that exclamation mark,
# (and it doesn't matter if this applies to a hundred different lines/locations),
# We can just update it in one spot:


def hello_func():
    # right here! replace the exclamation mark with a period:
    print('Hello Function.')


hello_func()
hello_func()
hello_func()
hello_func()
# returns: Hello Function.
#          Hello Function.
#          Hello Function.
#          Hello Function.

# THIS IS CALLED KEEPING YOUR CODE 'DRY'.
# Which stands for Don't Repeat Yourself.
# This is a common mistake for people new to programming,
# to repeat the same things throughout their code,
# when they could either put their code into certain variables or functions,
# so that it is in a single location.

###################################################################

# So we saw earlier that since we aren't returning anything from our function,
# it was actually equal to None:

# for example:


def hi_func():
    pass


print(hi_func())
# returns: None

# So what does it mean for our function to return something?
# Now this is where functions become really powerful:

# because it allows us to operate on some data,
# and then pass the result to whatever caught our function.

# So instead of print('Hello Function'),
# Let's actually return this.


def hello_func():
    return 'Hello Function.'

# This means that when we execute our function,
# it's actually going to be equal to our return value.


# So when we run these:
hello_func()
hello_func()
# doesn't return anything

# these executed functions here are actually equal to the string 'Hello Function'.
# i.e. they don't give us any result,
# because they're just strings that we're not doing anything with.

# BUT, instead, if we print this executed function:
print(hello_func())
# returns: Hello Function.

# We can see that it prints out our string.

# Basically, think of the function as a machine that takes input and produces result.

# When you execute a function, you can think of it almost as a black box.
# You don't need to know exactly how it's doing what it's doing,
# You're mainly concerned about the input and the return value.

# In this simple example below, we don't have any input,
# and we can see the return value is a string:


def hello_func():
    return 'Hello Function.'


print(hello_func())
# returns: Hello Function.

# Now, it's useful to know what the function is doing,
# but when just getting started,
# don't get caught up on understanding every detail of what every function does.
# Just focus on the input and what's returned.

# For example, when we called the len() function in the string:
print(len('Test'))
# returns: 4

# This just returns the number of characters that the string consists of;
# We have NO idea what the code that produces the result looks like,
# But we do know we passed in a string, and it returned this integer.

# i.e. We'll see in a bit why looking at functions in this way
# will help you become better when working with Python,.
# Because _we can treat the return value just like the data type that it is_,

# And understanding this will allow you to chain together some functionality.
# So we know hello_func returns a string,
# _so we can treat that executed function just like a string_.

# If we remember the string .methods,
# we can upper case the string by using the .upper()
print(hello_func().upper())
# returns: HELLO FUNCTION.

# To reverse the .upper method to how it was before:
print(hello_func().format())
# returns: Hello Function.

###################################################################

# Let's look at how we can pass arguments to our function.

# We need to create some parameters within our parentheses:

# If we want to customize the greeting that our function returns,

# 1) create a parameter called greeting
# 2) now, within our function, return a string where we use that greeting,
# instead of our 'Hello Function' text we had before.


def hello_func(greeting):
    return '{} Function.'.format(greeting)


# Now before we run this, we have to pass in that greeting argument when we execute the function.
print(hello_func('Hi'))
# returns: Hi Function.

# We can see that when we passed in that string 'Hi' into our function,
# it set that greeting variable equal to the string 'Hi',
# then returned the string 'Hi Function.'

# Now this greeting variable doesn't affect any variables anything outside the function,
# i.e. its scope is only local to the function
# which is nice,
# because we don't have to worry about it affecting anything we don't want to affect.

# Right now this greeting parameter is a required parameter,
# because it doesn't have a default value.
# Now, if we had a default value, then it would just fall back to the default falue,
# whenever we didn't pass that argument in.

# For example, let's say that we also want to be able to pass a name to the Hello function,
# and it will return both the greeting and the name.

# We can add that to the parameters by putting in a comma,
# and that we also want to accept the name parameter,
# we also want to say that if no name is passed in,
# we want to have a _default_ value of 'You'.


def hello_func(greeting, name='You'):
    return '{}, {}'.format(greeting, name)


print(hello_func('Hi'))
# returns: Hi, You

# What this does, is it returns a greeting and name, separated by comma and a space.
# Even though we didn't pass in a value for the name argument when we executed this function,
# it didn't throw an error and,
# instead, use the default value you threw in as 'You'.

# But if we want to pass in a value, it will use that value instead:


def hello_func(greeting, name='You'):
    return '{}, {}'.format(greeting, name)


print(hello_func('Hi', name='Corey'))
# returns: Hi, Corey

# or
# notice here that name='Corey' and 'Corey' are the same
print(hello_func('Hey there', 'Corey'))
# returns: Hey there, Corey

print('your required positional argument has to come before your keyword argument.')

# If you try to create function with those out of order, it's going to give you an Error.

###################################################################

# Sometimes you may run into a code like this in Python:


def any_function(*args, **kwargs):
    # *args and **kwargs parameters
    # that basically allow us accept an arbitrary no. of positional and keyword arguments.
    print(args)
    print(kwargs)

# arbitrary number is good because we might not know-
# -how many positional or keyword argument there will be in a given function's argument.


'''
reminder--
keyword argument: argument _preceded by an identifier_ (i.e. name='John')
positional argument: anything that isn't a keyword argument.
*arg can be typed out as *anything; **kwarg can be typed out as **whatever,
but we print them out this way because this is the convention!
'''
any_function('Math', 'Art', name='John',
             age=22)  # notice positional args come BEFORE kw args
# returns: ('Math', 'Art')              <-- positional arguments of the ^function
#          {'name': 'John', 'age': 22}  <-- keyword arguments of the ^function


def top_rappers(*args, **kwargs):
    print(args)
    print(kwargs)


'''
the 'arbitrary number' of positional and key word arguments is very useful,
when we are dealing with the below scenario:
'''

fem_rappers = ['Nicki Minaj', 'Cardi B', 'Lauren Hill']
# this is a list of positional arguments
male_rappers = {'name': 'Eminem', 'name': 'Dr.Dre', 'name': 'Snoop Dogg'}
# this is a dictionary(*) of keyword arguments
# (*): reminder that a dict. is a list of key-value pairs

# when we put the * and ** before the positional and keyword argument parameters below:
top_rappers(*fem_rappers, **male_rappers)
'''returns:

('Nicki Minaj', 'Cardi B', 'Lauren Hill')
{'name': 'Snoop Dogg'}    						'''

# notice that the * and ** allowed us to work with more than one pos/kw arguments!

# Last applied exercise (ignore the specifics of calculating for a leap year)
print('*********')

# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year=True):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year.""" # <-- doc string, used to explain what a-
    													    # -function or class does """docstring"""
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


print(is_leap(2020))
#returns: True
print(days_in_month(2019, 2))
#returns: 28
