from http.server import HTTPServer, BaseHTTPRequestHandler

from briw import rounds_api, people_api, drinks_api, preferences_api
import briw.src.helpers.database_order as order_db

def render_drinks(drinks):
    drinks_html = ""
    for drink in drinks:
        drinks_html += f'<li>{drink.name.capitalize()} ({drink.type.capitalize()})</li>'
    return drinks_html

def render_people(people):
    people_html = ""
    for person in people:
        people_html += f'<li>{person.name.title()}</li>'
    return people_html

def render_preferences(prefs):
    pref_html = ""
    for person_id,drink_name in prefs.items():
        person = people_api.get_person_by_id(str(person_id))
        pref_html += f'<li>{person.name.title()} - {drink_name.capitalize()}</li>'
    return pref_html

def render_rounds(rounds):
    round_html = ""
    for round_ in rounds:
        if round_.active != 1:
            order_html = render_orders(round_)
            round_html += f'<li> Round {round_.id}: <ul>{order_html}</ul></li>'
    return round_html

def render_orders(round_):
    orders = order_db.fetch_orders_from_round(round_.id)
    order_html = ""
    for order in orders:
        person = people_api.get_person_by_id(str(order.person_id))
        order_html += f'<li>{person.name.title()} - {order.drink_name.capitalize()}'
    return order_html

class SiteHandler(BaseHTTPRequestHandler):
    def _set_headers(self, code):
        self.send_response(code)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers(200)
        drinks = drinks_api.get_drinks()
        people = people_api.get_people()
        prefs = preferences_api.get_favourites()
        active_round = rounds_api.get_active_round()
        rounds = rounds_api.get_rounds()
        html_document = f"""
<!doctype html>
<html>
    <body>
        <p>Available drinks:</p>
        <ul>
            {render_drinks(drinks)}
        </ul>
        <p>Registered people:</p>
        <ul>
            {render_people(people)}
        </ul>
        <p>People and their favourite drinks:</p>
        <ul>
            {render_preferences(prefs)}
        </ul>
        <hr/>
        <p>Current round orders:</p>
        <ul>
            {render_orders(active_round)}
        </ul>
        <p>Previous rounds:</p>
        <ul>
            {render_rounds(rounds)}
        </ul>
    </body>
</html>
"""
        self.wfile.write(html_document.encode('utf-8'))

if __name__ == "__main__":
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SiteHandler)
    print("Starting server.")
    httpd.serve_forever()