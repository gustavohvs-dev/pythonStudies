#This is a one line comment

print("Hello World!")

'''
You can make a comment block using three single quotes together
'''
print("You can break the line\nusing '\\n'")

x = 1
print("It's possible", "using more than", x , "string argument")

#Its possible set a string to show between the words and in the end of the sentence
print("My", "name", "is", "Joe", sep="-", end=".")

#You can print octals and hexadecimals number too
print(0o123)
print(0x123)

#Python operators
print(2+2)
print(2-2)
print(2*2)
print(2/2)
print(2**3)
print(5//2)
print(5%2)

#Operators priorities
print(2 + 3 * 5)
print(9 % 6 % 2) # % (modulo) has left-sided binding
print(2 ** 2 ** 3) # ** (exponentiation) uses right-sided binding
print(2 * 3 % 5)
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)

#You can short some expressions
x = x + 2
print(x)
x *= 2
print(x)

#It's possible combine text and variables using +
var = "007"
print("Agent " + var)

#You can ask the user types a value on terminal using input()
inputSomething = input("Input a number: ")
print("The value inputed was: " + inputSomething)

#You can do a type conversion writing typeName(variable)
inputSomething = str(inputSomething)