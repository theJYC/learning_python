# Methods and Functions are different when executing:
# method requires the .method() format ; such as abc.method()
# function requires the function() format ; such as function(abc)

# Variables can be used in lieu of string
# The variable used is 'message'

message = "Hello World"

print('Hello World')

print(message)

###################################################################

# Exercise to demonstrate the distinction between single quote and double quote
# When you use the single quote (') as an apostrophe in a given string (i.e. 'Bobby's World');
# Python will not be able to recognise the closing of the string,
# given the two single quotes that follow the initial single quote.
# IN THIS CASE, USE DOUBLE QUOTES TO PREVENT AMBIGUITY:

message2 = ("Bobby's World")

print(message2)

# If we need to use a multiline string,
# we can use three quotes ('''bob''' OR """bob""") in the beginning and end of our string
# can be either single or double quote

message3 = '''Bobby's World
Consists of Ice Creams'''
print(message3)
# returns:
# Bobby's World
# Consists of Ice Creams

# To determine how many characters are in a given string, we use the len() function (length)

print(len(message))
print(len(message2))
print(len(message3))

###################################################################

# To access the string's characters individually, we use sq. brackets [],
# and use index to indicate the location of the character.

# For message 1, which was 'Hello World', index 1 is e. (N.B. first character starts with 0)
# Index = (nth character - 1);
print(message[1])

# highest index of a given string = (total no. of characters - 1).

print(message[10])

# To get a range of characters, use [x:y], whereby:
# To print out all the characters between index(x) upto, BUT NOT INCLUDING, index(y)

print(message[0:11])

# Given that the above range begins at 0, we could omit the starting index,
# And it will be automatically assumed as such:

print(message[:11])

# Now, same applies for the ending index; if we omit the second index in the range,
# it will be assumed that the range ends at the ending character of the string:

print(message[6:])

# ^what we are doing above is called 'slicing' and there is a follow-up video for it.

###################################################################

# All of the data that we use are going to have various method types available, which will allow a lot of useful functionalities
# Functions and Methods are essentially the same thing;
# a method is just a function that belongs to an object

# A method we can use, for instance, is to make all characters lowercase in a given string;
# using .lower()

print(message.lower())

# Conversely we could use .upper()

print(message.upper())

###################################################################

# We could also use the .count() function,
# to count how many times a given character(s) appear(s) in a string:

print(message.count('Hello'))

# This showcases that 'Hello' appears once in the string 'Hello World'

print(message.count('l'))

# This showcases that the letter 'l' appears three times in the string 'Hello World'

###################################################################

# We can also use the .find() function to see where a given character appears in a string:

print(message.find('World'))

# 'World appears at the sixth index of the string 'Hello World'

# N.B. if you try to find a non-existent character(s) in the string, it will yield -1.

print(message.find('Universe'))

###################################################################

# We can also use the .replace() function to swap out given character(s) for new character(s),
# following the format: .replace('old character(s)','new character(s)')
print(message.replace('World', 'Universe'))

###################################################################

# Now we'll look at how we can add multiple strings and concatenate together:

greeting = 'Hello'
name = 'Michael'

new_message = greeting + name
print(new_message)
# returns: Hello Michael

# Realise that the new_message, when spelled out, is missing some punctuations. correct by adding them

new_message = greeting + ', ' + name
print(new_message)
# returns: Hello, Michael

###################################################################

# Sometimes using the + sign is not the easiest, esp. when the string gets long.

new_message = greeting + ', ' + name + '. Welcome!'
print(new_message)
# returns: Hello, Michael. Welcome!

# Instead, we can use a formatted string, which will write the sentence as it will appear,
# and put placeholder(s) in place of our variable(s).
# Accordingly, the first {} occupies the first spot (where (greeting) is) in the format parenthesis,
# and the second {} the second spot (where (name) is):

new_message = '{}, {}. Welcome!'. format(greeting, name)
print(new_message)
# returns: Hello, Michael. Welcome!
# For more detail on string formatting there is a follow-up video.

###################################################################

# To make string formatting as simple as possible, use f strings:

new_message = f'{greeting}, {name}. Welcome!'
print(new_message)
# returns: Hello, Michael. Welcome!

# What makes f strings neat is that you can actually write code within the placeholder,
# as such:
new_message = f'{greeting}, {name.upper()}. Welcome!'
print(new_message)
# returns: Hello, MICHAEL. Welcome!

###################################################################

# Now, for bonus functions to use:

# The dir() function shows all the attributes of a given string; i.e. how the string is composed:

print(dir(name))

###################################################################

# The help() function shows all the info. regarding all the available string methods:

print(help(str))

# You can also look up the specfic string function via help() function,
# As such:

print(help(str.lower))
# returns: lower(self, /)
#             Return a copy of the string converted to lowercase.
