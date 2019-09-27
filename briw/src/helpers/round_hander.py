from src.helpers.round_class import Round
from src.helpers.order_class import Order
import src.helpers.database_round as round_db
import src.helpers.database_preference as pref_db
import src.helpers.database_order as order_db

def get_rounds():
    return round_db.fetch_rounds()

def get_round(round_id: int):
    return round_db.get_round(round_id)

def get_active_round():
    return round_db.get_active_round()

def start_round(owner_id: int):
    round_db.insert_round_row(owner_id)

def end_round(round_id: int):
    round_db.set_round_inactive(round_id)

