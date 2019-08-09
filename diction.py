f = open("dictionary.txt", "r")
in_dictionary = False

print("can your password survive a dictionary attack?")
test_password = input("type in a trial password: ")

for line in f:
    if line.strip() == test_password.strip():
        in_dictionary = True
        print("Password match found: ", line.strip())
        break

if not in_dictionary:
    print("Password not found... in this dictionary attack")
