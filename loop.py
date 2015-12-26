choice = raw_input('Enjoying the course? (y/n)')

while choice is not "y" and choice is not "n":  # Fill in the condition (before the colon)
    print "old choice: " + choice
    choice = raw_input("Sorry, I didn't catch that. Enter again: ")
