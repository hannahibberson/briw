menu_context = "Hello! What do you want to do today?"
get_people = "Show the list of people"
get_drinks = "Show the list of drinks"
favourites = "View or edit the list of people's favourite drinks"
edit_people = "Edit the list of people"
edit_drinks = "Edit the list of available drinks"
get_help = "I need help"
exit_ = "Exit"

help_context = "I store information about people and their favourite drinks, and through this menu you can see those lists and add new people and drinks!"
get_people_help = "You can be shown a list of all the people we have stored"
get_drinks_help = "You can be shown a list of all the favourite drinks we have stored"
favourites_help = "Assign each name with a favourite drink so you always know what to get people!"
edit_people_help = "Add or remove people from the list of people"
edit_drinks_help = "Add or remove people from the list of drinks"
help_help = "That's what got you here!"
exit_help = "Exit this menu and continue with your day"

menu_return = "Press 'enter' to return to the main menu."

def list_add(title):
    return f"""
ADDING NEW {title.upper()}
--------------------
Please enter your list separated by commas. For example:
    a, b, c
To make no changes, please respond with 'quit'.
    """
def list_remove(title):
    return f"""
REMOVING {title.upper()}
--------------------
Please enter a list of id codes of {title.lower()} you would like to remove, separated by commas. For example:
    a, b, c
To make no changes, please respond with 'quit'.
    """