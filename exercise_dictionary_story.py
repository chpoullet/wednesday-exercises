# Assignment2 for post class
#
# define an empty dictionary# name_dict = {}
# Prompt user for input for a story.
# it should have:
    # hero, beggiging, middle, end
    # 2 other things you define to be part of the story.
    # add each response to the dictionary under an appropriate key
# Print out the dictionary information in an ordered way so we can read the story.


story = {}

hero = input('Please enter the name of the hero:   ').capitalize()
villain = input('Please enter the name of the villain:    ').capitalize()
beginning = input('Please enter the beginning of your story:  ').capitalize()
middle = input('Please enter the middle part to your story:   ').capitalize()
end = input('Please enter the end part to your story:   ').capitalize()
plot = input('Please enter a plot summary:   ').capitalize()

story['hero'] = hero
story['villain'] = villain
story['beginning'] = beginning
story['middle'] = middle
story['end'] = end
story['plot'] = plot

print(story)

view_story = input('Do you want to view your story? Y/N:   ').strip().upper()

if view_story == 'Y':
    view_specificstory = input("What part of the story do you want to view? (beginning, middle, end, plot, hero, villain    )")
    if view_specificstory == 'beginning':
        print(story['beginning'])
    if view_specificstory == 'middle':
        print(story['middle'])
    if view_specificstory == 'end':
        print(story['end'])
    if view_specificstory == 'plot':
        print(story['plot'])
    if view_specificstory == 'hero':
        print(story['hero'])
    if view_specificstory == 'villain':
        print(story['villain'])

else:
    print('Bye.')
