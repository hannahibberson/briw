from flask import Flask, jsonify, render_template, request, redirect, url_for

import people_api, drinks_api, preferences_api, rounds_api

app = Flask(__name__)

### GETS ###

@app.route('/', methods=['GET','POST'])
def login_page():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        first_name = request.form.get("first_name").lower()
        surname = request.form.get("surname").lower()
        slack_id = request.form.get("slack_id").lower()
        values = [first_name, surname, slack_id]
        for string in values:
            if string.isdigit() or '/' in string or '\\' in string or ';' in string or '\'' in string or '"' in string or len(string) > 100:
                return ('', 204)
        query_string = first_name + '&' + surname + '&' + slack_id
        person = people_api.get_person_by_names(query_string)
        if person:
            return redirect(f"/home/{person.person_id}")
        else:
            # Ask if they want to register
            return redirect(f"/register/{first_name}/{surname}/{slack_id}")

@app.route('/home')
def invalid_home_page():
    return redirect("/")

@app.route('/home/<person_id>', methods=['GET','POST'])
def home_page(person_id):
    person = people_api.get_person_by_id(person_id)
    favourite = preferences_api.get_favourite(person_id)
    active_round = rounds_api.get_active_round()
    if person:
        return render_template('home.html', person=person, favourite=favourite, active_round=active_round)
    else:
        return redirect("/")

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

@app.route('/helloworld')
def hello_world():
    return redirect("/people")

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
    rounds_api.stop_round()

@app.route('/join-round/<person_id>', methods=['POST'])
def join_round(person_id):
    rounds_api.add_order_to_round({'person_id':person_id})


if __name__ == "__main__":
    app.run(host='localhost', port=8000)