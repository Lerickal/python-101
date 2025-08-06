#sets

my_set = {0,1,2,3,4,5}
print(my_set)

my_set.add(6)
my_set.remove(3)
print(my_set)

set1 = {0,1,2,3,4,5}
set2 = {3,4,5,6,7,8,9}

union_set = set1.union(set2)
print(union_set)

intersetion = set1.intersection(set2)
print(intersetion)

diff_set = set1.difference(set2)
print(diff_set)