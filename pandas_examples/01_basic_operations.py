import pandas as pd
import numpy as np

# Create a DataFrame

# From dictionary
data = {
    'name' : ['Alice', 'Bob', 'Charlie', 'David'],
    'age' : [24, 27, 22, 32],
    'city' : ['New York', 'Los Angeles', 'Chicago', 'Houston'],
}

df1 = pd.DataFrame(data)
print("\nFrom dictionary:")
print(df1)