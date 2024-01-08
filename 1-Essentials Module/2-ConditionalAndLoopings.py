#Comparative operators ==, !=, >, <, >=, <=
if(2 == 2):
    print("True")
else:
    print("False")

print("While Looping")
x = 3
while (x > 0):
    print(x)
    x-=1

print("For Looping")
for i in range(5):
    print(i)

for i in range(2, 8):
    print("The value of i is currently", i)

for i in range(2, 8, 3):
    print("The value of i is:", i)

print("\nThe break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")

print("\nYou can use else statement with while")
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

print("\nYou can use else statement with for too")
for i in range(5):
    print(i)
else:
    print("else:", i)

print("\nIt's possible use a string in the for statement")
word = "Python"
for letter in word:
    print(letter, end="*\n")

text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")

print("\n\nYou can do multiple comparisons with 'and' and 'or'")
if(1 == 1 and 2 == 2):
    print("Testing 'and'")
