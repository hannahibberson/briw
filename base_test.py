import unittest
import testfile
import random

class Test_Methods(unittest.TestCase):
    def condition_check(self, value):
        if int(value) == 0:
            return True
        else: 
            print(f"### {value} is not a valid input. ###")
            return False
    def test_correct_input(self):
        # Arrange
        def get_input(message):
            return 0
        expected_value = 0
        # Act
        actual_value = testfile.user_input(self.condition_check, "", get_input)
        # Assert
        self.assertEqual(actual_value, expected_value)

    iterator = 2
    def get_incorrect_input(self, message):
        self.iterator -= 1
        return self.iterator
    def test_incorrect_input(self):
        # Arrange
        expected_value = 0 
        # Act
        actual_value = testfile.user_input(self.condition_check, "", self.get_incorrect_input)
        # Assert
        self.assertEqual(actual_value, expected_value)

    def test_unchecked_incorrect_input(self):
        # Arrange
        def get_input(message):
            return "hello"
        expected_message = "The validation function was unable to process the given user input. Please add a way to process user inputs such as \"hello\"."
        # Act
        with self.assertRaises(Exception) as exception:
            testfile.user_input(self.condition_check, "", get_input)
        # Assert
        actual_message = str(exception.exception)
        self.assertEqual(actual_message, expected_message)
        


