import unittest
from briw.src.helpers.user_input import *

class Test_Methods(unittest.TestCase):
    def condition_check(self, value):
        if int(value) == 0:
            return True
        else: 
            print(f"### {value} is not a valid input. ###")
            return False
    def test_input_is_returned_when_passing_a_correct_input(self):
        # Arrange
        def get_input(message):
            return 0
        expected_value = 0
        # Act
        actual_value = user_input(self.condition_check, "", get_input)
        # Assert
        self.assertEqual(actual_value, expected_value)

    iterator = 2
    def get_incorrect_input(self, message):
        self.iterator -= 1
        return self.iterator
    def test_if_the_input_is_incorrect_the_user_will_be_asked_for_input_until_it_meets_the_conditions(self):
        # Arrange
        expected_value = 0 
        # Act
        user_input(self.condition_check, "", self.get_incorrect_input)
        # Assert
        self.assertEqual(self.iterator, expected_value)

    def test_if_the_validation_function_does_not_account_for_an_input_an_exception_will_be_raised(self):
        # Arrange
        def get_input(message):
            return "hello"
        expected_message = "The validation function was unable to process the given user input. Please add a way to process user inputs such as \"hello\"."
        # Act
        with self.assertRaises(Exception) as exception:
            user_input(self.condition_check, "", get_input)
        # Assert
        actual_message = str(exception.exception)
        self.assertEqual(actual_message, expected_message)
        


