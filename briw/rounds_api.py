import src.helpers.round_hander as handler
import src.helpers.database_order as order_db
import src.helpers.database_preference as pref_db
from src.helpers.round_class import Round
from src.helpers.order_class import Order

def get_rounds():
    return handler.get_rounds()

def get_active_round():
    return handler.get_active_round()

def get_round(id:int):
    return handler.get_round_by_id(id)

def add_round(data):
    handler.start_round(data["owner_id"])
    add_order_to_round({'person_id':data["owner_id"]})

def add_order_to_round(data):
    active_round: Round = get_active_round()
    person_id = int(data["person_id"])
    drink_name = pref_db.get_preference(person_id)
    order_db.insert_order_row(active_round.id, person_id, drink_name)

def stop_round():
    active_round = get_active_round()
    handler.end_round(active_round.id)
    