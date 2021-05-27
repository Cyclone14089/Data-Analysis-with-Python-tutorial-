import pandas as pd

print()

######  Creating data frames  #####

d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)

print(type(df))
print()

print(df)

print()

#####  Accessing locations in data frames  #####

row = 0
column = 'col1'
dataElement = df.loc[row, column]

print(f"Element at [{row}, '{column}']:  {dataElement}")

print("Element at [0, 'col2']: ", df.loc[0, 'col2'])
print("Element at [1, 'col1']: ", df.loc[1, 'col1'])

print("\n---------------------------------------------------------------------------------")

#####  Modifying data frames  #####

row = 1
column = 'col2'
df.loc[row, column] = 7

print("After modification :-\n")

print("Element at [{}, '{}']:  {}".format(row, column, df.loc[row, column]))

print(f"\n{df}")

print("\n---------------------------------------------------------------------------------")

#####  Direct interaction with Columns (adding, accessing)  #####

df['col3'] = [5, 6] # adding a new column

# we need to keep in mind the number of rows associated with the data frame
# an error will be thrown if the index length does not match
# uncomment the line below to see the error in action 
# df['col4'] = [10, 11, 12]

print("After adding col3 :-\n")

print(df)

df['col4'] = [9, 8]
print("\n")
print("After adding col4 :-\n")
print(df)

print("\n---------------------------------------------------------------------------------")

print("Accessing col2 and col4 only :-\n")
print(df[['col2', 'col4']])

print("\n\nAccessing col1, col3 and col4 only :-\n")
print(df[['col1', 'col3', 'col4']])

print("\n\nAccessing col1, col2, col3 and col4 :-\n")
print(df[['col1', 'col2', 'col3', 'col4']])

print()