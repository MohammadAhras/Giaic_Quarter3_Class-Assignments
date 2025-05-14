# Lists
my_lists = [1,2,3,4,5]
print(my_lists[0]) #indexing
print(my_lists[1:3]) #slicing
my_lists.append(6)
print(my_lists)
my_lists.insert(2, 2.5)
print(my_lists)
my_lists.remove(2.5)
print(my_lists)

# TUPLES
my_tuple = (1,2,3,4,5)
print(my_tuple[0]) #indexing
print(my_tuple[1:3]) #slicing

# DICTIONARIES
my_dict = {"name": "Rizwan", "Age": 21}
print(my_dict["name"]) # get
print(my_dict)
print(my_dict["Age"]) # update
print(my_dict)
del my_dict["Age"] #delete
print(my_dict)