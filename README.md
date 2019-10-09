# briw
Tea and coffee and other drinks.

Please note: This is a mass of code, most of which is no longer of any use. Proceed with caution!

### To run the program
You will need to create the file `_db_connect.py` within the `briw/src` directory, and fill in the necessary information in the following format:

```
_host = <host>
_username = <username>
_password = <password>
_database = <database-name>
```

You will also need to create `_slack_webhook.py` in the `briw/src` directory, and fill in the url field with the slack webhook:

```
url = '<slack-url'
```

In the root directory run:

```pip3 install -r requirements.txt```

```python3 flask_handler.py```

Navigate to `localhost:8000` and you'll be greeted with a login page. Once you've logged in (and possibly registered), you will be able to add your favourite drink, then start new rounds with your friends and colleagues.

### Contributing
Please contribute, it's fun! Just submit a pull-request and I'll have a look. Just __beware__, everything is a bit crazy and unorganised.

### How it works
I have used flask for this project, and all of this logic is held in `flask_handler.py`. It handles the GET and POST requests to the different pages in the site.

From here, it calls out to the `*_api.py` files, which manage the logic for each of the key functions of the site.

The API files manage database accessing, so that your people, drinks, and rounds can be stored in a database. The `database_*.py` files are where you can find the database logic.

### Run the tests

The tests use unittest, but can also be run with pytest. We can also get the coverage of the tests over the `src` directory using:

```
$ coverage run --source=briw/src --omit=briw/src/__*,briw/src/_* -m pytest

$ coverage report -m
```

An example coverage report:

```
Name                              Stmts   Miss  Cover   Missing
---------------------------------------------------------------
briw/src/database_base.py            24      0   100%
briw/src/database_drink.py           33     33     0%   1-39
briw/src/database_order.py           30     30     0%   1-34
briw/src/database_person.py          46     25    46%   5-8, 25-26, 30-39, 42-51, 54
briw/src/database_preference.py      37     37     0%   1-44
briw/src/database_round.py           46     46     0%   1-54
briw/src/drink_class.py               4      4     0%   1-4
briw/src/drinks_api.py               11     11     0%   1-15
briw/src/json_helper.py               7      7     0%   1-8
briw/src/order_class.py               6      6     0%   1-6
briw/src/people_api.py               22     22     0%   1-29
briw/src/person_class.py              7      0   100%
briw/src/preferences_api.py          11     11     0%   1-15
briw/src/round_class.py               6      6     0%   1-6
briw/src/round_hander.py             15     15     0%   1-20
briw/src/rounds_api.py               22     22     0%   1-28
---------------------------------------------------------------
TOTAL                               327    275    16%
```
