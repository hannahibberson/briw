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
