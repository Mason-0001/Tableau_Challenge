# Dependencies
import pandas as pd

file1 = "Personal-Repo/Tableau_Challenge/Data/201306-citibike-tripdata.csv"
file2 = "Personal-Repo/Tableau_Challenge/Data/2013-12 - Citi Bike trip data.csv"
# Read in CSV's

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Clean CSV's

df1 = df1.dropna()
print(df2.count())

df2 = df2.dropna()
print(df2.count())

main_df = pd.concat([df1, df2], axis=0)
print(main_df.head())
print(main_df.tail())
main_df.to_csv("Personal-Repo/Tableau_Challenge/Data/citibike_merge_clean.csv")
