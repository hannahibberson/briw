round_count = {}
class Round:
    active = False
    totalRounds = 0
    def __init__(self, owner, onlyTeam=True):
        self.owner = owner
        self.people = [owner]
        self.team = owner.team
        if onlyTeam == False:
            self.team = None

    def start(self):
        print("A new round has started!")
        self.active = True

    def join(self,person):
        if self.active == True:
            if self.team == person.team or self.team == None:
                self.people.append(person)
                print(f"{person.name.capitalize()} has been added to the current round.")
            else:
                print(f"Sorry, this round is currently being run by the {self.team.capitalize()} team.")
        else:
            print("Sorry, there's currently no round active!")

    def end(self):
        print("The round has been closed.")
        self.active = False
        print("\n-----------------------\nYou need to make:\n-----------------------")
        for drink_type, drinks in self.get_drinks().items():
            print(f"{drink_type.capitalize()}:")
            for drink, count in drinks.items():
                print(count,drink.name.capitalize())
        print("-----------------------\n")
        self.people = [self.owner]
        self.totalRounds += 1

    def get_all_data(self):
        # owner - string
        # people - list
        # team - string
        # active - bool
        # onlyTeam - bool

        all_data_list = [self.owner.uuid, self.people, self.team, self.active]
        return all_data_list

    def get_owner_name(self):
        return self.owner.name

    def get_drinks(self):
        drinks = {}
        for member in self.people:
            drink_type = member.favourite.type
            if not drink_type in drinks.keys():
                drinks[drink_type] = {}
            drink_name = member.favourite.name
            if not drink_name in drinks[drink_type].keys():
                drinks[drink_type][drink_name] = 0
            drinks[drink_type][drink_name] += 1
        return drinks

    def get_deliveries(self):
        deliveries = []
        for member in self.people:
            deliveries.append({"name":member.name,"drink":member.favourite.name})
        return deliveries

class Person:
    def __init__(self, name, team, slack_name, favourite, fav_additionals=None):
        self.name = name
        self.favourite = favourite
        self.fav_additionals = fav_additionals
        self.team = team
        self.uuid = slack_name

    def change_favourite(self,favourite):
        self.favourite = favourite

    def change_team(self, team):
        self.team = team

    def get_all_data(self):
        all_data_list = [self.name, self.favourite, self.team, self.uuid]
        return all_data_list

class Drink:
    def __init__(self, name, drink_type):
        self.name = name
        self.type = drink_type
    
    def get_all_data(self):
        all_data_list = [self.name, self.type]
        return all_data_list

class Coffee(Drink):
    def __init__(self, name):
        super(Coffee, self).__init__(name, "coffee")

class Tea(Drink):
    def __init__(self, name):
        super(Tea, self).__init__(name, "tea")

latte = Coffee("Latte")
americano = Coffee("Americano")
chai = Tea("Chai")
earl = Tea("Earl Grey")
lemonade = Drink("lemonade", "fizzy")

hannah = Person("Hannah", lemonade, "melon", "0")
billy = Person("Billy", chai, "melon", "1")
henry = Person("Henry", latte, "apple", "2")
bob = Person("Bob", chai, "lemon", "3")
jimmy = Person("Jimmy", americano, "apple", "4")
jimbo = Person("Jimbo", earl, "apple", "5")

people = [billy, henry, bob, jimmy, jimbo]

round1 = Round(hannah)
round1.join(billy)
print("\n")
round1.start()
for person in people:
    round1.join(person)
round1.end()

round2 = Round(hannah, False)
round2.start()
for person in people:
    round2.join(person)
# round2.end()

print(round2.get_all_data())
