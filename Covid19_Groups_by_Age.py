# program name - covid_3.py
# Author: Gokce Gokmen, A01258386, set C, ACIT 1515
# Date: April 23, 2021


"""This program displays the total number of Covid-19 cases by age group in BC. """
import pandas as pd

df = pd.read_csv("BCCDC_COVID19_Case_Details.csv") # read_csv

df_group = df.groupby("Age_Group").agg({"Age_Group":"count"}) # groupby and count
df_group = df_group.rename(columns={"Age_Group":"Case_Count"}) #change column name

df_group = df_group.reset_index() # remove index

total_case = df_group["Case_Count"].sum() # sum all cases

# Founding Pct
for i in df_group.Age_Group:
    group_case = df_group.loc[df["Age_Group"]==i,"Case_Count"]
    df_group.loc[df["Age_Group"]==i,"Pct"] = 100 * group_case / total_case   

df_group = df_group.sort_values(by="Pct") # Sorting Pct

# Creating Histogram
for count, i in enumerate(df_group["Pct"]):
    count += 1
    df_group.loc[df_group["Pct"]==i,"Histogram"] = count * "*"

df_group = df_group.sort_values(by="Age_Group") # Sorting Age

# Editing Histogram
for count, i in enumerate(df_group["Histogram"]):
    a = 11 - len(i)
    if a > 0:
        space = " " * a
        df_group.loc[df_group["Histogram"]==i,"Histogram"] = df_group["Histogram"][count] + space

df_group.loc[df_group["Age_Group"]=="<10","Age_Group"] = "0-10" # Age_Group arrangement

df_group = df_group.sort_values(by="Age_Group") # Sorting Age

df_group.loc[df_group["Age_Group"]=="0-10","Age_Group"] = "<10" # Age_Group arrangement

print(df_group)