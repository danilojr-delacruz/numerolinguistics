"""Generate the figures used in the report.

Due to the randomness of the nx.draw, you may have to repeat the function
multiple times until you get lucky enough to get a good configuration.

The numbering obeys the order in the report.
"""


import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import argparse


from argparse import RawTextHelpFormatter
from numerolinguistics.analysis import Analyse
from numerolinguistics.model import minimal_N, ulh


def english10():
    en = Analyse("english", 10)
    plt.figure(figsize = (5, 5))
    nx.draw(en.graph, with_labels=True, node_size=1000)
    plt.savefig("figures/english10.png", format="PNG")


def french10():
    fr = Analyse("french", 10)
    plt.figure(figsize = (5, 5))
    nx.draw(fr.graph, with_labels=True, node_size=1000)
    plt.savefig("figures/french10.png", format="PNG")


def english100():
    en = Analyse("english", 100)
    plt.figure(figsize = (10, 10))
    nx.draw(en.graph, with_labels=True, node_size=[300*d for d in en.degree.values()])
    plt.savefig("figures/english100.png", format="PNG")


def g_plot():
    m = 20
    n = np.linspace(1, 60, 100)
    def g(n):
        return ulh(n, m) - n

    plt.figure(figsize=(15, 3))
    plt.plot(n, g(n))
    plt.annotate("$m/\ln{10}$", (m / np.log(10) - 2.8, g(m / np.log(10)) - 2.5))
    plt.scatter(m / np.log(10), g(m / np.log(10)))
    plt.axhline(y=0, color='k')
    plt.xlabel("$n$")
    plt.ylabel("$g$")
    plt.savefig("figures/g_plot.png", format="PNG")


def N_estimate():
    m = np.linspace(1, 100)
    N = minimal_N(m)
    plt.plot(m, N, label="Minimal N")
    # a, b = np.polyfit(m, N, 1)
    # plt.plot(m, a*m + b, "--", label=f"$N = {a:.2f}m + {b:.2f}$")
    plt.plot(m, 4*m, "--", label=f"$N = 4m$")
    plt.xlabel("$m$")
    plt.ylabel("Minimal $N$")
    plt.legend(loc="upper left")
    plt.savefig("figures/N_estimate.png", format="PNG")


if __name__ == "__main__":
    description = """Generate figures.

    To generate all figures:
        python3 generate_figures.py figures a
    To generate figures xth and yth figure:
        python3 generate_figures.py figures x y
"""
    parser = argparse.ArgumentParser(description = description,
                                        formatter_class= RawTextHelpFormatter)

    parser.add_argument("figures", nargs="+")
    args = parser.parse_args()

    figures = [english10, french10, english100, g_plot, N_estimate]

    if args.figures[0] == "a":
        to_generate = figures
    else:
        to_generate = args.figures[1:]

    for i in to_generate:
        try:
            figures[int(i) - 1]()
            print(f"Figure {i} successfully generated.")
        except Exception as e:
            print(f"Error in generating figure {i}: {e}")
