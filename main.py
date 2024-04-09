"""
Matthew Gregorio
Daniela Alejandra Gonzalez
Ikonkar Kaur Khalsa
"""

from CSVModule import *
from Counterskills import *
from Visualizationmostrequired import *
from Visualizationmostrequiredcombination import *


# CSV class to load data
csv_handler = CSVLoader("job_skills.csv")
csv_handler.load_data()


# Using the SkillCounter class to count skills and skill combinations
skill_counter = SkillCounter("job_skills.csv")
skill_counts, top_skills, top_combinations = skill_counter.count_skills()
least_required_skills = skill_counter.least_required_skills()

# printing results
print("\nSkills:")
print(skill_counts)
print("\nTop 10 required skills:")
print(top_skills)
print("\nThe 10 least required skills:")
print(least_required_skills)
print("\nTop 10 most common skill combinations:")
print(top_combinations)



# Visualization of the 10 most required skills
wordcloud_generator = WordCloudGenerator(top_skills)
wordcloud_generator.generate_wordcloud()

# Visualization more required combinated skills
skills_visualizer = SkillsVisualizer(top_combinations)
chord_diagram = skills_visualizer.visualize_chord_diagram()
hv.save(chord_diagram, 'chord_diagram.html')







