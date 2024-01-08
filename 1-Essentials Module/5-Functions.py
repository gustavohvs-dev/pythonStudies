def myFunction(x, y, z=1):
    return x + y + z

result = myFunction(1, 2)
print(result)


result = myFunction(z=2, y=1, x=3)
print(result)

def globalExample():
    global var #The global keyword has a power to change the var's value inside and outside a function
    var = 2
    print("Do I know that variable?", var)

