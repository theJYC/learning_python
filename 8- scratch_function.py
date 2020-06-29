def hello_func(str=True, var=1):
    if str == True and var == 1:
        print('Function meets both our parameters')
    elif str == True or var == 1:
        print('Function meets our string parameter')
    else:
        print('Function is not String')


hello_func(str=False, var=0)
hello_func(str=True, var=2)


def hello_func(greeting):
    return f'{greeting}, Function.'


print(hello_func('Hi'))


def hello_func(greeting, name):
    return f'{greeting}, {name}'


print(hello_func('Hi', 'Jonathan'))

# Now, if we want to set a default parameter
# i.e. if the parameter is not defined when running the function,
# the default parameter will be returned instead:


def hello_func_d(greeting, name='Customer'):
    return f'{greeting}, {name}'


# greeting is defined ('Hello'), but name is left empty (i.e. undefined)
print(hello_func_d('Hello'))  # so default variable 'Customer' will be assumed.
# returns: Hello, Customer

# greeting is defined and name is also defined 'Chad'
# function will run according to the defined parameters
print(hello_func_d('Hello', 'Chad'))
# returns: Hello, Jason

# print(hello_func())  # neither greeting nor name parameters is entered
# returns TypeError: hello_func() missing 2 required positional arguments: 'greeting' and 'name'!

# ^ this is because the function REQUIRES two (positional) parameters to be inputted
