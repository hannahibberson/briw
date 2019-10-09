from briw.json_helper import MyEncoder
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

from briw import people_api, drinks_api, rounds_api, preferences_api

class PersonHandler(BaseHTTPRequestHandler):
    def _set_headers(self, code):
        self.send_response(code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers(200)
        path_values = self.path.split('?')
        command = path_values[0]
        response = self.help_output
        if 'people' in command:
            response = people_api.get_people()
        elif 'person' in command:
            if len(path_values) == 1:
                print("No query given")
            else:
                response = people_api.parse_people_query(path_values[1])
        elif 'drinks' in command:
            response = drinks_api.get_drinks()
        elif 'drink' in command:
            response = drinks_api.get_drink(path_values[1])
        elif 'rounds' in command:
            response = rounds_api.get_rounds()
        elif 'active-round' in command:
            response = rounds_api.get_active_round()
        elif 'favourites' in command:
            response = preferences_api.get_favourites()
        elif 'favourite' in command:
            try:
                response = preferences_api.get_favourite(path_values[1])
            except:
                print("This person has no favourite drink.")
        else:
            print(f"Error with command: {command}")
        self._json_parse_and_output(response)


    def do_POST(self):
        data = self._read_input_data()

        path_values = self.path.split('?')
        command = path_values[0]
        if 'person' in command:
            people_api.add_person(data)
        elif 'drink' in command:
            drinks_api.add_drink(data)
        elif 'round/start' in command:
            rounds_api.add_round(data)
        elif 'round/join' in command:
            try:
                rounds_api.add_order_to_round(data)
            except:
                print("No active round.")
        elif 'round/stop' in command:
            rounds_api.stop_round()
        elif 'favourite' in command:
            preferences_api.change_favourite(data)
        self._set_headers(201)

    def _json_parse_and_output(self, encoded_item):
        jd = json.dumps(encoded_item, cls=MyEncoder)
        self.wfile.write(jd.encode('utf-8'))

    def _read_input_data(self):
        content_len = self.headers['Content-Length']
        if content_len != None:
            raw_data = self.rfile.read(int(content_len))
            return json.loads(raw_data)
        else:
            return None

    help_output = {
        'get': '/people, /person?id=x, /person?firstname&surname&slackid, /drinks, /drink?drinkname, /favourites, /favourite?personid, /rounds, /active-round',
        'post': '/person (first_name, surname, slack_id), /drink (drink_name, drink_type), /favourite (person_id, drink_name), /round/start (owner_id), /round/join (person_id), /round/stop'
    }

if __name__ == "__main__":
    server_address = ('0.0.0.0', 8000)
    my_server = HTTPServer(server_address, PersonHandler)
    print("Starting server.")

    my_server.serve_forever()