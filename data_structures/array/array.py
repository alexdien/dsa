# list is used to store an ordered collection of items. lists are mutable.
# can contain integers, floats, strings or even other lists.

# create a list of mixed data types
list_of_mixed = [1, 'joe', '3.14', [5,7]]
print(list_of_mixed)

# create a list of integers
list_of_integers = [1, 3, 5, 7, 9 , 11]
print(list_of_integers)

# create list of strings
list_of_strings = ['this', 'is', 'my', 'list']
print(list_of_strings)

# using list() constructor
list_constructor = list()
list_constructor.append(0)
list_constructor.append(50)
list_constructor.append('name')
print(list_constructor)
print(list_constructor[2])

# create a list with repeated elements
repeated_integer = [3] * 5
print(repeated_integer)

# access list elements
access_elements = [0, 1, 3, 4, 6]
print(access_elements[0])
print(access_elements[-1])

# add elements into list
empty_list = []
empty_list.append(10)
print("after append", empty_list)

# inserting at index 0
empty_list.insert(0, 99)
print("inserted 99 at index 0", empty_list)

# add multiple elemejnts at the end
empty_list.extend([11, 22, 33])
print("extended [11, 22, 33] at the end: ", empty_list)