import helpers.user_input as u_input
import helpers.strings as strings

class MenuOption:
    def __init__(self, text, enabled=True):
        self.text = text
        self.enabled = enabled
    def enable(self):
        self.enabled = True
    def disable(self):
        self.enabled = False

class ExitOption(MenuOption):
    def __init__(self):
        super(ExitOption, self).__init__(strings.menu_return)

    def execute(self):
        return

class Menu:
    def __init__(self, menu_options, menu_context):
        self.options = menu_options
        self.context = menu_context

    def get_active_items(self):
        items = []
        for option in self.options:
            if option.enabled == True:
                items.append(option)
        return items

    def print_menu(self):
        print(self.context,'\n')
        option_list = self.get_active_items()
        for option in option_list:
            list_number = option_list.index(option) + 1
            option_text = option.text
            print(" ",list_number,option_text)
        print()

    def option_input_validation(self, user_input):
        try:
            option_number = int(user_input)
            if option_number > 0 and option_number < len(self.get_active_items()):
                return True
            else:
                return False
        except:
            return False

    def get_option(self):
        option_number = int(u_input.user_input(self.option_input_validation, "Option: "))
        option = self.get_active_items()[option_number-1]
        return option
    
    def perform_option(self, option):
        if (option.execute):
            return option.execute()

    def run(self):
        self.print_menu()
        option = self.get_option()
        return self.perform_option(option)