class Order():
    def __init__ (self, order_id: int, round_id: int, person_id: int, drink_name: str):
        self.id = order_id
        self.round = round_id
        self.person_id = person_id
        self.drink_name = drink_name