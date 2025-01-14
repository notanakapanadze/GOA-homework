
my_set = {1, 2, 3, 4, 5}


my_set.add(6)  
print("After add:", my_set)


my_set.remove(3) 
print("After remove:", my_set)

my_set.discard(10)
print("After discard:", my_set)


my_set.clear()  
print("After clear:", my_set)


another_set = {7, 8, 9}
union_set = my_set.union(another_set)
print("Union with another set:", union_set)


intersection_set = union_set.intersection({8, 9, 10}) 
print("Intersection:", intersection_set)


difference_set = union_set.difference({8, 9}) 
print("Difference:", difference_set)


copied_set = union_set.copy()
print("Copied set:", copied_set)
