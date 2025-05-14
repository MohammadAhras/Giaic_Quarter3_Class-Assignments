# Sets

my_set = {1,2,3,4,5}
my_set.add(6)
print(my_set)
my_set.remove(3)
print(my_set)
set1 = {4,2,6}
set2 = {9,0,3}
print(set1.union(set2)) # union
print(set1.intersection(set2)) # intersection
print(set1.difference(set2)) # Difference

# Frozensets
frozen_set1 = frozenset({1,2,3,4})
frozen_set2 = frozenset({3,4,5})
print(frozen_set1.union(frozen_set2))
print(frozen_set1.intersection(frozen_set2))
print(frozenset)
print(frozen_set1.difference(frozen_set2))
print(frozenset)