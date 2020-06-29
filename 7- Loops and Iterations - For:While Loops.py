# Quick recap on loops

# We've got a list of numbers here
nums = [1, 2, 3, 4, 5]
# let's loop through this list:
for num in nums:
    print(num)
# returns: 1
#         2
#         3
#         4
#         5

# We are looping throuhg each value of our list,
# And each time through our list,
# the num variable will be equal to the next variable in the list

###################################################################

# Let's now look at two important key words when working with loops.
# These are the 'break' and 'continue' keywords

# a) break keyword will completely break out of a loop,
# b) where the continue keyword will move on to the next iteration of the loop

# Let's say we're looking for a certain number on our list and,
# once we find it we don't need to continue looping through the rest of our values.

# Say we're looking for the value of 3:

for num in nums:
    if num == 3:
        print('Found!')
        # break is inserted after 3 is found:
        break
    print(num)
# returns: 1
#         2
#         Found!

# We can see that the first two values didn't meet our conditionals but,
# on the third value, 3, the conditional was met, so printed 'Found!',
# and then the loop was broken from continuing further down the list by the break keyword.
# thereby not iterating through anymore values once for loop was broken out of.

# Notice that if the print(num) statement is put in before the if num == 3:

for num in nums:
    print(num)
    if num == 3:
        print('Found!')
        break
# returns: 1
#         2
#         3
#         Found!

###################################################################

# Now, what if we wanted to loop through the list,
# while ignoring some values,
# and not break out of the loop completely?

# We use the continue statement
# Continue will skip to the next iteration of the loop,

for num in nums:
    if num == 3:
        print('Found!')
        # continue is inserted after 3 is found:
        continue
    print(num)
#returns: 1
#         2
#         Found!
#         4
#         5

###################################################################

# Now, lets look at a loop within our loop:

# Within the loop we have:
for num in nums:
    # We're going to replace the if num == 3 conditional with an inner loop:
    for letter in 'abc':
        print(num, letter)
#returns: 1 a
#         1 b
#         1 c
#         2 a
#         2 b
#         2 c
#         3 a
#         3 b
#         3 c
#         4 a
#         4 b
#         4 c
#         5 a
#         5 b
#         5 c

# This means that for each number, it will loop through every character in the string,
# and print out the number and the character (which is function of the inner loop),
# then loop through the next number and do it all over again.

# You want to be careful with nested loops because these combinations can grow pretty quickly.
# i.e. if you have nested loops with a lot of different values,
# it may take a while to loop through all of those different combinations.

###################################################################

# A lot of times we want to go through a loop a certain number of times.
# There is a built in function called range() which will come in very handy.

# Say we want to run through a loop 10 times:
for i in range(10):
    print(i)
#returns: 0
#         1
#         2
#         3
#         4
#         5
#         6
#         7
#         8
#         9

# It just prints out 0 to 9 (which is 10 items)
# which starts at 0 and go upto, but not including the number we passed into the range (10)

# Now, if we don't want it to start at 0, and end at 10;
# We can also pass a starting value in the range,
# with 11 (since range doesn't include the last value):
for i in range(1, 11):
    print(i)

#returns: 1
#         2
#         3
#         4
#         5
#         6
#         7
#         8
#         9
#         10

###################################################################

# Let's take a look at while loops.

# Our for loops iterated through a certain number of values,
# But while loops will just keep going until a certain condition is met,
# Or until we hit a break:

x = 0

while x < 10:
    print(x)
    # refer to '***'
    x += 1

# *** We will have to remember that this loop will iterate FOREVER,
# *** (until x < 10 is no longer met)!
# *** Therefore we have to increment this x,
# *** so that at some point it will be greater than, or equal to, 10 and break out!

#returns: 0
#         1
#         2
#         3
#         4
#         5
#         6
#         7
#         8
#         9

# See that it prints out 0 through 9;
# it came in and saw that x = 0, which meets the loop condition x < 10,
# so it continues through the loop, increment by 1,
# and continues until x = 10, which no longer meets the x < 10 condition.

###################################################################

# Now at any point, you can just use a break to break out of the while loop,
# just like we did with the for loop:

x = 0

while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

#returns: 0
#         1
#         2
#         3
#         4

###################################################################

# Sometimes, we just want to create an infinite loop,
# that never ends until we get some input or find some values.

# To create an infinite loop:

x = 0

# we can just replace the comparison with the value of True:
while True:
    # Now that we have an infinite loop,
    # there is no conditional for which the loop could break out.
    if x == 5:
        # So we need the break statement if we ever want to stop this loop.
        break
    print(x)
    x += 1
#returns: 0
#         1
#         2
#         3
#         4

# This is how you would continue a loop indefinitely,
# until you find or receive values that you're looking for.

# If you ever get stuck in an infinite loop,
# you can press control + c to stop the process.
