import pandas
import pyperclip
import re
import time

cols_in_tracker = ["Roll", "Blank", "Blank", "Blank", "Blank", "Size", "Files", "Clips", "Duration"]

cols_in_report = ["Roll", "Camera", "Clips", "Duration", "Min", "Files", "Size", "GB"]
regex_list = [r"\w\d{3}\w+", r'[A-Z]', r"\d+", r"\d+:\d+", r"min", r"\d+", r"\d+\.\d*", r"GB"]


df = pandas.read_clipboard(sep=" ", header=None, names=cols_in_report, on_bad_lines="error")

for index, value in enumerate(df.columns):

    col_value = str(df[value][0])

df["Blank"] = "-"

ii = 0

for entry in df["Duration"]:

    hmsf_list = entry.split(":")

    # hmsf_list.append("00")

    while len(hmsf_list) < 3:
        hmsf_list.insert(0, "00")

    hmsf_list = [str(item).zfill(2) for item in hmsf_list]

    if len(hmsf_list) == 2:
        hmsf_list.insert(0, "0")

    df.at[ii, "Duration"] = ":".join(hmsf_list)

    ii = ii + 1

df = df[cols_in_tracker]

string = df.to_string(header=False, index=False, justify="left")

string = re.sub(r"((?<=^)|(?<= )|(?<=\n)) +", "", string)
string = string.replace(" ", "\t")

print(string)

pyperclip.copy(string)
