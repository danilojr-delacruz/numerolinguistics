import pandas as pd


from os import listdir
from numerolinguistics.analysis import Analyse, SUPPORTED_LANGUAGES


data = {
    "language": [],
    "max_fixed_point": [],
    "fixed_point": [],
    "max_cycle_length": [],
    "cycle": []
}

for lang in SUPPORTED_LANGUAGES:
    try:
        summary = Analyse(lang)

        data["language"].append(lang)
        data["max_fixed_point"].append(summary.max_fixed_point)
        data["fixed_point"].append(summary.highest_fixed_point)
        data["max_cycle_length"].append(summary.max_cycle_length)
        data["cycle"].append(" → ".join(summary.longest_cycle))
    except Exception as e:
        print(lang, e)

df = pd.DataFrame.from_dict(data)

df.columns = ["Language", "MFP", "Highest Fixed Point", "MCL", "Longest Cycle"]
df.columns = df.columns.to_series().apply(lambda r: "\\textbf{" + r + "}")

with open("results_table.txt", "w") as f:
    f.write("\\begin{landscape}\n")
    f.write(df.to_latex(
        index=False,
        longtable=True,
        column_format="|c|c|c|c|c|",
        escape=False
    ))
    f.write("\\end{landscape}\n")
