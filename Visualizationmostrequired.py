"""
Matthew Gregorio
Daniela Alejandra Gonzalez
Ikonkar Kaur Khalsa
"""


from wordcloud import WordCloud
import matplotlib.pyplot as plt

class WordCloudGenerator:
    """
    Class: WordCloudGenerator. Designed to generate a word cloud from a list
           of the 10 most required skills.
    """
    def __init__(self, skills):
        """
        function: Initialize the WordCloudGenerator object.
        param: skills (list): List of tuples containing the top 10 most common
                              skills and their counts.
        """
        self.skills = dict(skills)

    def generate_wordcloud(self):
        """
        function: Generate a word cloud from the top 10 most required skills.
        returns: Displays the generated world cloud plot.
        """
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(self.skills)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()




