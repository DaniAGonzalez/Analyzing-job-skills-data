"""
Matthew Gregorio
Daniela Alejandra Gonzalez
Ikonkar Kaur Khalsa
"""


import unittest
from CSVModule import CSVLoader
from Counterskills import SkillCounter


# Test class for CSV module
class TestCSVLoader(unittest.TestCase):

    def setUp(self):
        self.csv_loader = CSVLoader("job_skills_test.csv")

    def test_load_data_success(self):
        self.csv_loader.load_data()
        # Checking if the number of lines is equal to 50
        self.assertEqual(len(self.csv_loader.data), 50)

    def test_load_empty_file(self):
        self.csv_loader.filename = "job_skillsempty.csv"
        self.csv_loader.load_data()
        # Checking if the list is empty
        self.assertEqual(len(self.csv_loader.data), 0)


# Test class created for skills counter
class TestSkillCounter(unittest.TestCase):

    def setUp(self):
        self.skill_counter = SkillCounter("job_skills_test.csv")

    def test_count_skills(self):
        result, _, _ = self.skill_counter.count_skills()
        # Verifying that the result is indeed an empty dict
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
