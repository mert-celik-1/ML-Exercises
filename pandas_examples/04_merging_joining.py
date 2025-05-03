import pandas as pd

df1 = pd.DataFrame({
    'id' : [1, 2, 3],
    'name' : ['Alice', 'Bob', 'Charlie'],
    'age' : [24, 27, 22]
})

df2 = pd.DataFrame({
    'id' : [2, 3, 4],
    'city': ['Los Angeles', 'Chicago', 'Houston'],
    'salary' : [5040,2312,21123],
})

print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)

# Different types of joins
print("\nInner Join:")
print(pd.merge(df1, df2, on='id', how='inner'))

print("\nLeft Join:")
print(pd.merge(df1, df2, on='id', how='left'))

print("\nRight Join:")
print(pd.merge(df1, df2, on='id', how='right'))

print("\nOuter Join:")
print(pd.merge(df1, df2, on='id', how='outer'))

# Concatenation
print("\nConcatenation (Vertical):")
print(pd.concat([df1, df1]))

print("\nConcatenation (Horizontal):")
print(pd.concat([df1, df2], axis=1))