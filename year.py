print("How old will you be in 2025?")
print(2025-2002)

born=input ("what year were you born")
born = int(born)
age = (2025-born)
print(age)

print("In the year 2025 you will be",age, "years old!")

print()
print()
# While loop 
i = 0
while i <5:
	print(i)
	i += 1
print()
print (i)

i = 0 
for i in range(5):
	print(i)

i =-1
while True:
	i += 1

	if(i > 20):
	     break

	# i is odd
	if(i % 2 != 0):
		continue

	print(i)
