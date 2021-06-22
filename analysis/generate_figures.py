"""Generate the figures used in the report.

Due to the randomness of the nx.draw, you may have to repeat the function
multiple times until you get lucky enough to get a good configuration.
"""


import networkx as nx
import matplotlib.pyplot as plt


from numerolinguistics.analysis import Analyse


def figure_1():
    en = Analyse("english", 10)
    plt.figure(figsize = (5, 5))
    nx.draw(en.graph, with_labels=True, node_size=1000)
    plt.savefig("figures/english10.png", format="PNG")


def figure_2():
    fr = Analyse("french", 10)
    plt.figure(figsize = (5, 5))
    nx.draw(fr.graph, with_labels=True, node_size=1000)
    plt.savefig("figures/french10.png", format="PNG")


def figure_3():
    en = Analyse("english", 100)
    plt.figure(figsize = (10, 10))
    nx.draw(en.graph, with_labels=True, node_size=[300*d for d in en.degree.values()])
    plt.savefig("figures/english100.png", format="PNG")


if __name__ == "__main__":
    figures = [figure_1, figure_2, figure_3]
    for figure in figures:
        figure()
