import unittest
import briw.src.database_drink as drinks_db
import briw.src.database_base as base_db

from briw.src.drink_class import Drink

from unittest.mock import MagicMock, Mock

class Test_Drink_Table_Functions(unittest.TestCase):
    def test1_parse_drink_should_correctly_return_a_Drink_object(self):
        # Arrange
        drink_name = "drink"
        drink_type = "type"
        drink_row = [drink_name, drink_type]
        # Act
        drink: Drink = drinks_db._parse_drink_row(drink_row)
        # Assert
        self.assertEqual(type(drink), Drink)
        self.assertTrue(drink.name == drink_name and drink.type == drink_type)

    @unittest.mock.patch("briw.src.database_base._fetch_table")
    def test2_get_drinks_should_fetch_table(self, fetch_table):
        # Arrange
        fetch_table.return_value = []
        # Act
        drinks_db.get_drinks()
        # Assert
        fetch_table.assert_called_with('drinks')

    @unittest.mock.patch("briw.src.database_base._fetch_table")
    def test3_get_drinks_should_return_list_of_Drink_objects(self, fetch_table):
        # Arrange
        drink_1 = Drink('drink1','type1')
        drink_2 = Drink('drink2','type2')
        fetch_table.return_value = [[drink_1.name,drink_1.type],[drink_2.name,drink_2.type]]
        # Act
        response = drinks_db.get_drinks()
        # Assert
        self.assertEqual(len(response),2)
        self.assertTrue(type(response[0]) == Drink and type(response[1]) == Drink)
        self.assertEqual(response[0].__dict__, drink_1.__dict__)
        self.assertEqual(response[1].__dict__, drink_2.__dict__)

    @unittest.mock.patch("briw.src.database_base._query_database")
    def test4_get_drink_should_return_the_correct_drink(self, query_database):
        # Arrange
        drink = Drink('drink','type')
        query_database.return_value = [[drink.name,drink.type]]
        query = f"SELECT * FROM drinks WHERE drink_name=\"{drink.name}\""
        # Act
        response = drinks_db.get_drink(drink.name)
        # Assert
        self.assertTrue(type(response) == Drink)
        self.assertEqual(response.__dict__, drink.__dict__)
        query_database.assert_called_with(query)

    @unittest.mock.patch("briw.src.database_base._insert_row")
    def test6_add_drink_should_call_the_insert_row_function(self, insert_row):
        # Arrange
        drink = Drink('drink','type')
        query = f"INSERT INTO drinks (drink_name,drink_type) VALUES ('{drink.name}','{drink.type}')"
        # Act
        drinks_db.add_drink(drink)
        # Assert
        insert_row.assert_called_with(query)