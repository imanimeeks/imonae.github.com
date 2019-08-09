
# Creates the dictionary to store responses.
answers = {}


'''
Below, write code that will pose the survey questions from the student prompt
to a user. Your program should save user input as a dictionary.
'''
survey = [
"what is your name?",
"How old are you?",
"What is you hometown?",
"What is your date of birth? (DD/MM/YYYY)"

keys = ["name", "age", "hometown", "DOB"]

for x in range(len(survey))
    response = input(survey[x] +":     ")
    answers[keys[x]] = responses
# Print the context of the dictionary.
print(answers)
