"""Show top languages change depending on the blacklist."""


import pandas as pd


from itertools import chain, combinations
from numerolinguistics.analysis import Analyse, BLACKLIST, SUPPORTED_LANGUAGES


def powerset(iterable):
    """Return the powerset of the iterable.

    Source: https://docs.python.org/3/library/itertools.html?highlight=powerset#itertools-recipes"""
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


prettify = {
    "-": "H",
    "\ ": "S",
    "'": "A",
    "`": "B",
    ",": "C"
}


data = {
    "Blacklist": [],
    "Highest Fixed Point": [],
    "Maximum Cycle Length": [],
    "Most Fixed Points": [],
    "Most Proper Cycles": [],
}


for blacklist in powerset(BLACKLIST):
    pretty_blacklist = [prettify[symbol] for symbol in blacklist]
    data["Blacklist"].append(tuple(pretty_blacklist))

    hfp = []
    mcl = []
    mfp = []
    mpc = []
    mc = []

    for lang in SUPPORTED_LANGUAGES:
        try:
            summary = Analyse(lang, blacklist=blacklist)

            if summary.max_fixed_point == "-":
                hfp.append((lang, -1))
            else:
                hfp.append((lang, summary.max_fixed_point))
            mcl.append((lang, summary.max_cycle_length))
            mfp.append((lang, len(summary.fixed_points)))
            mpc.append((lang, len(summary.proper_cycles)))
            mc.append((lang, len(summary.cycles)))
        except Exception as e:
            print(lang, e)

    data["Highest Fixed Point"].append(max(hfp, key=lambda x: x[1]))
    data["Maximum Cycle Length"].append(max(mcl, key=lambda x: x[1]))
    data["Most Fixed Points"].append(max(mfp, key=lambda x: x[1]))
    data["Most Proper Cycles"].append(max(mpc, key=lambda x: x[1]))

df = pd.DataFrame.from_dict(data)


# Will have to make headers bold manually
with open("tables/altered_blacklist.txt", "w") as f:
    f.write(df.to_latex(
        index=False,
        longtable=True,
        column_format="|c|c|c|c|c|",
        escape=True
    ))
