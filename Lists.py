list_of_random_things = [1, 3.4, 'a string', True]

list_of_random_things[0]
# Returns the first item in the list

list_of_random_things[len(list_of_random_things) - 1]
# Returns the last thing
# Don't forget to subtract ZEROth item >_>

list_of_random_things[-1]
# Last element
# -2 is second to last, etc

list_of_random_things = [1, 3.4, 'a string', True]
list_of_random_things[1:2]
# Returns 3.4 - skips 0th, grabs 1st, does not grab 2nd

list_of_random_things[:2]
# Returns [1, 3.4]

list_of_random_things[1:]
# Returns [3.4, 'a string', True]

# Check if something is in or not in a list
'this' in 'this is a string'
# True
'in' in 'this is a string'
# True
'isa' in 'this is a string'
# False
5 not in [1, 2, 3, 4, 6]
# True
5 in [1, 2, 3, 4, 6]
# False

# Mutability - Lists can be changed. Strings cannot.
# Are they mutable? Are they ordered?
# >>> my_lst = [1, 2, 3, 4, 5]
# >>> my_lst[0] = 'one'
# >>> print(my_lst)
# ['one', 2, 3, 4, 5]



