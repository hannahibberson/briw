import strings
s = strings.Strings()

class MenuOption:
    def __init__(self, text, enabled=False):
        self.text = text
        self.enabled = enabled
    def enable(self):
        self.enabled = True
    def disable(self):
        self.enabled = False

class Menu:
    def __init__(self, menu_options, menu_context):
        self.options = menu_options
        self.context = menu_context

    def enable_option(self, option):
        self.options[option].enable()

    def disable_option(self, option):
        self.options[option].disable()

    def get_active_items(self):
        items = []
        for option, option_details in self.options.items():
            if option_details.enabled == True:
                items.append(option)
        return items

    def print_menu(self):
        print(self.context,'\n')
        option_list = self.get_active_items()
        for option in option_list:
            list_number = option_list.index(option) + 1
            option_text = self.options[option].text
            print(" ",list_number,option_text)
        print()
    
    def get_option(self, index):
        menu_options = self.get_active_items()
        return menu_options[index]

class MainMenu(Menu):
    def __init__(self):
        options = {
            "get_people": MenuOption(s.get_people),
            "get_drinks": MenuOption(s.get_drinks),
            "edit_people": MenuOption(s.edit_people,True),
            "edit_drinks": MenuOption(s.edit_drinks,True),
            "edit_favourites": MenuOption(s.favourites),
            "help": MenuOption(s.get_help,True),
            "exit": MenuOption(s.exit_,True)
        }
        super(MainMenu, self).__init__(options, s.menu_context)

class HelpMenu(Menu):
    def __init__(self):
        options = {
            "get_people": MenuOption(s.get_people_help),
            "get_drinks": MenuOption(s.get_drinks_help),
            "edit_people": MenuOption(s.edit_people_help,True),
            "edit_drinks": MenuOption(s.edit_drinks_help,True),
            "edit_favourites": MenuOption(s.favourites_help),
            "help": MenuOption(s.help_help,True),
            "exit": MenuOption(s.exit_help,True)
        }
        super(HelpMenu, self).__init__(options, s.help_context)