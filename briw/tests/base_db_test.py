import unittest
import briw.src.database_base as db


test_table_name = 'test'
test_table_field = 'test_field'

def create_test_table():
    db._query_database("CREATE TABLE "+test_table_name+" ( "+test_table_field+" VARCHAR(100) );")

def delete_test_table():
    db._query_database(f"DROP TABLE {test_table_name};")

class Test_Basic_Database_Functions(unittest.TestCase):
    def test1_connecting_to_database_does_not_cause_exception(self):
        # Arrange
        exception_raised = False
        # Act
        try:
            database = db._connect_to_database()
        except:
            exception_raised = True
        # Assert
        self.assertFalse(exception_raised)
        if database:
            database.close()

    def test2_closing_the_database_does_not_cause_exception(self):
        # Arrange
        exception_raised = False
        database = db._connect_to_database()
        # Act
        try:
            db._close_database(database)
        except:
            exception_raised = True
        # Assert
        self.assertFalse(exception_raised)
        if exception_raised == True:
            database.close()

    def test3_querying_the_database_does_not_cause_exception(self):
        # Arrange
        exception_raised = False
        database = db._connect_to_database()
        # Act
        try:
            db._query_database('show tables;')
        except:
            exception_raised = True
        # Assert
        self.assertFalse(exception_raised)
        database.close()

    def test4_fetching_a_table_in_the_database_does_not_cause_exception(self):
        # Arrange
        exception_raised = False
        database = db._connect_to_database()
        create_test_table()
        # Act
        try:
            db._fetch_table(test_table_name)
        except:
            exception_raised = True
        # Assert
        self.assertFalse(exception_raised)
        delete_test_table()
        database.close()

    def test5_adding_an_entry_to_a_table_in_the_database_does_not_cause_exception(self):
        # Arrange
        exception_raised = False
        database = db._connect_to_database()
        create_test_table()
        # Act
        try:
            db._insert_row(f'INSERT INTO {test_table_name} ({test_table_field}) VALUES ("test")')
        except:
            exception_raised = True
        # Assert
        self.assertFalse(exception_raised)
        delete_test_table()
        database.close()

    def test6_fetching_a_table_with_an_entry_in_the_database_returns_correct_value(self):
        # Arrange
        database = db._connect_to_database()
        create_test_table()
        test_value = 'hello'
        db._insert_row(f'INSERT INTO {test_table_name} ({test_table_field}) VALUES ("{test_value}")')
        # Act
        try:
            table = db._fetch_table(test_table_name)
        except:
            print('error fetching table')
            self.assertFalse(True)
        # Assert
        self.assertTrue(len(table) == 1 and table[0][0] == test_value)
        delete_test_table()
        database.close()

    

