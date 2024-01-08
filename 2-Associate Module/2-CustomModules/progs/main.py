import sys

sys.path.append(__file__ + "\\..\\..\\modules")

for p in sys.path:
    print(p)

import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))

