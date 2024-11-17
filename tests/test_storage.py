import unittest
import os
import json
from Storage import load_choces, save_choices

class TestStorage(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_choices.json"
        self.sample_choices = ["test1", "test2"]
    
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_load_choices_with_existing_file(self):
        with open(self.test_file, "w") as file:
            json.dump(self.sample_choices, file)
        loaded_choices = load_choces(self.test_file)
        self.assertEqual(loaded_choices, self.sample_choices)
    
    def test_load_choices_with_nonexisting_file(self):
        loaded_choices = load_choces(self.test_file)
        self.assertEqual(loaded_choices, [])

    def test_save_choices(self):
        save_choices(self.test_file, self.sample_choices)
        with open(self.test_file, "r") as file:
            data = json.load(file)
        self.assertEqual(data, self.sample_choices)

if __name__ == "__main__":
    unittest.main()
