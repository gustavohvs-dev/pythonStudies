# Example 1

word = 'by'
print(len(word))


# Example 2

empty = ''
print(len(empty))


# Example 3

i_am = 'I\'m'
print(len(i_am))

multiline = '''Line #1
Line #2'''

print(len(multiline))

str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)

# Demonstrating the ord() function. If you want to know a specific character's ASCII/UNICODE code point value, you can use a function named ord() (as in ordinal).

char_1 = 'a'
char_2 = ' '  # space

print(ord(char_1))
print(ord(char_2))

# Demonstrating the chr() function. If you know the code point (number) and want to get the corresponding character, you can use a function named chr().

print(chr(97))
print(chr(945))

# Indexing strings.

the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print()

# Slices

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])

# In and not in functions

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet)
print("f" not in alphabet)

# Demonstrating min() - Example 1:
print(min("aAbByYzZ"))


# Demonstrating min() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))

# Demonstrating max() - Example 1:
print(max("aAbByYzZ"))


# Demonstrating max() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))

# Demonstrating the index() method:
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

# Demonstrating the list() function:
print(list("abcabc"))

# Demonstrating the count() method:
print("abcabc".count("b"))
print('abcabc'.count("d"))

# Demonstrating the capitalize() method:
print('aBcD'.capitalize())

# Demonstrating the center() method:
print('[' + 'alpha'.center(10) + ']')

# Demonstrating the endswith() method:
if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")

# Demonstrating the find() method:
print("Eta".find("ta"))
print("Eta".find("mma"))

# Demonstrating the isalnum() method: The parameterless method named isalnum() checks if the string contains only digits or alphabetical characters (letters), and returns True or False according to the result.
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

# The isalpha() method is more specialized - it's interested in letters only.
# Example 1: Demonstrating the isapha() method:
print("Moooo".isalpha())
print('Mu40'.isalpha())

# Example 2: Demonstrating the isdigit() method:
print('2018'.isdigit())
print("Year2019".isdigit())

# Example 1: Demonstrating the islower() method:
print("Moooo".islower())
print('moooo'.islower())

# Example 2: Demonstrating the isspace() method:
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

# Example 3: Demonstrating the isupper() method:
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())

# Demonstrating the join() method:
print(",".join(["omicron", "pi", "rho"]))

# Demonstrating the lower() method:
print("SiGmA=60".lower())

# The parameterless lstrip() method returns a newly created string formed from the original one by removing all leading whitespaces.
# Demonstrating the lstrip() method:
print("[" + " tau ".lstrip() + "]")

# Demonstrating the replace() method:
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))

# The one-, two-, and three-parameter methods named rfind() do nearly the same things as their counterparts (the ones devoid of the r prefix), but start their searches from the end of the string, not the beginning (hence the prefix r, for right).
# Demonstrating the rfind() method:
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))

# Two variants of the rstrip() method do nearly the same as lstrips, but affect the opposite side of the string.
# Demonstrating the rstrip() method:
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))

# Demonstrating the split() method:
print("phi       chi\npsi".split())

# Demonstrating the startswith() method:
print("omega".startswith("meg"))
print("omega".startswith("om"))

# Demonstrating the strip() method:
print("[" + "   aleph   ".strip() + "]")

# The swapcase() method makes a new string by swapping the case of all letters within the source string: lower-case characters become upper-case, and vice versa.
# Demonstrating the swapcase() method:
print("I know that I know nothing.".swapcase())

# The title() method performs a somewhat similar function - it changes every word's first letter to upper-case, turning all other ones to lower-case.
# Demonstrating the title() method:
print("I know that I know nothing. Part 1.".title())

# Last but not least, the upper() method makes a copy of the source string, replaces all lower-case letters with their upper-case counterparts, and returns the string as the result.
# Demonstrating the upper() method:
print("I know that I know nothing. Part 2.".upper())

# Demonstrating the sorted() function:
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)

print(first_greek)
print(first_greek_2)

# Demonstrating the sort() method:
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)

second_greek.sort()
print(second_greek)


