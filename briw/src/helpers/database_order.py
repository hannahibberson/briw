import src.helpers.database_base as db
from src.helpers.order_class import Order

def insert_order_row(round_id: int, person_id: int, drink_name: str):
    query = f"INSERT INTO orders (round_id,person_id,drink_name) VALUES ({round_id},{person_id},\"{drink_name}\")"
    db._insert_row(query)

def _parse_order_row(row):
    order_id = row[0]
    person_id = row[1]
    drink_name = row[2]
    round_id = row[3]
    order = Order(order_id, round_id, person_id, drink_name)
    return order

def fetch_orders():
    orders = []
    try:
        results = db._fetch_table('orders')
        for result in results:
            order = _parse_order_row(result)
            orders.append(order)
    except:
        print("Connection Error.")
    return orders

def fetch_orders_from_round(round_id:int):
    query = "SELECT * FROM orders WHERE round_id="+str(round_id)
    results = db._query_database(query)
    orders = []
    for result in results:
        order = _parse_order_row(result)
        orders.append(order)
    return orders