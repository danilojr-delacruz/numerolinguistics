"""Update the data file in the numerolinguistics module."""


from os import listdir


docstring = "A dictionary containing the numbers 0-100 for a collection of languages."


langs = sorted([filename[:-4] for filename in listdir("raw_data")])

with open("../numerolinguistics/data.py", "w") as f:
    f.write(f"\"\"\"{docstring}\"\"\"")
    f.write("\n\n")
    f.write("\n")
    f.write("NUMBERS = {\n")

    for lang in langs:
        f.write(f"   \"{lang}\" : [\n")
        with open(f"raw_data/{lang}.txt", "r") as numbers:
            for number in numbers.read().splitlines():
                f.write(f"      \"{number}\",\n")

            f.write("   ],\n")

    f.write("}")
    f.write("\n\n")
    f.write("\n")
    f.write("SUPPORTED_LANGUAGES = NUMBERS.keys()")
