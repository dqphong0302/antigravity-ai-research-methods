import pandas as pd
import numpy as np
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, '../data/raw/photocatalysis_experiments.csv')
df = pd.read_csv(input_path)

print("Original shape:", df.shape)

# 1. Handle missing values
print(f"Missing values before: {df['Degradation_Efficiency'].isna().sum()}")
# Drop rows with missing target variable
df = df.dropna(subset=['Degradation_Efficiency'])
print(f"Missing values after: {df['Degradation_Efficiency'].isna().sum()}")

# 2. Handle outliers (Efficiency should be 0-100)
print(f"Outliers before: {(df['Degradation_Efficiency'] > 100).sum()}")
# Cap at 100
df.loc[df['Degradation_Efficiency'] > 100, 'Degradation_Efficiency'] = 100
# Alternatively, could drop: df = df[df['Degradation_Efficiency'] <= 100]

# 3. Create derived feature: Efficiency Rate (%/min)
df['Efficiency_Rate'] = (df['Degradation_Efficiency'] / df['Time_min']).round(4)

# 4. Save processed data
output_dir = os.path.join(script_dir, '../data/processed')
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'photocatalysis_cleaned.csv')
df.to_csv(output_path, index=False)
print("Cleaned shape:", df.shape)
print(f"Processed data saved to {output_path}")
