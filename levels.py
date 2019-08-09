#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
aList = [0, 1]

#Generates a random integer.
aRandomIndex = randint(0, len(aList)-1)

#Code below is the skeleton for a simple name generator.
#Create the list of words you want to choose from.

# Create a variable for the name
name = ""
word_list = ['ruby', 'bob', 'lucy', 'jane', 'chloe']
# This will work through the name
for x in range(5):
    #Generates a random integer.
    x = randint(0, len(word_list)-1)
    name += word_list[x] + ""
    print(name)
    break

#Print the Name

#Code below is the skeleton for a menu generator.

#Create the 3 lists of words you want to choose from.

#Create a sides_selected list
side = ['beans', 'coslaw', 'mac and cheese', 'salad']
sides_selected = []
# This will work through the name
for x in range(4):

    #Generates a random integer.
    x = randint(0, len(side)-1)
    sides_selected.append(side[x])
    print("sides: ", sides_selected)
    break
main = ['tacos', 'burritos', 'pizza', 'chicken']
main_selected = []
# This will work through the name
for x in range(4):

    #Generates a random integer.
    x = randint(0, len(main)-1)
    main_selected.append(main[x])
    print("main: ", main_selected)
    break
dessert = ['cookies', 'cake', 'icecream', 'brownies']
dessert_selected =[]
# This will work through the name
for x in range(4):

    #Generates a random integer
    x = randint(0, len(dessert)-1)
    dessert_selected.append(dessert[x])
    print("dessert: ", dessert_selected)
    break
