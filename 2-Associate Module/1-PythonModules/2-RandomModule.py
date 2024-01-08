from random import random, randrange, randint

for i in range(2):
    print(random())

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print()

for i in range(10):
    print(randint(1, 10), end=',')