import briw.src.helpers.strings as strings
from briw.src.helpers.menu_base import *

class HelpMenu(Menu):
    def __init__(self):
        
        people_help = MenuOption(strings.people_help)
        drink_help = MenuOption(strings.drinks_help)
        favourites_help = MenuOption(strings.favourites_help)
        rounds_help = MenuOption(strings.rounds_help)
        help_ = MenuOption(strings.help_help)
        exit_ = MenuOption(strings.exit_help)

        options = [people_help, drink_help, favourites_help, rounds_help, help_, exit_]

        super(HelpMenu, self).__init__(options, strings.help_menu_context)