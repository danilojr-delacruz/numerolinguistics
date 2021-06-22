import re
import networkx as nx


from functools import cached_property
from numerolinguistics.data import NUMBERS, SUPPORTED_LANGUAGES


# Remember to escape if it's a special character (Regex)
BLACKLIST = ["-", "\ ", "'", "`"]


def clean(number):
    """Remove blacklisted characters."""
    return re.sub(r"|".join(BLACKLIST), "", number)


def length(number):
    """Return the clean length of a number."""
    return len(clean(number))


class Analyse:
    def __init__(self, language, threshold=100):
        """Return the numbers in the langauge up to the threshold."""
        assert language in SUPPORTED_LANGUAGES, f"{language} is not supported."
        assert threshold <= 100, "Numbers above 100 are not available."
        self.threshold = threshold
        self.numbers = NUMBERS[language][:threshold + 1]
        self.clean_numbers = [clean(number) for number in self.numbers]

    @cached_property
    def lengths(self):
        """Return length of numbers below given threshold."""
        return [length(number) for number in self.numbers]

    @cached_property
    def graph(self):
        G = nx.DiGraph([
            (self.numbers[i], self.numbers[self.lengths[i]])
            for i in range(self.threshold + 1)])
        return G

    @cached_property
    def degree(self):
        return dict(self.graph.degree)

    @cached_property
    def cycles(self):
        return list(nx.simple_cycles(self.graph))

    @cached_property
    def fixed_points(self):
        return [cycle[0] for cycle in self.simple_cycles if len(cycle) == 1]

    @cached_property
    def proper_cycles(self):
        return [cycle for cycle in self.simple_cycles if len(cycle) > 1]

    @cached_property
    def highest_fixed_point(self):
        return max(self.fixed_points, key=lambda x: length(x))

    @cached_property
    def longest_cycle(self):
        return max(self.simple_cycles, key=len)
