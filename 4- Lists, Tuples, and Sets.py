# LISTs and TUPLEs allow us to work with sequential data,
# and SETs are unordered collections of values with no duplicates.

# # # # # # # # # # # # # #     # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # LISTS # # # # # # # # # # # # # #
# # # # # # # # # # # # # #     # # # # # # # # # # # # # # #

# Just as the name implies, lists allow us to work with a list of values:
# For example, if we want to create a list of courses,
# square brackets are used to create a list, with each value separated by a comma within these sq. brackets:
courses = ['History', 'Maths', 'Physics', 'CompSci']
print(courses)

###################################################################

# Now, if we want to see how many values are in our list:
print(len(courses))

###################################################################

# We can also access a given value in our list,
# by using square brackets [] after the list variable,
# and adding the index (location) of the given value:
print(courses[2])

# N.B. the first index [0] will return the first item on the list (History),
# the second index [1] will return the second item (Maths), etc.

###################################################################

# We can also use negative indexes too,
# negative indexes just start from the end of our list:
print(courses[-1])

# N.B. it's more convenient to be using the last item of the list via negative indexes,
# Because we don't have to worry about what the length of the list is.

# For example, if the list grew by 10 items, the 3rd index will no longer be the last item,
# Where as the -1 will always return the last item.

###################################################################

# To return a range of items in a given list
print(courses[0:2])

# Or, similarly:
print(courses[:2])

# N.B. This follows the same range function as with strings in the first tutorial.
# Once again, this method is called slicing, and there is more detail
# in the follow-up tutorial: https://youtu.be/ajrtAuDg3yw

###################################################################

# Now let's look at some list methods which will allow us to modify our list

# We use the .append() method to add an item to (the end of) our list:
courses.append('Art')
print(courses)

###################################################################

# We can use the .insert() method to add an item to the specific location in our list;
# insert() takes 2 arguments:
# first the index (i.e. location) where you want to insert the value
# and second the value (to be added) itself:
courses.insert(0, 'Health')
print(courses)

###################################################################

# We can use the .extend() method when we want to add multiple values to our list
# Say we have another list:
courses_2 = ['Biology', 'Chemistry']

# If we use the .insert() method to add the two items of the new list to the existing courses list:
courses.insert(0, courses_2)
print(courses)
# We see that this inserted the entire list structure of courses_2 to our courses list,
# Thereby returning a list, inside a list.

# This messes with the index of the list, since the new list, as it is enclosed in one structure,
# will become the 0 index, as below:
print(courses[0])

# To prevent this list-inside-a-list scenario,
# We use the .extend() method to add the new course as two individual items:
courses.extend(courses_2)
print(courses)
# Notice that now 'Biology' and 'Chemistry' are added to the end of the list!

###################################################################

# Let's now look at some methods that remove some items from our list

# Giving ourselves a new list:
fruits = ['Apple', 'Pear', 'Orange', 'Melon']

# We use the .remove() method to, say, remove Apple from our list:
fruits.remove('Apple')
print(fruits)

###################################################################

# We can also use the .pop() method to remove the last item ('Melon') of our list:
fruits.pop()
print(fruits)

# This is useful if we want to use our list like a stack or a q

# One other thing about pop() is that it returns the value that it removed:

# Say we have a new list, and pop it:
alphabets = ['a', 'b', 'c', 'd', 'e']
popped = alphabets.pop()

print(popped)
print(alphabets)

# If you have a stack or a q, you can just keep popping off values until the list is empty

###################################################################

# We use the .reverse() method to reverse the order of our list:
cars = ['Ferrari', 'Porsche', 'Lamborghini', 'Audi']

cars.reverse()
print(cars)


# We can also use the .sort() method to sort our list
veggies = ['Carrot', 'Potato', 'Cucumber', 'Onion']

veggies.sort()
print(veggies)
# If we sort a list of TEXTUAL items, the sort will order the items in alphabetical order

# If we sort a list of NUMERIC items, the sort will order the items in ascending order:
nums = [1, 4, 2, 3, 5]

nums.sort()
print(nums)

# Now, to customise the sort method
# (say, to sort using the reverse of the automatically defined order)
# (which would be the reverse of alphabetical order for string, and descending order for nums)

# We can introduce an argument to the sort METHOD.
clothes = ['Armani', 'Primark', 'Benetton', 'H&M']
clothes.sort(reverse=True)
print(clothes)

###################################################################

# What if we wanted to get a sorted version of our list, without altering the original list?

# We use the sorted FUNCTION.
sorted(clothes)
print(clothes)
# returns ['Primark', 'H&M', 'Benetton', 'Armani']

# As we can see, the list is not sorted; it is exactly the way it is above at line 153;
# this is because the sorted function doesnt sort the list in place;
# it returns a sorted version of the list.

# So to get that sorted list, we have to make a new variable,
# and set it to the return value of the sorted function:
sorted_clothes = sorted(clothes)
# sorted_clothes is equal to the sorted version of the clothes list (i.e. sorted(clothes))
print(sorted_clothes)
# returns ['Armani', 'Benetton', 'H&M', 'Primark'].

# This is very useful because a lot of the times you won't want to alter your original list in any way

###################################################################

# Besides the sorted() function, there are a couple more built-ins that we can use for these sequences

# 1st, We will look at min(), max(), sum() functions.

# Where:
nums = [1, 4, 2, 3, 5]

print(min(nums))
# returns the minimum value of the list: 1.
print(max(nums))
# returns the maximum value of the list: 5.
print(sum(nums))
# returns the sum total of the values of the list: 15.

###################################################################

# 2nd, if you want to find the index of a certain value within a list,

# (referring to the list of text items, [clothes] from above example ^^)
clothes = ['Armani', 'Primark', 'Benetton', 'H&M']

# We use the .index() method where the argument is reserved for value being looked up:
# For ease of comprehension, i've set the new variable as
primark_in_clothes = clothes.index('Primark')
print(primark_in_clothes)

# or
print(clothes.index('Primark'))
# returns: 1, meaning primark is the second item in the list 'clothes'

# N.B. if we search for an item that does not exist in the list, code returns 'ValueError'

###################################################################

# Now, if we just want to see if a value does or does not exist in a list,
# for a true/false result (i.e. a boolean),
# we use the in OPERATOR:

is_primark_in_clothes = 'Primark' in clothes
print(is_primark_in_clothes)

# or
print('Primark' in clothes)
# returns True, meaning primark is indeed an item in the clothes list

# N.B. This is going to be esp. useful when learning conditionals & if/then statements,
# which we will go over in a couple of courses.

###################################################################

# This is ALSO useful when we need to loop through values of our list,
# by using a for loop:

for item in clothes:
    print(item)

# returns Armani
#        Primark
#        Benetton
#        H&M

# This is the first time we have indented a code!
# Basically what we are saying here is, we want to create a loop;
# where we're looping through each value of our list,
# and each loop through,
# this item variable will equal to the next item in the list.

# This is why line 227 is indented;
# because it tells us that this code is executed within the for loop.
# FYI the item variable in line 226 is just a variable; it's not a key word or anything.
# Hence, if you put it under a different name to item, it will still return the same results.

###################################################################

# We can access each value as we're looping through,
# but sometimes it can be useful to also have the index of what value we're on.

# For a given list:
candies = ['M&Ms', 'Snickers', 'Sour Patch Kids', 'Twix', 'Kitkat']

# To access this in Python, we can access the value and the index,
# using the enumerate function (also note we want to print both value & its index):

for index, item in enumerate(candies):
    print(index, item)
# returns 0 M&Ms
#         1 Snickers
#         2 Sour Patch Kids
#         3 Twix
#         4 Kitkat

# If we don't want to start at 0, we can pass in a start value to our enumerate function:

for index, item in enumerate(candies, start=1):
    print(index, item)
# returns 1 M&Ms
#         2 Snickers
#         3 Sour Patch Kids
#         4 Twix
#         5 Kitkat

###################################################################

# One last thing to go over before moving onto tuples and sets.

# It is common that we want to turn our lists into strings, separated by a common value.
# to do this, we're going to use a string method called .join,
# and pass in our list as the argument.

candies_str = ', '.join(candies)
print(candies_str)
# returns: M&Ms, Snickers, Sour Patch Kids, Twix, Kitkat

# we see the ', ' separated each item of the list by a comma and a space;
# these can be modified according to need, e.g. using hyphen (-) instead of comma:

candies_strhyph = ' - '.join(candies)
print(candies_strhyph)
# returns: M&Ms - Snickers - Sour Patch Kids - Twix - Kitkat

###################################################################

# Now, to do the revese of this,
# i.e. turn a string into a list,
# we can use the .split method given a certain common value (e.g. a (,) or (-) as above):

new_list = candies_str.split(', ')
print(new_list)
# returns our original list prior to joining:
# ['M&Ms', 'Snickers', 'Sour Patch Kids', 'Twix', 'Kitkat']

# # # # # # # # # # # # # #       # # # # # # # # # # # # # # #
# # # # # # # # # # # # # #  TUPLES # # # # # # # # # # # # # #
# # # # # # # # # # # # # #       # # # # # # # # # # # # # # #

# Tuples are very similar to lists apart from one thing:
# Tuples cannot modify.
# i.e. they are immutable.

# To illustrate, here we have a mutable list;
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
#returns: ['History', 'Math', 'Physics', 'CompSci']

print(list_2)
#returns: ['History', 'Math', 'Physics', 'CompSci']

# If we replace the zeroth index of list_1 to 'Art',
list_1[0] = 'Art'

print(list_1)
#returns: ['Art', 'Math', 'Physics', 'CompSci']

print(list_2)
#returns: ['Art', 'Math', 'Physics', 'CompSci']

# both list_1 and list_2 reflect the change when printed

# i.e. if you need to modify your list, this mutability is what you want.

# if you have a list of values that you know you don't want to change, use a tuple.
# Tuples look exactly like a list, except that it is otherwise enclosed by parentheses(),
# instead of the sq. brackets of the list []:
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# Now, although we are performing the exact same thing as we did with the above list example,
# Tuple will not allow us to perform the above command because it is immutable!
#tuple_1[0] = 'Art'
# returns TypeError: 'tuple' object does not support item assignment

# A tuple does not support item assignment because it is immutable.
# Since a tuple is immutable it does not have nearly as many methods as a list,
# because a lot of the methods we looked at involved mutating the values.
# we can't .append or .remove, for example.

# Other than that, they behave pretty much the same;
# we can loop through tuples, access values, etc.
# except for what mutates the list.

# # # # # # # # # # # # # #     # # # # # # # # # # # # # #
# # # # # # # # # # # # # # SETS # # # # # # # # # # # # # #
# # # # # # # # # # # # # #     # # # # # # # # # # # # # #

# Set are values that are unordered and also have no duplicates.

# Sets are expressed by curly brackets, as below:
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}

print(cs_courses)
# returns {'Physics', 'CompSci', 'Math', 'History'}

# Notice how the values are returned in no particular order;
# when the command is performed for multiple times, the returned order will always be different.

# This is because sets {}, unlike lists [] or tuples (), don't really care about order.
# In fact, some of the main uses of a set is to test whether a value is a part of a set,
# or to remove duplicate vales;
# since sets throw away duplicates!

# for instance, if we create a set with duplicate values:
food = {'pizza', 'pizza', 'spaghetti', 'milanese', 'pizza'}
print(food)
# returns {'spaghetti', 'milanese', 'pizza'};
# i.e. returns 'pizza' only once despite 3 duplicates!

###################################################################

# 'Membership test' refers to the testing whether a value is a part of a set

# if we check using the in operator as we learned before:

print('pizza' in food)
# returns True
# Sets do this a lot more efficiently than lists or tuples.
# we can run the above command with lists and tuples but sets are optimised for this.

###################################################################

# Lastly, one other thing sets are optimised to do,
# is to determine what value(s) a set shares with other set(s)

# To illustrate, we have two different sets here with some shared values
mgmt_consulting = {'mckinsey', 'm&a', 'powerpoint', 'duedilligence'}
i_banking = {'fp&a', 'duedilligence', 'goldmansachs', 'm&a', 'clout'}

# To see what the shared values are,
# We use the .intersection() method:
print(mgmt_consulting.intersection(i_banking))
# returns {'duedilligence', 'm&a'}

###################################################################

# To see what the unshared values are, i.e. what the difference is,
# We use the .difference() method:
print(mgmt_consulting.difference(i_banking))
# returns {'powerpoint', 'mckinsey'}

###################################################################

# To combine the two sets and see both sets' values,
# We use the .union() method:
print(mgmt_consulting.union(i_banking))
# returns {'powerpoint', 'clout', 'mckinsey', 'fp&a', 'duedilligence', 'm&a', 'goldmansachs'}

###################################################################
###################################################################
###################################################################

# Finally, to create empty lists, tuples, and sets,
# WARNING: A SMALL GOTCHA!

# Empty Lists
# To create an empty list, we can either type:
empty_list = []
# or
empty_list = list()

# Empty Tuples
# Similarly, to create an empty tuple, we can either type:
empty_tuple = ()
# or
empty_tuple = tuple()

# HOWEVER;

# Empty Sets
# To create an empty set, we CAN'T type:
empty_set = {}
# because THIS ^ will create an empty DICTIONARY.

# So, to create an empty set, we can only use:
empty_set = set()
