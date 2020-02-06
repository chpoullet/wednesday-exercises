#Assignment for post class
# Learning outcome: [variables, print, different data types]
# ask and store the following in variables:
 # Name, last_name, age, age_of_mother, 3 skills
 # Print out the information in a formated manor
 # Calculate age difference between response and mother
 # Store skills in a list
 # Print each skill in a formated way.
# Definition of formated
 # a little context text
 # appropriate string formating like lower case or upper case, or other
# assignment to variable


first_name = input('What is your name?' ).strip().capitalize()
last_name = input('What is your last name?' ).strip().capitalize()
age = int(input('What is your age? '))
age_of_mother = int(input("What is your mother's age? "))
skill1 = input('What is a skill of yours? ').strip()
skill2 = input('Another skill? ').strip()
skill3 = input('One more skill? ').strip()

print(f'Your name is {first_name} {last_name}, you are {age} years old, your mother is {age_of_mother} years old, and your skills are: {skill1}, {skill2} and {skill3}.')

age_difference = age_of_mother - age
print(age_difference)

skillset = [
    skill1,
    skill2,
    skill3,
]

print(skillset)

print(f"Your first skill is {skill1}, that's impressive! {skill2} is also a good skill to have, as well as {skill3}.")
