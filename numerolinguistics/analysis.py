import re
import networkx as nx


from functools import cached_property
from numerolinguistics.data import *


DATA_DIR = "../data/raw_data"
# Remember to escape if it's a special character (Regex)
BLACKLIST = ["-", "\ ", "'"]


def clean(number):
    """Remove blacklisted characters."""
    return re.sub(r"|".join(BLACKLIST), "", number)


def length(number):
    """Return the clean length of a number."""
    return len(clean(number))


class Analyse:
    def __init__(self, language):
        # TODO: Allow for a threshold for numbers to consider.
        with open(f"{DATA_DIR}/{language}.txt", "r") as f:
            self.numbers = f.read().splitlines()
            self.clean_numbers = [clean(number) for number in self.numbers]

    @cached_property
    def lengths(self):
        """Return length of numbers below given threshold."""
        return [length(number) for number in self.numbers]

    def average_length(self, threshold):
        """Return length of numbers below a given threshold."""
        # TODO: Check if this index is correct.
        lengths = self.lengths[:min(len(self.numbers), threshold)]
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
    def simple_cycles(self):
        return list(nx.simple_cycles(self.graph))

    @cached_property
    def fixed_points(self):
        return [cycle[0] for cycle in self.simple_cycles if len(cycle) == 1]

    @cached_property
    def cycles(self):
        """Return simple cycles that are not fixed points."""
        return [cycle for cycle in self.simple_cycles if len(cycle) > 1]

    @cached_property
    def highest_fixed_point(self):
        return max(self.fixed_points, key=lambda x: length(x))

    @cached_property
    def longest_cycle(self):
        return max(self.simple_cycles, key=len)
