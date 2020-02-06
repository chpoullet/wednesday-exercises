# Assignment2 for post class
#
# define an empty dictionary# name_dict = {}
# Prompt user for input for a story.
# it should have:
    # hero, beggiging, middle, end
    # 2 other things you define to be part of the story.
    # add each response to the dictionary under an appropriate key
# Print out the dictionary information in an ordered way so we can read the story.



defined_name = input("What would you like your hero/heroine's name to be?  ").strip().capitalize()

story = {
    'Beginning': ' ',
    'Middle': ' ',
    'End': ' ',
    'hero': ' '
}


print(f"{story['hero']}{story['Beginning']}")
print(story['Middle'])


middle_input = input("Do you enter the door? Y/N:  ").strip().upper()
if middle_input == 'Y':
    print('You enter the door and escape.')
else:
    print(story['End'])



