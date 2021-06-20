import pandas as pd


from os import listdir
from analysis import Analyse, clean, length


langs = sorted([filename[:-4] for filename in listdir("../data/raw_data")])


data = {
    "language": [],
    "max_fixed_point": [],
    "max_cycle_length": [],
    "fixed_point": [],
    "cycle": []
}

for lang in langs:
    try:
        summary = Analyse(lang)

        data["language"].append(lang)
        if summary.fixed_points:
            data["max_fixed_point"].append(length(summary.highest_fixed_point))
            data["fixed_point"].append(summary.highest_fixed_point)
        else:
            data["max_fixed_point"].append(-1)
            data["fixed_point"].append("Null")

        data["max_cycle_length"].append(len(summary.longest_cycle))
        data["cycle"].append(" → ".join(summary.longest_cycle))
    except Exception as e:
        print(lang)
        print(e)
        print()


df = pd.DataFrame.from_dict(data)


with open("results_table.txt", "w") as f:
    f.write(df.to_markdown())
