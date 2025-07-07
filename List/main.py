# myList = ['a', 'apple', 1, 3.14]


# # Initializing a list
# example_list = [3.14159, "apple", 23]
# empty_list = []
# sequence_list = list(range(10))

# print(example_list)
# print(empty_list)
# print(sequence_list)

# a_list = [2, "Educative", "A"]

# def foo():
#     print("Hello from foo()!")


# another_list = [a_list, "Python", foo, ["Yet another list"]]

# print(another_list[0]) #Elements of aList
# print(another_list[0][1]) #Second element of aList
# print(another_list[1]) #Python

# # Append function
# # Use this function to add a single element to the end of a list. This function works in O(1), constant time

# list = [1, 3, 5, 'seven']
# print(list)
# list.append(9)
# print(list)


# # Insert function
# # inserts an element to the list. use it like list.insert(index, value). It works in O(n) time. Try it out yourself
# # Depends on the the input size of n

# list.insert(0, 2)
# print(list)

# # Remove function 
# # removes the given element at a given index.  use it like list.remove(element)

# print(list)
# list.remove("seven")
# print(list)
# # Runs in O(n)
# # if value not in list, you get a run time value error
# # list.remove(0)

# list.reverse()
# print(list)

# Why the .remove() is O(n) ?
# The .remove(x) method searches from the beginning of the list to the end to find the first occurence of the elemnent x, then removes it

# It starts at index 0 and checks each element until it finds 3.

# In the worst case, x is at the end (or not present), so it needs to scan the entire list: O(n).

# After finding the element, it needs to shift all elements after it one position to the left to fill the gap — also O(n) in worst case.

# Pop function
# list 

# Summary                  Time complexity
# list.remove(x)              O(n)
# list.insert(i, x)           O(n)
# list.pop(i)                 O(1)
# reverse()


# Slice Notation Examples

new_list = list(range(10))
print(new_list[3:])

# initializing list elements
x = list(range(5))
print(x) #0, 1, 2, 3, 4, 5
x[1:4] = [45, 21, 83]
print(x)

# Deleting elements from a list
del_list = list(range(10))
print(del_list)
del del_list[::2]
print(del_list)