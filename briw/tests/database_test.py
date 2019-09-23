import unittest
import briw.src.helpers.database as db

class Test_Database_Connections(unittest.TestCase):
    def test_connecting_to_database_does_not_cause_exception(self):
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

    def test_closing_the_database_does_not_cause_exception(self):
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

    def test_fetching_people_table_does_not_cause_exception(self):
        # Arrange
        exception_raised = False
        # Act
        try:
            db._fetch_table('people')
        except:
            exception_raised == True
        # Assert
        self.assertFalse(exception_raised)

