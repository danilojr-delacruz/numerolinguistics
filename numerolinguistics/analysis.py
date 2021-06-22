import re
import networkx as nx


from functools import cached_property
from numerolinguistics.data import NUMBERS, SUPPORTED_LANGUAGES


# Remember to escape if it's a special character (Regex)
BLACKLIST = ["-", "\ ", "'", "`"]


def clean(number, blacklist=BLACKLIST):
    """Remove blacklisted characters."""
    return re.sub(r"|".join(blacklist), "", number)


def length(number, blacklist=BLACKLIST):
    """Return the clean length of a number."""
    return len(clean(number, blacklist))


class Analyse:
    def __init__(self, language, threshold=100, blacklist=BLACKLIST):
        """Return the numbers in the langauge up to the threshold."""
        assert language in SUPPORTED_LANGUAGES, f"{language} is not supported."
        assert threshold <= 100, "Numbers above 100 are not available."
    
        self.language = language
        self.threshold = threshold
        self.blacklist = blacklist
        self.numbers = NUMBERS[language][:threshold + 1]

    def length(self, number):
        return length(number, self.blacklist)

    @cached_property
    def lengths(self):
        """Return length of numbers below given threshold."""
        return [self.length(number) for number in self.numbers]

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
        return [cycle[0] for cycle in self.cycles if len(cycle) == 1]

    @cached_property
    def proper_cycles(self):
        return [cycle for cycle in self.cycles if len(cycle) > 1]

    @cached_property
    def highest_fixed_point(self):
        return max(self.fixed_points, key=self.length) if self.fixed_points else "Null"

    @cached_property
    def longest_cycle(self):
        return max(self.cycles, key=len)

    @property
    def max_fixed_point(self):
        """Return the value of the highest fixed point."""
        return self.length(self.highest_fixed_point) if self.fixed_points else -1

    @property
    def max_cycle_length(self):
        return len(self.longest_cycle)

    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"(\"{self.language}\", {self.threshold}, {self.blacklist})")

    def __len__(self):
        "Return length of self.numbers"
        return self.threshold + 1
