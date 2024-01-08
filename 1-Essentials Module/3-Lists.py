numbers = [10, 5, 7, 2, 1]
print("List content:", numbers)

numbers[0] = 11;
print("List content:", numbers)

del numbers[1]
print("List content:", numbers)

print("List's length:", len(numbers))

#result = function(arg) 
#result = data.method(arg)

numbers.append(4)
print("List content:", numbers)

numbers.insert(0, 222)
print("List content:", numbers)

#The inner life of lists
print("Pay attention with the inner life of lists!!")
print("If you want to assign a new list with a old list, try this:")
list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)
print(list_1)

print("But if you want to copies a list to a new one, try this instead:")
#Copying intire list
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)
print(list_1)

#Copying part of the list
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

#Copying part of the list using negative indice
my_list = [10, 8, 6, 4, 2, 1, 2, 5, 8]
new_list = my_list[1:-1]
print(new_list)

#Verify if something exists inside the list
my_list = [0, 3, 12, 8, 2]
print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

#Two-dimensional arrays
board = []

for i in range(8):
    row = [0 for i in range(8)]
    board.append(row)
    
print(board)

#Setting a 3x2 array
temps = [[1 for h in range(3)] for d in range(2)]
print(temps)

#Three-dimensional arrays
rooms = [[[False for r in range(3)] for f in range(3)] for t in range(3)]
print(rooms)