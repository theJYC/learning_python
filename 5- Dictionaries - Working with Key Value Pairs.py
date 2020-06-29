# Dictionaries allow us to work with key-value pairs.
# These key-value pairs may also be called as hashmaps or associative arrays

# These key-value pairs are two linked values where the key is a unique identifier to look up data,
# where the value is the data

# In this sense the dictionary is like a real physical dictionary, where we look up word defn.
# Each word we look up is the key, and the definition is the value

# Let's say we want to represent a student using a dictionary
student = {'name': 'John', 'age': 25, 'courses': ['Maths', 'CompSci']}
# 'name' is key, separated by comma for the value 'John', etc. etc.

print(student)
# returns: {'name': 'John', 'age': 25, 'courses': ['Maths', 'CompSci']}

# Now, let's just the get a value of one particular key, 'name':
print(student['name'])
# returns: John

# or the value of the 'age' key; i.e. how old is John?
print(student['age'])

# We can see that these VALUES of the dictionary can be just about anything.
# Now, all of our KEYS in the above dictionary are all strings.
# But they can be any immutable data types.

# For example, if we have the below dictionary with the key '1',
EmoryStudent = {1: 'Swoop', 'age': 25, 'courses': ['Maths', 'CompSci']}

print(EmoryStudent[1])
#returns: Swoop

###################################################################

# If we try to access a key that doesn't exist, i.e. 'phone':
# print(EmoryStudent['phone'])
# returns: KeyError: 'phone'

###################################################################

# Sometimes throwing an error for a key that doesn't exist,
# might not be what we want.

# Sometimes we may just want to return a None or a default value.
# To do this, we can use the dictionary's .get() method

print(EmoryStudent.get('age'))
#returns: 25

# When we use the .get() method for a non-existent key, say 'phonenumber':
print(EmoryStudent.get('phone'))
#returns: None

# Now, instead of None, if we were to want a default value to return,
# We pass the default value we want as a second argument of the .get() method,
# whereby the default value = 'Not Found':
print(EmoryStudent.get('phone', 'Not Found'))
# returns: Not Found

###################################################################

# Now, if we want to add a new entry to the dictionary,
# Say we want to add the 'phone' key & its corresponding value to our dictionary:
EmoryStudent['phone'] = '+(404)862-8679'
print(EmoryStudent['phone'])
# returns: +(404)862-8679

# If we execute the above command for a key that already exists, the OG content will be updated.
# For instance, knowing we already have the value '25' assigned to the 'age' key in our dict;
EmoryStudent['age'] = 48
print(EmoryStudent['age'])
#returns: 48

# ^As we can see, the 'age' key has been updated from '25' to '48'

###################################################################

# We can also update values using the .update() method,
# which is esp. useful when we want to update multiple values at a time.

# Going back to our first dictionary for reference, where:
student = {'name': 'John', 'age': 25, 'courses': ['Maths', 'CompSci']}

# We use the .update() method, using the dictionary as an argument,
# To update our 'name', 'age' keys, and add a new key 'phone':
student.update({'name': 'Jane', 'age': 34, 'phone': '+1 404 862 8679'})
print(student)
# returns:
#{'name': 'John', 'age': 26, 'courses': ['Maths', 'CompSci'], 'phone': '+1 404 862 8679'}

###################################################################

# Now, let's say we want to delete a specific key and its value:
# We can use the del key word:
del student['age']
print(student)
#returns: {'name': 'Jane', 'courses': ['Maths', 'CompSci'], 'phone': '+1 404 862 8679'}

###################################################################

# Another way we can do this is to use the .pop() method like we use in lists:
# the .pop() method will remove but also return that value.
# allowing us to grab the removed value with a variable:

# for our updated dict below:
updt_student = {'name': 'Jane', 'courses': [
    'Maths', 'CompSci'], 'phone': '+1 404 862 8679'}

name = updt_student.pop('name')

print(updt_student)
#returns: {'courses': ['Maths', 'CompSci'], 'phone': '+1 404 862 8679'}
print(name)
#returns: Jane

###################################################################

# Now let's look at how we can loop through all the keys and values of our dictionary.

# For our student dictionary:
student = {'name': 'Jane', 'courses': [
    'Maths', 'CompSci'], 'phone': '+1 404 862 8679'}
# First, we use the len() function if we want to see how many keys we have in our dict:
print(len(student))
# returns 3

# If we want to see all of these KEYS of our dictionary,
# Use the .keys() method:
print(student.keys())
#returns: dict_keys(['name', 'courses', 'phone'])

# If we want to see all of the VALUES of our dict,
# Use the .values() method:
print(student.values())
#returns: dict_values(['Jane', ['Maths', 'CompSci'], '+1 404 862 8679'])

# If we want to see BOTH our KEYS and VALUES of our dict.,
# We use the .items() method:
print(student.items())
#returns: dict_items([('name', 'Jane'), ('courses', ['Maths', 'CompSci']), ('phone', '+1 404 862 8679')])

# ^We can see the key + values pairs of the dict., in brackets. e.g. ('name', 'Jane')

###################################################################

# So, if we wanted to loop through our keys and values
# We might be tempted to loop through our dictionary as we would our list,
# BUT, if we do this, it will just loop through the keys:

for key in student:
    print(key)
#returns: name
#         courses
#         phone

# In order to loop through our keys AND values, we nedd to use the .items() method,
# Now these come in a pair of two values,
# So instead of just key, we're also going to have to access the value:

for key, value in student.items():
    print(key, value)
# returns: name Jane
#         courses ['Maths', 'CompSci']
#         phone +1 404 862 8679
