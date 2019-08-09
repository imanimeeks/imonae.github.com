# Python program to demonstrate
# Creating of list
# Creating a list
List = []
print("Initial blank list: ")
print(List)

# Creating a List with
# the use of a string
List = ['GeeksForGeeks']
print("\n List with the use of String: ")
print(List)

# Creating a List with
# the use of multiple values
List = ["Geeks", "For", "Geeks"]
print("\nList containing multiple values: ")
print(List[0])
print(List[2])

# Creating a Multi-Dimensional List
# (By Nesting a list inside a list)
List = [['Geeks', 'For'],['Geeks']]
print("\nMulti-Dimensional List: ")
print(List)

# Creating a List with
# the use of numbers
# (Having duplicate values)
List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print("\n List with the use of the Numbers: ")
print(List)
# Creating a List with
# mixed types of values
# (Having numbers and strings)
List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
print("\nList with the use of Mixed Values: ")
print(List)

# Creating a List
name = ['Jimmy','Skylar', 'Tom', 'Rebecca','Becky']
print("\nList containing names")
print(List[0])
print(List[4])

print("************")
# Python program to demonstrate
# Addition of elements in a list

# Creating a list
ListA = []
print("Intial Blank List: ")
print(ListA)

# Addition of Elements
# in the List
ListA.append(1)
ListA.append(2)
ListA.append(4)
print("\nList after Addition of Three elements: ")
print(ListA)

# using Iterator
for i in range(1, 6):
     ListA.append(i)
print("\nList after Addition of elements from 1-3: ")
print(ListA)

# Adding Tuples to the List
ListA.append((5,6))
print("\nList after Addition of a Tuple: ")
print(ListA)

# Addition of List to a List
List2 = ['For','Geeks']
ListA.append(List2)
print("\nList after Addition of a List: ")
print(ListA)

# Addition of Element at
# specific Position
# (using Insert Method)
ListA.insert(3, 12)
List2.insert(0, 'Geeks')
print("\nList after performing Insert Operation: ")
print(ListA)

# Addition of Element at
ListA.remove(12)
print("\nList after performing Remove Operation: ")
print(ListA)
