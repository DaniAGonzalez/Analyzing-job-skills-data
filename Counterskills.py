"""
Matthew Gregorio
Daniela Alejandra Gonzalez
Ikonkar Kaur Khalsa
"""

import pandas as pd
import itertools
from collections import Counter

class SkillCounter:
    """
    Class: SkillCounter. Designed to iterate over the dataframe
    and get information about the
    required skills for Data Science jobs.
    """
    def __init__(self, filename):
        """
        Function - Initialize SkillCounter object
        Parameters - Filename (str): The name of the CSV file containing job skills data
        Returns - None
        """
        self.filename = filename

    def count_skills(self):
        """
        Function - Count the frequency of individual skills and combinations of skills in the dataset.
        Parameters - None
        Returns - skill_counts (dict): Dictionary containing counts of individual skills,
            top_skills (list): List of tuples containing the top 10 most common individual skills,
            top_combinations (list): List of tuples containing the top 10 most common combinations of skills
        """
        # Make dataframe from csv file data
        df = pd.read_csv(self.filename)

        # Find the column containing skills
        skills_column = None
        for col in df.columns:
            if 'skills' in col.lower():
                skills_column = col
                # break # Break the loop if a Column containing Skills is found NOT NECESSARY

        if skills_column is None:
            print("A column skill could not be find. ")
            return {}, [], [] # If a column containing the Skill word can not be found then return empty dictionary
                                # and lists representing skill_counts, top_skills, and top_combinations respectively

        # Extraction of individual skills from the specified column
        all_skills = []
        for skills in df[skills_column]:
            skill_list = [skill.strip() for skill in skills.split(',')]
            all_skills.extend(skill_list)

        # Frequency of each individual skill
        skill_counts = Counter(all_skills)
        skill_counts = {skill: count for skill, count in skill_counts.items() if skill}

        # Get the top 10 most common individual skills
        skill_counter = Counter(skill_counts)
        top_skills = skill_counter.most_common(10)

        # Count the frequency of combinations of skills (order does not matter)
        skill_combinations = Counter()
        for skills in df[skills_column]:
            skill_list = [skill.strip() for skill in skills.split(',')]
            combinations = itertools.combinations(skill_list, 2)
            skill_combinations.update(combinations)

        # Get the top 10 most common combinations of skills
        top_combinations = skill_combinations.most_common(10)

        return skill_counts, top_skills, top_combinations

    def least_required_skills(self):
        """
        Function - Find the 10 least required skills in the dataset.
        Parameters - None
        Returns - least_required_skills (list): List of tuples containing the 10 least required skills and their counts.
        """
        # Get all skills and their counts
        all_skills, _, _ = self.count_skills()

        # Exclude hyperlinks from the skills
        least_required_skills = [(skill, count) for skill, count in all_skills.items()
                                 if "http://" not in skill and "https://" not in skill]

        # Sort the skills by count and get the 10 least required skills
        least_required_skills = sorted(least_required_skills, key=lambda item: item[1])[:10]

        return least_required_skills

# Testing
#skill_counter = SkillCounter('job_skills.csv')
#least_required_skills = skill_counter.least_required_skills()
#result, top_skills, top_combinations = skill_counter.count_skills()

"""print("\n Skills:")
print(result)
print("\nTop 10 required skills:")
print(top_skills)
print("\nThe 10 least required skills:")
print(least_required_skills)
print("\nTop 10 most common skill combinations:")
print(top_combinations)"""