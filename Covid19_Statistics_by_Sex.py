# program name - covid_1.py
# Author: Gokce Gokmen, A01258386, set C, ACIT 1515
# Date: April 23,2021

import argparse
import pandas as pd

ap = argparse.ArgumentParser()  # argparse constraction
ap.add_argument("--filename", required=True)
args = vars(ap.parse_args())

filename = args["filename"]
datafields= ""

try:
    df = pd.read_csv(filename)

    for i in df.columns:
        datafields = datafields + i + " "

    number_of_cases = df.shape[0]
    sex_f = 100 * df[df["Sex"]=="F"].shape[0] / number_of_cases
    sex_m = 100 * df[df["Sex"]=="M"].shape[0] / number_of_cases
    sex_un = 100 * df.shape[0] - (sex_m+sex_f) / number_of_cases

    print("Data File Name:", filename)
    print("Data Fields:", datafields)
    print("Number of Cases:", number_of_cases)
    print("Covid case by gender:", sex_f, "% female, ", sex_m, "% male, ", sex_un, "% unspecified" )

except:
    print("File is not found")


