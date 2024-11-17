import unittest
from Wheel import Wheel

class TestWheel(unittest.TestCase):
    def setUp(self):
        self.predefined_choices = ["Option1", "Option2", "Option3"]
        self.custom_choices = ["Custom1", "Custom2"]
        self.wheel = Wheel(self.predefined_choices, self.custom_choices)
    
    def test_all_choices(self):
        self.assertEqual(
            # Query to see al choices
            self.wheel.all_choices,
            # Check to see if they match
            self.predefined_choices + self.custom_choices
        )
    
    def test_add_choices(self):
        # Add A test value to the list
        self.wheel.add_choice("Custom3")
        # Check to see if the value was added
        self.assertIn("Custom3", self.wheel.custom_choices)

    def test_add_duplicate_choice(self):
        # Add a duplicate choice
        self.wheel.add_choice("Custom1")
        # Check to see if it was added
        self.assertEqual("Custom1", self.wheel.custom_choices)
    
    def test_remove_choice(self):
        # Remove a choice
        self.wheel.remove_choice("Custom1")
        # Check to see if it was deleted
        self.assertNotIn("Custom1", self.wheel.custom_choices)
    
    def remove_nonexistent_choice(self):
        # Read initial length of choices list
        initial_length = len(self.wheel.custom_choices)
        # Remove nonexistant choice
        self.wheel.remove_choice("NonExistant")
        # Check to see if anything was removed
        self.assertEqual(len(self.wheel.custom_choices), initial_length)
    
    def test_spin_with_choices(self):
        # Spin wheel
        result = self.wheel.spin()
        # Check to see if all choices are there
        self.assertIn(result, self.wheel.all_choices)
    
    def test_spin_with_no_choices(self):
        empty_wheel = Wheel([], [])
        self.assertEqual(empty_wheel.spin(), "No Choices Avaialable!")

if __name__ == "__main__":
    unittest.main()
