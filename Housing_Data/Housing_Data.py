"""Write a program to ingest the home_data.csv file and list the 10 least expensive houses along with their ZIP codes, condition, and living square feet."""
import csv
# with open("Housing_Data/home_data.csv", "r") as file:
#     data = file.readlines()
    

#     # C:\Users\Demet\Programming\UD Problem Sets\Housing_Data\home_data.csv

# print(data)

data = csv.DictReader("Housing_Data\home_data.home_data.csv")

print(list(data))