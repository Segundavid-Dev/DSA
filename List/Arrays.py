import array

# We Learn about arrays and how they are used in python 

# In python, an array is just an ordered sequence of homogenous elements. In other words, array can just hold one datatype


# Pythons arrays are intialized using the array library
new_array = array.array("f", [1,2,3])
print(new_array[0])

# Take note: that the array type in python is just a wrapper of the C array type


initializer_list  = [2,5,43,5,10,52,29,5]

number_array = array.array("i", initializer_list)

print(number_array[1:5]) 

# Changing or adding array elements
# Arrays are mutable, their elements can be changed in the same way as list elements

integers = array.array("i", [1,2,3,4,5])
integers[0] = 43
print(integers)

# Adding an element to the end of the array using the append() method

integers_append = array.array("i", [100, 101, 102, 103, 104])
integers_append.append(300) #append to the end of the array
print(integers_append)

# Concatenate two arrays using the + operators
odd = array.array("i", [1, 3, 5])
even = array.array("i", [2, 4, 6])
print(odd + even)

# Remove or delete elements in an array
integer_array = array.array("i", [1, 2, 3, 4, 5])

del integer_array[2] #removes 3
del integer_array[3] #removes 4

# .pop() method to remove
integer_array.pop(0) 
print(integer_array)