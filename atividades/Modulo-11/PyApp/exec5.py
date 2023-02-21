sets = {1, 2, 3, 4, 5}
print(sets)
print(type(sets))
sets.add(7)
print(sets)
sets.discard(3)
print(sets)

sets2 = {5, 6, 7, 8}

symetric_diff = sets.symmetric_difference(sets2)
print(symetric_diff)

dif = sets.difference(sets2)
dif2 = sets2.difference(sets)
print(dif2)
print(dif)

sets = sets.union(sets2)
print(sets)


intersection = sets.intersection(sets2)
print(intersection)



set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}

subset = set_b.issubset(set_a)
print(subset)

super_set = set_b.issuperset(set_a)
print(super_set)

lisst = ['Dog', 'Cat', 'Lion', 'Elefant', 'Lion', 'Jaguar', 'Zebra', 'Lion']
set_animals = set(lisst)
animals_list = list(set_animals)
print(set_animals)
print(animals_list)
