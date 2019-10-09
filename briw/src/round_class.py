class Round:
    def __init__(self, id: int, owner_id: int, active: bool, orders):
        self.id = id
        self.owner_id = owner_id
        self.active = active
        self.orders = orders