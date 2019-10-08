from flask import Flask, jsonify, render_template, request, redirect, url_for

import json

from src.helpers.person_class import Person
import people_api, drinks_api, preferences_api, rounds_api

app = Flask(__name__)

def valid_slack_id (string):
    if string.isdigit() or '/' in string or '\\' in string or '"' in string or '\'' in string or ';' in string:
        return False
    else:
        return True

def is_letter (c):
    return c.lower() != c.upper()

def valid_string (string):
    valid = True
    for character in string:
        valid = is_letter(character) or character == '-'
    return valid

def check_input (string, validation_fn):
    length = len(string)
    print(validation_fn(string))
    if validation_fn(string) == False or length > 100:
        return False
    else:
        return True

### GETS ###

@app.route('/', methods=['GET','POST'])
def login_page():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        first_name = request.form.get("first_name").lower()
        surname = request.form.get("surname").lower()
        slack_id = request.form.get("slack_id").lower()
        strings = [
                {'string': first_name, 'type': 'name'},
                {'string': surname, 'type': 'name'},
                {'string': slack_id, 'type': 'slackID'}
            ]
        valid = True
        for string in strings:
            validation_fn = valid_slack_id
            if string["type"]== 'name':
                validation_fn = valid_string
            is_valid = check_input(string["string"], validation_fn)
            if is_valid == False:
                valid = False
        print(valid)
        if valid == True:
            query_string = first_name + '&' + surname + '&' + slack_id
            person = people_api.get_person_by_names(query_string)
            if person:
                return redirect(f"/home/{person.person_id}")
            else:
                return redirect(f"/register/{first_name}/{surname}/{slack_id}")
        else:
            return ('', 204)

@app.route('/home')
def invalid_home_page():
    return redirect("/")

@app.route('/home/<person_id>', methods=['GET', 'POST'])
def home_page(person_id):
    if request.method == 'GET':
        person = people_api.get_person_by_id(person_id)
        favourite = preferences_api.get_favourite(person_id)
        if favourite:
            favourite = favourite.title()
        if person:
            return render_template('home.html', person=person, favourite=favourite)
        else:
            return redirect("/")

    elif request.method == "POST":
        button_value = request.form['submit_button']
        if button_value == 'End the round':
            round_ = rounds_api.get_active_round()
            rounds_api.stop_round()
            return redirect(f'/round-orders/{round_.id}')
        elif button_value == 'Start a round':
            rounds_api.add_round({'owner_id':person_id})
            return redirect(f"/home/{person_id}")
        elif button_value == 'Edit drink preference':
            return redirect(f"/preference/{person_id}")
        elif 'Join' in button_value:
            rounds_api.add_order_to_round({'person_id':person_id})
            return redirect(f'/home/{person_id}/joined-round')

@app.route('/register/<first_name>/<surname>/<slack_id>', methods=['GET','POST'])
def register_page(first_name, surname, slack_id):
    if request.method == 'GET':
        return render_template('register.html', first_name=first_name, surname=surname, slack_id=slack_id)
    elif request.method == 'POST':
        if request.form['submit_button'] == 'Register':
            people_api.add_person({"first_name":first_name,"surname":surname,"slack_id":slack_id})
            person = people_api.get_person_by_names(first_name+'&'+surname+'&'+slack_id)
            return redirect(f"/home/{person.person_id}")
        elif request.form['submit_button'] == 'Cancel':
            return redirect("/")

@app.route('/round-orders/<round_id>')
def round_orders_page(round_id):
    round_ = rounds_api.get_round(round_id)
    orders = {}
    for order in round_.orders:
        drink = order.drink_name
        if not drink in orders.keys():
            orders[drink] = {}
            orders[drink]['people'] = []
            orders[drink]['count'] = 0
        order_person = people_api.get_person_by_id(str(order.person_id))
        orders[drink]['people'].append(order_person.name)
        orders[drink]['count'] += 1
    return render_template('orders.html',orders=orders,person_id=round_.owner_id)

@app.route('/home/<person_id>/joined-round')
def joined_round_page(person_id):
    return render_template('join-confirmation.html',person_id=person_id)

@app.route('/preference/<person_id>', methods=['GET','POST'])
def edit_preference(person_id):
    if request.method == 'GET':
        drinks = drinks_api.get_drinks()
        drink_names = [drink.name for drink in drinks]
        return render_template('preference.html', drinks=json.dumps(drink_names))
    else:
        if request.form['submit_button'] == 'Confirm Drink Choice':
            drink_name = request.form.get("drink_form_entry").lower()
            valid_drink = check_input(drink_name, valid_string)
            if valid_drink:
                drink = drinks_api.get_drink(drink_name)
                if not drink:
                    drinks_api.add_drink({"drink_name":drink_name})
                preferences_api.change_favourite({"person_id":person_id,"drink_name":drink_name})
                return redirect(f'/home/{person_id}')
            else:
                return('',204)
        else:
            return redirect(f'/home/{person_id}')

@app.route('/people')
def get_people():
    people = people_api.get_people()
    people_dict = [person.__dict__ for person in people]
    return jsonify(people_dict)

@app.route('/person')
def get_person_by_id():
    args = request.args
    if 'id' in args:
        user_id = args.get('id')
        person = people_api.get_person_by_id(user_id)
        if person:
            return jsonify(person.__dict__)
        else:
            return jsonify({'error':'no person found.'})
    elif ('first_name' in args) and ('surname' in args) and ('slack_id' in args):
        first_name = args.get('first_name')
        surname = args.get('surname')
        slack_id = args.get('slack_id')
        query_string = first_name + '&' + surname + '&' + slack_id
        person = people_api.get_person_by_names(query_string)
        if person:
            return jsonify(person.__dict__)
        else:
            return jsonify({'error':'no person found.'})
    else:
        return jsonify({'error':'please provide an id=number or first_name=name&surname=name&slack_id=id'})

@app.route('/drinks')
def get_drinks():
    drinks = drinks_api.get_drinks()
    return jsonify([drink.__dict__ for drink in drinks])

@app.route('/drink/<name>')
def get_drink(name):
    drink = drinks_api.get_drink(name)
    if drink:
        return jsonify(drink.__dict__)
    else:
        return jsonify({'error':'no drink found.'})

@app.route('/favourites')
def get_favourites():
    favourites = preferences_api.get_favourites()
    return jsonify(favourites)

@app.route('/favourite/<person_id>')
def get_favourite(person_id):
    drink_name = preferences_api.get_favourite(person_id)
    if drink_name:
        return jsonify({person_id:drink_name})
    else:
        return jsonify({'error':'no favourite for this person found.'})

@app.route('/rounds')
def get_rounds():
    rounds = rounds_api.get_rounds()
    rounds_dict = []
    for round_ in rounds:
        round_.orders = [o.__dict__ for o in round_.orders]
        rounds_dict.append(round_.__dict__)
    return jsonify([r for r in rounds_dict])

@app.route('/active-round')
def get_active_round():
    round_ = rounds_api.get_active_round()
    round_.orders = [o.__dict__ for o in round_.orders]
    return jsonify(round_.__dict__)

@app.route('/start-round/<person_id>', methods=['POST'])
def start_round(person_id):
    rounds_api.add_round({'owner_id':person_id})

@app.route('/end-round', methods=['POST'])
def end_round():
    round_ = rounds_api.get_active_round()
    rounds_api.stop_round()
    return redirect(f'/round-orders/{round_.id}')

@app.route('/join-round/<person_id>', methods=['POST'])
def join_round(person_id):
    rounds_api.add_order_to_round({'person_id':person_id})
    return redirect(f'/home/{person_id}/joined-round')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)