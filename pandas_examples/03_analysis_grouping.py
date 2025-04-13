import pandas as pd
import numpy as np

# Create a Sales data
data = {
    'date': pd.date_range('2023-01-01', periods=10),
    'product': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C'],
    'sales': np.random.randint(10, 100, 10),
    'quantity': np.random.randint(1, 10, 10)
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Grouping
print("\nGrouping by product:")
grouped = df.groupby('product')
print(grouped)
print("\nMean sales by product:")
print(grouped['sales'].mean())
print("\nTotal sales by product:")
print(grouped['sales'].sum())


# Multiple aggregations
print("\nMultiple aggregations:")
agg_result = grouped.agg({
    'sales': ['sum', 'mean','std'],
    'quantity': ['sum', 'mean']
})
print(agg_result)


# Time-based analysis
print("\nSales by date:")
daily_sales = df.groupby('date')['sales'].sum()
print(daily_sales)

# Rolling statistics
print("\nRolling mean of sales (3-day window):")
print(daily_sales.rolling(window=3).mean())
