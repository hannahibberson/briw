import unittest
import briw.src.database_base as db

class Test_Database_Correctly_Configured(unittest.TestCase):
    def test1_database_should_have_5_tables(self):
        # Arrange
        database = db._connect_to_database()
        # Act
        response = db._query_database('show tables;')
        # Assert
        self.assertEqual(len(response),5)
        db._close_database(database)

    def test2_fetching_people_table_should_not_cause_exception(self):
        # Arrange
        database = db._connect_to_database()
        exception_raised = False
        # Act
        try:
            db._fetch_table('people')
        except:
            exception_raised = True
        # Assert
        self.assertFalse(exception_raised)
        db._close_database(database)

    def test3_people_table_should_have_correct_columns(self):
        # Arrange
        database = db._connect_to_database()
        passed = True
        # Act
        response = db._query_database('describe people;')
        # Assert
        if response[0] != ('person_id','int(11)','NO','PRI',None,'auto_increment'):
            passed = False
        if response[1] != ('first_name','varchar(100)','YES','',None,''):
            passed = False
        if response[2] != ('surname','varchar(100)','YES','',None,''):
            passed = False
        if response[3] != ('slack_id','varchar(100)','YES','',None,''):
            passed = False
        self.assertTrue(passed)
        db._close_database(database)

    def test4_fetching_drinks_table_should_not_cause_exception(self):
        # Arrange
        database = db._connect_to_database()
        exception_raised = False
        # Act
        try:
            db._fetch_table('drinks')
        except:
            exception_raised = True
        # Assert
        self.assertFalse(exception_raised)
        db._close_database(database)

    def test5_drinks_table_should_have_correct_columns(self):
        # Arrange
        database = db._connect_to_database()
        passed = True
        # Act
        response = db._query_database('describe drinks;')
        # Assert
        if response[0] != ('drink_name','varchar(100)','NO','PRI',None,''):
            passed = False
        if response[1] != ('drink_type','varchar(100)','YES','',None,''):
            passed = False
        self.assertTrue(passed)
        db._close_database(database)

    def test6_fetching_rounds_table_should_not_cause_exception(self):
        # Arrange
        database = db._connect_to_database()
        exception_raised = False
        # Act
        try:
            db._fetch_table('rounds')
        except:
            exception_raised = True
        # Assert
        self.assertFalse(exception_raised)
        db._close_database(database)

    def test7_rounds_table_should_have_correct_columns(self):
        # Arrange
        database = db._connect_to_database()
        passed = True
        # Act
        response = db._query_database('describe rounds;')
        # Assert
        if response[0] != ('round_id','int(11)','NO','PRI',None,'auto_increment'):
            passed = False
        if response[1] != ('owner_id','int(11)','YES','MUL',None,''):
            passed = False
        if response[2] != ('active','tinyint(1)','YES','','1',''):
            passed = False
        self.assertTrue(passed)
        db._close_database(database)

    def test8_fetching_orders_table_should_not_cause_exception(self):
        # Arrange
        database = db._connect_to_database()
        exception_raised = False
        # Act
        try:
            db._fetch_table('orders')
        except:
            exception_raised = True
        # Assert
        self.assertFalse(exception_raised)
        db._close_database(database)

    def test8_orders_table_should_have_correct_columns(self):
        # Arrange
        database = db._connect_to_database()
        passed = True
        # Act
        response = db._query_database('describe orders;')
        # Assert
        if response[0] != ('order_id','int(11)','NO','PRI',None,'auto_increment'):
            passed = False
        if response[1] != ('person_id','int(11)','YES','MUL',None,''):
            passed = False
        if response[2] != ('drink_name','varchar(100)','YES','MUL',None,''):
            passed = False
        if response[3] != ('round_id','int(11)','YES','MUL',None,''):
            passed = False
        self.assertTrue(passed)
        db._close_database(database)

    def test9_fetching_preferences_table_should_not_cause_exception(self):
        # Arrange
        database = db._connect_to_database()
        exception_raised = False
        # Act
        try:
            db._fetch_table('preferences')
        except:
            exception_raised = True
        # Assert
        self.assertFalse(exception_raised)
        db._close_database(database)

    def test10_preferences_table_should_have_correct_columns(self):
        # Arrange
        database = db._connect_to_database()
        passed = True
        # Act
        response = db._query_database('describe preferences;')
        # Assert
        if response[0] != ('person_id','int(11)','NO','PRI',None,''):
            passed = False
        if response[1] != ('drink_name','varchar(100)','YES','MUL',None,''):
            passed = False
        self.assertTrue(passed)
        db._close_database(database)