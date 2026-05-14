import pandas as pd
import numpy as np

# Load CSV file
df = pd.read_csv("dataset/energy_usage.csv")

# Convert timestamp column
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Convert energy column to float
df['energy_kwh'] = df['energy_kwh'].astype(float)

# Room-wise summary
room_summary = df.groupby('room_id')['energy_kwh'].sum()

print("Room-wise Energy Summary:")
print(room_summary)

# Average energy usage
average_energy = np.mean(df['energy_kwh'])

print("\nAverage Energy Usage:")
print(average_energy)