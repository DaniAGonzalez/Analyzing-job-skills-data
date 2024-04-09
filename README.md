# Project-DS5010

Description: This repository contains classes and methods for analyzing job skills data contained in a CSV file and visualizing the findings. The main classes and their functionalities are outlined below:
1.	SkillCounter: • Functionality: Counts the frequency of individual skills and combinations of skills in a dataset. • Methods: a) count_skills(): Counts skills and skill combinations. b) least_required_skills(): Identifies the least required skills.
2.	CSVLoader: • Functionality: Loads data from a CSV file and provides methods to display information. • Methods: a) load_data(): Loads data from a CSV file. b) display_data(n=5): Displays the first n rows of loaded data. c) tail_data(n=5): Displays the last n rows of loaded data. d) info(): Displays information about the loaded data.
3.	WordCloudGenerator: • Functionality: Generates a word cloud from the top required skills. • Methods: a) generate_wordcloud(): Generates a word cloud plot.
4.	SkillsVisualizer: • Functionality: Visualizes skill combinations using a chord diagram. • Methods: a) visualize_chord_diagram(): Visualizes skill combinations. Usage:
5.	Setup: • Ensure Python and necessary libraries are installed (pandas, matplotlib, wordcloud, holoviews). • Place the CSV file containing job skills data in the repository directory.
6.	Instructions: • Instantiate SkillCounter with the filename. • Call count_skills() and least_required_skills() methods. • Instantiate WordCloudGenerator and SkillsVisualizer for visualization. • Run the main script to see results and visualizations.
7.	Examples: Refer to the examples provided in the source code files for usage demonstrations.
8.	Contributions: Contributions are welcome! Feel free to submit pull requests or report issues on GitHub.
9. Credits: Gregorio, Matthew. Gonzalez, Daniela Alejandra. khalsa Kaur Ikonkar
10. Project Status: This project is actively maintained and open to contributions.
