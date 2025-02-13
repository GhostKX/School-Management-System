# School Management System


# Dictionaries for storing students data
class_number = {}
class_letter = {}
class_room = {}
class_all = {}


# Logic for adding a new class
def add_class():
    add_number = input('\nType in number of the class: ')
    add_letter = input('Type in a letter of the class: ').upper()
    add_room = input('Type in three digit room number of the class: ')
    if add_number.isdigit() and len(add_letter) == 1 and add_letter.isalpha() and len(add_room) == 3 and add_room.isdigit() :
        add_number = int(add_number)
        add_room = int(add_room)

        room_exists = any(room == add_room for (number, letter, room) in class_all.keys())

        if room_exists:
            print('\nError: Room already in use!')
        else:
            class_number[add_number] = {'class_number': add_number}
            class_letter[add_letter] = {'class_letter': add_letter}
            class_room[add_room] = {'class_room': add_room}
            class_all[(add_number, add_letter, add_room)] = {'class_number': add_number, 'class_letter': add_letter,
                                                                     'class_room': add_room}
            show_class()
    else:
        print('\nError invalid symbol')


# Logic for deleting class
def delete_class():

    if len(class_all) == 0:
        print('\nNothing to delete!')
    elif len(class_all) != 0:
        show_class()
        delete_number = input('\nType a class number to delete: ')
        delete_letter = input('Type in a letter of the class to delete: ').upper()
        delete_room = input('Type in a room number to delete: ')

        if delete_number.isdigit() and len(delete_letter) == 1 and delete_letter.isalpha() and delete_room.isdigit() and len(delete_room) == 3:
            delete_number = int(delete_number)
            delete_room = int(delete_room)
            key = (delete_number, delete_letter, delete_room)
            if key in class_all:
                del class_all[key]
                del class_number[delete_number]
                del class_letter[delete_letter]
                del class_room[delete_room]
                print('\nClass successfully deleted!')
                show_class()
            else:
                print('\nClass not found!')
        else:
            print('\nError invalid symbol!')


# Logic for showing all classes
def show_class():
    if len(class_all) == 0:
        print('\nNo records!')
    elif len(class_all) != 0:
        print('\nClasses:')
        print('-'*35)
        print('{:<10} {:<10} {:<10} {:<10}'.format('ID','Number', 'Letter', 'Room\n'))
        count = 0
        for i, ((number, letter, digits), details) in enumerate(class_all.items(), 1):
            count += 1
            print('{:<10} {:<10} {:<10} {:<10}'.format(f'{i}.', number, letter, digits))
        print('-' * 35)
        print(f'Total number of classes: "{count}"\n')


# Logic for editing class details
def edit_class():
    show_class()
    if len(class_all) == 0:
        print('\nNo records!')
    else:
        edit_number = input('\nType in class number to edit: ')
        edit_letter = input('Type in class letter to edit: ')
        edit_room = input('Type in class room number to edit: ')

        if edit_number.isdigit() and len(edit_letter) == 1 and edit_letter.isalpha() and edit_room.isdigit() and len(edit_room) == 3:
            edit_number= int(edit_number)
            edit_room = int(edit_room)

            edit_key = (edit_number, edit_letter, edit_room)
            if edit_key in class_all.keys():
                del class_all[edit_key]
                del class_number[edit_number]
                del class_letter[edit_letter]
                del class_room[edit_room]

                new_number = input('\nType in a new number: ')
                new_letter = input('Type in a new letter: ')
                new_room = input('Type in a new room number: ')
                if new_number.isdigit() and len(new_letter) == 1 and new_letter.isalpha() and new_room.isdigit() and len(new_room) == 3:
                    new_number = int(new_number)
                    new_room = int(new_room)

                    class_number[new_number] = {'class_number': new_number}
                    class_letter[new_letter] = {'class_letter': new_letter}
                    class_room[new_room] = {'class_room': new_room}
                    class_all[(new_number, new_letter, new_room)] = {'class_number': new_number,
                                                                     'class_letter': new_letter,
                                                                     'class_room': new_room}
                    show_class()
                    print('\nChanges are saved successfully!')
                else:
                    print('\nError invalid symbol!')
            else:
                print('\nError invalid symbol!')


# Loop for calling logic functions until user decides to stop using it
while True:
    user = input('\nWelcome to the School Management System!\n'
                 '\nType in:\n'
                 '"Add" to a class\n'
                 '"Delete" to delete a class\n'
                 '"Edit" to change a class\n'
                 '"Show" to display classes\n'
                 '"Exit" to leave\n'
                 '::: ').lower()
    if user == 'add':

        # Calling the add function to add a new class
        add_class()

    elif user == 'delete':

        # Calling the delete function to delete the class
        delete_class()

    elif user == 'edit':

        # Calling the edit function to edit the class details
        edit_class()

    elif user == 'show':

        # Calling the show function to show the class details
        show_class()

    elif user == 'exit':
        print('\nExit')
        exit(0)

