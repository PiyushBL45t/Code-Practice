a = set()
a.add(2)
print("The set is: ", a)
 
# output: The set is: {2}
 
a = {2, 3, 4, 5, 6}
a.clear()
print("The empty set is: ", a)
 
#output: The empty set is: set()
 
a = set([3, 4, 5, 6, 7])
b = a.copy()
print("The copy set b from a is:",b)
 
#output: The copy set b from a is: {3, 4, 5, 6, 7}
 
a = set([1, 2, 3, 4, 5, 6, 7])
b = set([4, 5, 6, 7, 8])
c = a.difference(b)
print("Difference between sets a and b is:", c)
 
#output: Difference between sets a and b is: {1, 2, 3}
 
a = set([1, 2, 3, 4, 5, 6, 7])
b = set([4, 5, 6, 7, 8])
a.difference_update(b)
print("Difference between sets a and b is:", a)
 
#output: Difference between sets a and b is: {1, 2, 3}
 
a = set([1, 2, 3, 4, 5, 6, 7])
a.discard(5)
print(a)
 
#output: {1, 2, 3, 4, 6, 7}
 
a = set([1, 2, 3, 4, 5, 6, 7])
b = set([2, 4, 6, 8, 10])
c = a.intersection(b)
print("Intersection of a and b is:", c)
 
#output: Intersection of a and b is: {2, 4, 6}
 
a = set([1, 2, 3, 4, 5, 6, 7])
b = set([2, 4, 6, 8, 10])
a.intersection_update(b)
print("Intersection of a and b on a is:", a)
 
#output: Intersection of a and b on a is: {2, 4, 6}
 
a = set([1, 2, 3, 4, 5, 6, 7])
b = set([2, 4, 6, 8, 10])
print(a.isdisjoint(b))
 
#output: False,
 
a = set([1, 2, 3, 4, 5, 6, 7])
b = set([-1, -2, -3 ,-4])
print(a.isdisjoint(b))
 
#output: True
 
a = set([1, 2, 3, 4, 5, 6, 7])
b = set([2, 4, 6, 8, 10])
print(a.issubset(b))
 
#output: False
 
a = set([1, 2, 3])
b = set([1, 2, 3, 4, 5, 6])
print(a.issubset(b))
 
#output: True
 
a = set([1, 2, 3, 4, 5, 6, 7, 8, 9 ,10])
b = set([2, 4, 6, 8, 10])
print(a.issuperset(b))
 
#output: True
 
a = set([1, 2, 3])
b = set([1, 2, 3, 4, 5, 6])
print(a.issuperset(b))
 
#output: False
 
a = set([1, 2, 3, 4, 5, 6, 7, 8, 9 ,10])
c = a.pop()
print(c)
 
#output: 1
 
a = set([1, 2, 3, 4, 5, 6, 7, 8, 9 ,10])
a.remove(6)
print(a)
 
#output: {1, 2, 3, 4, 5, 7, 8, 9, 10}
 
a = set([1, 2, 3, 4, 5, 6, 7, 8, 9 ,10])
b = set([1, 2, 4, 5, 6, 7])
c = a.symmetric_difference(b)
print(c)
 
#output: {3, 8, 9, 10}
 
a = set([1, 2, 3, 4, 5, 6, 7, 8, 9 ,10])
b = set([1, 2, 4, 5, 6, 7])
a.symmetric_difference_update(b)
print("Updated set a is: ", a)
 
#output: Updated set a is:  {3, 8, 9, 10}
 
a = set([1, 2, 3, 4, 5, 6, 7, 8, 9 ,10])
b = set([1, 2, 4, 5, 6, 7])
c = a.union(b)
print("Union of a and b is: ", a)
 
# output: Union of a and b is:  {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
 
a = set([1, 2, 3, 4, 5])
a.update({13, 14}, {45, 67})
print("Updates set a is: ", a)
 
#output: Updates set a is:  {1, 2, 3, 4, 5, 67, 13, 14, 45}
