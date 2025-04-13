import numpy as np
import pandas as pd


# Create a DataFrame

df = pd.DataFrame({
    'A': [1, 2,np.nan, 4],
    'B': [5, 6, 7, np.nan],
    'C': ['z',np.nan, 'b', 'a']
})

print("Original DataFrame:")
print(df)

# Handling Missing Data
print("\nHandling Missing Data:")
print("Drop NA rows")
print(df.dropna())
print("\nFill NA with 0:")
print(df.fillna(0))


# Adding columns
df['D'] = df['A'] * 2
print("\nAdding a new column:")
print(df)

# Removing columns
df_dropped = df.drop(columns=['B'],axis=1)  # axis = 0 = rows, axis = 1 = columns
print("\nRemoved column B:")
print(df_dropped)

# Sorting
print("\nSorted by column A:")
print(df.sort_values(by='A', ascending=False))

# Applying functions
def double_value(x):
    return x * 2 if pd.notnull(x) else x

print("\nApplying function to column A:")
print(df['A'].apply(double_value))


