

import pandas as pd
import argparse
import sys

ap = argparse.ArgumentParser()  # Configuring the argparse object
ap.add_argument("--filename", required=True) # add new arguments
args = vars(ap.parse_args())

filename = args["filename"] # saving the received argument

try:
    df = pd.read_csv(filename)
    answer = input("File is existing. Do you want to continue?")
    if answer != "y":
        sys.exit("Exiting")
except:
    thisdict = {"date": [],      
               "area": [],
               "gender": [],
               "age": []
               }
    df = pd.DataFrame(thisdict)

    
# Save the changes
thisdict = {"date": [],      
               "area": [],
               "gender": [],
               "age": []
               }

new_case = "y"

while (new_case == "y") | (new_case == "Y"):  # continuous saving
    
    date = input("Enter the date case was identified [YYYY-MM-DD]:")
    area = input("Enter the health are where the case occured (? for list):")
    if area == "?":
        print("FR - Fraser")
        print("IN - Interior")
        print("NO - Northern")
        print("OC - Out of Canada")
        print("VC - Vancouver Coastal")
        print("VI - FVancouver Island")
        area = input("Enter the health are where the case occured:")
    gender = input("Enter gender [M, F or U (unknown)]:")
    age = input("Enter patient age:")

    print("The following case data has been entered:")
    print(date, " ", area, " ", gender, " ", age)

    save_or_discard = input("Enter S to keep this case data, anything else to discard it:")

    if (save_or_discard == "s") & (save_or_discard == "S"): # Saving
        thisdict["date"].append(date)
        thisdict["area"].append(area)
        thisdict["gender"].append(gender)
        thisdict["age"].append(age)
    else:
        pass
    
    new_case = input("Do you want to enter another case? [Y/N]")
    if (new_case != "y") & (new_case != "Y") & (new_case != "n") & (new_case != "N"):  
        new_case = input("Do you want to enter another case? [Y/N]")
        

save_data = input("Do you want save this data? [Y/N]")
if (save_data != "y") & (save_data != "Y") & (save_data != "n") & (save_data != "N"):  
        save_data = input("Do you want to save this data? [Y/N]")

if (save_data == "y") | (save_data == "Y"):
    df2 = pd.DataFrame(thisdict)
    df.append(df2)
    df.to_csv(filename)
    print("Change saved")
else:
    print("Change not saved")
                  
                       