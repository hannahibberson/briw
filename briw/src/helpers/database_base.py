import pymysql
import src.helpers._db_connect as db
from os import environ

def _connect_to_database():
    my_database = pymysql.connect(
        db._host,
        db._username,
        db._password,
        db._database
    )
    return my_database

def _close_database(database):
    database.close()

def _query_database(query: str, returns_result: bool = True):
    db = _connect_to_database()
    cursor = db.cursor()
    cursor.execute(query)
    if returns_result == True:
        results = cursor.fetchall()
        print(results)
    else:
        db.commit()
    db.close()
    if returns_result == True:
        return results

def _fetch_table(table_name: str):
    query = "SELECT * FROM " + table_name
    results = _query_database(query)
    return results

def _insert_row(query: str):
    _query_database(query, False)