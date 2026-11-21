
# List comprehension
cube_list = [i**3 for i in range(1, 11)]

# Convert list into tuple
cube_tuple = tuple(cube_list)

# Set comprehension
cube_set = {i**3 for i in range(1, 11)}

# Dictionary comprehension
cube_dict = {i: i**3 for i in range(1, 11)}



# Output
print("List :", cube_list)
print("Tuple :", cube_tuple)
print("Set :", cube_set)
print("Dictionary :", cube_dict)