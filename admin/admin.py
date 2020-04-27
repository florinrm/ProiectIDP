from flask import Flask, render_template, send_from_directory


def show_items():
    pass


def add_song():
    pass


def del_song():
    pass


def add_album():
    pass


def del_album():
    pass


def operate(option):
    if option == 1:
        show_items()
    elif option == 2:
        add_song()
    elif option == 3:
        del_song()
    elif option == 4:
        add_album()
    elif option == 5:
        del_album()
    else:
        print("Now exiting...")
        exit()


def print_options():
    print("1: View all items")
    print("2: Add a song")
    print("3: Delete a song")
    print("4: Add an album")
    print("5: Delete an album")
    print("6: Exit")


if __name__ == "__main__":
    while True:
        print_options()
        option = input("Write option: ")
        option = option.strip('\n')
        if not option.isnumeric():
            print("Option not a number")
            continue
        option = int(option)
        if option < 1 or option > 6:
            print("Given option not in range [1, 6]")
            continue
        operate(int(option))