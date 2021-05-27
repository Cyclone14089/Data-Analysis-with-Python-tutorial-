import pandas as pd

print()

#####  Working with csv files  #####

isl_df = pd.read_csv('./isl_data.csv') # reading the file and storing it

print("The csv file :-\n")
print(isl_df)

print("\n\nBasic information about the csv file :-\n")
isl_df.info()

print("\n\nBasic statistical values for each column :-\n")
print(isl_df.describe().round(1)) # round(1) rounds off the values to 1 decimal place

### Filtering and Slicing in Data Frames -----------------------------------

print("\n\nAccessing single column :-\n")
print(isl_df['scoresFor'])

print("\n\nSum of all entries under 'scoresFor': ", isl_df['scoresFor'].sum())

row = 2
print(f"\n\nDisplaying row {row} :-\n")
print(isl_df.loc[row])

# filtering data according to certain conditions

position = 1
print(f"\n\nDisplaying info about team in position {position} :-\n")
print(isl_df.loc[isl_df["position"] == position]) # prints the row whose value in the column 'position' is equal to the value in variable position

print(f"\n\nDisplaying info about team whose scoresFor > 25 :-\n")
print(isl_df.loc[isl_df["scoresFor"] > 25]) # prints the row whose value in the column 'scoresFor' is greater than 25

print("\n\nDisplaying name of team whose scoresFor > 25 and scoresFor < 25 :-\n")
# prints the 'team.name' in the row whose value in the column 'scoresFor' is greater than 25 and 'scoresAgainst' is less than 25
print(isl_df.loc[(isl_df["scoresFor"] > 25) & (isl_df["scoresAgainst"] < 25), 'team.name']) 
# Displaying two more columns for the same condition as above
print("\nVerbose :-\n")
print(isl_df.loc[(isl_df["scoresFor"] > 25) & (isl_df["scoresAgainst"] < 25), ['team.name', 'scoresFor', 'scoresAgainst']]) 

print()