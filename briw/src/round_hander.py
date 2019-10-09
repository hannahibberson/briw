from briw.src.round_class import Round
from briw.src.order_class import Order
import briw.src.database_round as round_db
import briw.src.database_preference as pref_db
import briw.src.database_order as order_db

def get_rounds():
    return round_db.fetch_rounds()

def get_round_by_id(round_id: int):
    return round_db.get_round_by_id(round_id)

def get_active_round():
    return round_db.get_active_round()

def start_round(owner_id: int):
    round_db.insert_round_row(owner_id)

def end_round(round_id: int):
    round_db.set_round_inactive(round_id)

