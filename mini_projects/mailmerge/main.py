import os

PLACEHOLDER = "[name]"

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, './Input/Names/invited_names.txt')
with open(filename) as names_file:
    names = names_file.readlines()
    print(names)

filename2 = os.path.join(dirname, './Input/Letters/starting_letter.txt')
with open(filename2) as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.rstrip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        completed_letter_dir = os.path.join(dirname, "./Output/ReadyToSend/letter_for_%s.txt" % stripped_name)
        with open((completed_letter_dir), mode="w") as completed_letter:
            completed_letter.write(new_letter)




