"""
Matthew Gregorio
Daniela Alejandra Gonzalez
Ikonkar Kaur Khalsa
"""
import pandas as pd
import holoviews as hv
from holoviews import opts

hv.extension('bokeh')

class SkillsVisualizer:
    """
    function: This class is designed to visualize skills combinations using a chord diagram.
    """
    def __init__(self, top_combinations):
        """
        function: This method initializes a SkillsVisualizer object with the provided list of top skill combinations.
        param: top_combinations (list): A list of tuples containing the top skill combinations and their counts.
               Each tuple should have the skill combination as the first element and its count as the second element.

        """
        self.top_combinations = top_combinations

    def visualize_chord_diagram(self):
        """
        function: Visualizes the skill combinations using a chord diagram. It will
                  extract the target skills along with their counts from the top_combinations
                  attribute.
        returns: chord (hv.Chord): A chord diagram object representing the skills
                                   the visualization of skill combinations.

        """
        # Extraction of the source and target skills and their counting
        source = [x[0][0] for x in self.top_combinations]
        target = [x[0][1] for x in self.top_combinations]
        value = [x[1] for x in self.top_combinations]

        # Dataframe creation
        links_df = pd.DataFrame({'source': source, 'target': target, 'value': value})

        # Chord diagram creation with the previous dataframe created
        chord = hv.Chord(links_df)

        # Stablishing chords settings
        chord.opts(
            opts.Chord(cmap='Category20', edge_cmap='Category20', edge_color=hv.dim('source').str(),
                       labels='index', node_color=hv.dim('index').str())
        )

        # Return the chord diagram object
        return chord

