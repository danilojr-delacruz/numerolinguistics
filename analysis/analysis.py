import re
import networkx as nx


from functools import cached_property
from collections import defaultdict


DATA_DIR = "../../data"


class Analyse:
    def __init__(self, language):
        # Assume that 
        # TODO: Allow for a threshold for numbers to consider.
        with open(f"{DATA_DIR}/{language}.txt", "r") as f:
            self.numbers = f.read().splitlines()
            # Remove any special characters
            self.clean_numbers = [
                re.sub(r"-|\ |'", "", number) for number in self.numbers
                ]

    @cached_property
    def lengths(self):
        """Return length of numbers below given threshold."""
        return [len(number) for number in self.clean_numbers]

    def average_length(self, threshold):
        """Return length of numbers below a given threshold."""
        # TODO: Check if this index is correct.
        lengths = self.lengths[:min(len(self.clean_numbers), threshold)]
        return sum(lengths) / len(lengths)

    @cached_property
    def graph(self):
        G = nx.DiGraph([
            (self.numbers[i], self.numbers[self.lengths[i]])
            for i in range(100 + 1)])
        return G

    @cached_property
    def degree(self):
        return dict(self.graph.degree)

    @cached_property
    def fixed_points(self):
        return [number for number in self.numbers 
        if (number in self.graph[number])]
