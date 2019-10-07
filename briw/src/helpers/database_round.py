import src.helpers.database_base as db
import src.helpers.database_order as order_db
from src.helpers.round_class import Round

def insert_round_row(owner_id: int):
    query = f"INSERT INTO rounds (owner_id,active) VALUES ({owner_id},1)"
    db._insert_row(query)

def _parse_round_row(row):
    round_id = row[0]
    owner_id = row[1]
    active = row[2]
    orders = order_db.fetch_orders_from_round(round_id)
    new_round = Round(round_id,owner_id,active,orders)
    return new_round

def fetch_rounds():
    rounds = []
    try:
        results = db._fetch_table('rounds')
        for result in results:
            new_round = _parse_round_row(result)
            rounds.append(new_round)
    except:
        print("Connection Error.")
    return rounds

def get_active_round():
    try:
        query = "SELECT * FROM rounds WHERE active=1"
        results = db._query_database(query)
        if len(results) > 0:
            active_round = _parse_round_row(results[0])
            return active_round
        else:
            print("There was no active round found.")
    except:
        print("Connection Error.")

def get_round_by_id(round_id:int):
    try:
        query = "SELECT * FROM rounds WHERE round_id="+str(round_id)
        results = db._query_database(query)
        if len(results) == 1:
            active_round = _parse_round_row(results[0])
            return active_round
        else:
            print("There was no active round found.")
    except:
        print("Connection Error.")

def set_round_inactive(round_id: int):
    query = f"UPDATE rounds SET active=0 WHERE round_id={round_id}"
    db._query_database(query, False)