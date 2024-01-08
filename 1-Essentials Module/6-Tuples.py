'''
Tuples work similarly to lists, however they are immutable while lists are mutable
'''

#Creating tuples example
this_is_a_list = [1, 2, 3]
this_is_a_tuple = (1, 2, 3)
this_is_also_a_tuple = 1, 2, 3

print(this_is_a_tuple)
print(this_is_also_a_tuple)

print(type(this_is_also_a_tuple))

print(this_is_a_tuple[0])
print(this_is_a_tuple[-1])
print(this_is_a_tuple[1:])
print(this_is_a_tuple[:2])
print(this_is_a_tuple[:-2])

my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)

