import pandas as pd

# Create a DataFrame

# From dictionary
data_dict = {
    'name' : ['Alice', 'Bob', 'Charlie', 'David'],
    'age' : [24, 27, 22, 32],
    'city' : ['New York', 'Los Angeles', 'Chicago', 'Houston'],
}

df1 = pd.DataFrame(data_dict)
print("\nFrom dictionary:")
print(df1)

# From list of lists
data_list = [
    ['Alice', 24, 'New York'],
    ['Bob', 27, 'Los Angeles'],
    ['Charlie', 22, 'Chicago'],
    ['David', 32, 'Houston'],
]

df2 = pd.DataFrame(data_list, columns=['name', 'age', 'city'])
print("\nFrom list:")
print(df2)

# Basic operations
print("\nBasic operations:")
print("Head of DataFrame:\n", df1.head(1))

print("\nDataFrame info:")
print(df1.info())

print("\nDataFrame description:")
print(df1.describe())

# Accessing data
print("\nAccessing data:")
print("Single column:\n",df1['name'])
print("\nMultiple columns:\n",df1[['name', 'age']])

# Basic Filtering
print("\nFiltering:")
print("Age > 25:\n", df2[df2['age'] > 25])