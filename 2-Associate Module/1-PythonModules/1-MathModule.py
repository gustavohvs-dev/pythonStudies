# Import all functions of the module
import math 

# Import some functions of the module
#from math import pi, radians, degrees, sin, cos, tan, asin, e, exp, log, ceil, floor, trunc, factorial, hypot

# The most agressive way to import all functions of the module
#from math import * 

# Imports math's module with a alias
#import math as mathFunctions 

# Import separate functions from a module using alias
#from module import n as a, m as b, o as c 

print(math.sin(math.pi/2))

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


pi = 3.14

print(sin(pi/2))
print(math.sin(math.pi/2))
