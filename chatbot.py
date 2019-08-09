# --- Define your functions below! ---
def intro():
    print("Hello, my name is chatterbox.")
    print("You can type whatever you like and press enter")
# Choose a response based on the user's input.
    # Define a lsit of possible ways the user might say hello.
greetings = ["hi","hello", "hey", "hey there", "sup"]
goodbyes = ["bye", "adios", "ciao", "bye-bye"]

def process_input(answer):
    if is_valid_input(answer, greetings) :
        say_greeting()
    elif is_valid_input(answer, goodbyes) :
        say_goodbye()
    else:
        say_default()

    # Display a greeting message to the user
def say_greeting() :
    print("Hey there!")

def say_goodbye() :
    print("Bye there!")

def say_default():
    print("That's cool!")

def is_valid_input(user_input, valid_responses):
 for item in valid_responses:
     if user_input == item:
            return True
 return False

    # Display a defauly message to the user.
# --- Put your main program below! ---
    # choose a response based on the user's input.
def main():
    intro()
    while True:
        answer = input("(What will you say?) ")
        process_input(answer)



# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()
