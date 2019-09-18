from helpers import *

def main():
    screen.clear()
    store = files.store()
    while True:
        menu, help = screen.getMenus(len(store["people"]), len(store["drinks"]))
        screen.printMenu(menu, 'main')
        command = user_input.getCommand()
        command_string = menu[command - 1]
        if command_string == strings.exit_:
            screen.clear()
            print("See you again soon!")
            files.write(store)
            exit()
        if command_string == strings.get_help:
            screen.clear()
            screen.printMenu(help, "help")
            screen.returnMenu()
        elif command_string == strings.get_people:
            screen.printList('people',store["people"])
            screen.returnMenu()
        elif command_string == strings.get_drinks:
            screen.printList('drinks',store["drinks"])
            screen.returnMenu()
        elif command_string == strings.edit_people:
            store = edit_lists.editList("people",store)
            screen.printList('people', store['people'])
            screen.returnMenu()
        elif command_string == strings.edit_drinks:
            screen.printList('drinks', store['drinks'])
            store = edit_lists.editList("drinks",store)
            screen.returnMenu()
        elif command_string == strings.favourites:
            # TODO: assign favourites
            screen.returnMenu()
        store = edit_lists.checkLists(store)
        files.write(store)
        screen.clear()

main()
