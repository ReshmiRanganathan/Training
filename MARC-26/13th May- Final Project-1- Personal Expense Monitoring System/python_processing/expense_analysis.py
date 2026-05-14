import pandas as pd
import numpy as np

# Load CSV file
df = pd.read_csv("dataset/expenses.csv")

# Convert amount column to float
df['amount'] = df['amount'].astype(float)

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Create month column
df['month'] = df['date'].dt.to_period('M')

# Monthly expense summary
monthly_expense = df.groupby(['month', 'category'])['amount'].sum().unstack().fillna(0)

print("Monthly Expense Summary:")
print(monthly_expense)

# Average expense
average_expense = np.mean(df['amount'])

print("\nAverage Expense:")
print(average_expense)