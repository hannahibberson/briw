import unittest
import briw.src.database_person as person_db
import briw.src.database_base as base_db

from briw.src.person_class import Person

from unittest.mock import MagicMock, Mock

class Test_People_Table_Functions(unittest.TestCase):
    def test1_parse_person_should_correctly_return_a_Person_object(self):
        # Arrange
        person_id = 0
        first_name = "tester"
        surname = "mcgee"
        slack_id = "t_m"
        person_row = [person_id, first_name, surname, slack_id]
        # Act
        person: Person = person_db._parse_person_row(person_row)
        # Assert
        self.assertEqual(type(person), Person)
        self.assertTrue(person.person_id == person_id and person.first_name == first_name and person.surname == surname and person.slack_id == slack_id)

    @unittest.mock.patch("briw.src.database_base._fetch_table")
    def test2_get_people_should_fetch_table(self, fetch_table):
        # Arrange
        fetch_table.return_value = []
        # Act
        person_db.get_people()
        # Assert
        fetch_table.assert_called_with('people')

    @unittest.mock.patch("briw.src.database_base._fetch_table")
    def test3_get_people_should_return_list_of_Person_objects(self, fetch_table):
        # Arrange
        person_1_data = [1,'tester','one','test1']
        person_2_data = [2,'tester','two','test2']
        fetch_table.return_value = [person_1_data,person_2_data]
        person_1 = Person(person_1_data[1],person_1_data[2],person_1_data[3],person_1_data[0])
        person_2 = Person(person_2_data[1],person_2_data[2],person_2_data[3],person_2_data[0])
        # Act
        response = person_db.get_people()
        # Assert
        self.assertEqual(len(response),2)
        self.assertTrue(type(response[0]) == Person and type(response[1]) == Person)
        self.assertEqual(response[0].__dict__, person_1.__dict__)
        self.assertEqual(response[1].__dict__, person_2.__dict__)

    @unittest.mock.patch("briw.src.database_base._query_database")
    def test4_get_person_by_id_should_return_the_correct_person(self, query_database):
        # Arrange
        person_data = [1,'tester','one','test1']
        query_database.return_value = [person_data]
        person = Person(person_data[1],person_data[2],person_data[3],person_data[0])
        query = "SELECT * FROM people WHERE person_id = "+str(person_data[0])
        # Act
        response = person_db.get_person_by_id(person_data[0])
        # Assert
        self.assertTrue(type(response) == Person)
        self.assertEqual(response.__dict__, person.__dict__)
        query_database.assert_called_with(query)

    @unittest.mock.patch("briw.src.database_base._query_database")
    def test5_get_person_by_names_should_return_the_correct_person(self, query_database):
        # Arrange
        person_id = 1
        first_name = 'tester'
        surname = 'one'
        slack_id = 'test1'
        query_database.return_value = [[person_id,first_name,surname,slack_id]]
        person = Person(first_name,surname,slack_id,person_id)
        query = f'SELECT * FROM people WHERE first_name="{first_name}" AND surname="{surname}" AND slack_id="{slack_id}"'
        # Act
        response = person_db.get_person_by_names(first_name,surname,slack_id)
        # Assert
        self.assertTrue(type(response) == Person)
        self.assertEqual(response.person_id, person_id)
        self.assertEqual(response.__dict__, person.__dict__)
        query_database.assert_called_with(query)

    @unittest.mock.patch("briw.src.database_base._insert_row")
    def test6_add_person_should_call_the_insert_row_function(self, insert_row):
        # Arrange
        person = Person('tester','one','test1')
        query = f"INSERT INTO people (first_name, surname, slack_id) VALUES ('{person.first_name}','{person.surname}','{person.slack_id}')"
        # Act
        person_db.add_person(person)
        # Assert
        insert_row.assert_called_with(query)