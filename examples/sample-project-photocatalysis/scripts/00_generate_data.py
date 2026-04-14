import pandas as pd
import numpy as np
import os

# Set random seed for reproducibility
np.random.seed(42)

# Number of experiments
num_samples = 150

# Variables:
# - Catalyst: Type of catalyst (TiO2, ZnO, TiO2/GO)
# - Dosage_g_L: 0.1 to 1.5
# - Light_Source: UV, Visible, Solar
# - pH: 3 to 11
# - Time_min: 30, 60, 90, 120, 150
# - Degradation_Efficiency: calculated with some noise

catalysts = ['TiO2', 'ZnO', 'TiO2/GO']
lights = ['UV', 'Visible', 'Solar']
times = [30, 60, 90, 120, 150]

data = {
    'Experiment_ID': [f'EXP_{i:03d}' for i in range(1, num_samples + 1)],
    'Catalyst': np.random.choice(catalysts, num_samples),
    'Dosage_g_L': np.round(np.random.uniform(0.1, 1.5, num_samples), 2),
    'Light_Source': np.random.choice(lights, num_samples),
    'pH': np.round(np.random.uniform(3.0, 11.0, num_samples), 1),
    'Time_min': np.random.choice(times, num_samples),
}

df = pd.DataFrame(data)

# Fake relationship:
# Efficiency increases with Time_min, optimal dosage around 0.8,
# TiO2/GO > TiO2 > ZnO. UV > Solar > Visible
# Optimal pH around 6.5
def calculate_efficiency(row):
    # Base efficiency
    eff = 10
    
    # Time factor
    eff += row['Time_min'] * 0.4
    
    # Catalyst factor
    cat_factor = {'TiO2/GO': 25, 'TiO2': 15, 'ZnO': 10}[row['Catalyst']]
    eff += cat_factor
    
    # Light factor
    light_factor = {'UV': 20, 'Solar': 15, 'Visible': 5}[row['Light_Source']]
    eff += light_factor
    
    # Dosage factor (parabola centered at 0.8)
    dosage_eff = -40 * (row['Dosage_g_L'] - 0.8)**2 + 20
    eff += max(0, dosage_eff)
    
    # pH factor (parabola centered at 6.5)
    ph_eff = -2 * (row['pH'] - 6.5)**2 + 10
    eff += max(0, ph_eff)
    
    # Add noise
    eff += np.random.normal(0, 5)
    
    # Cap between 0 and 100
    return np.clip(eff, 0, 99.9)

df['Degradation_Efficiency'] = df.apply(calculate_efficiency, axis=1).round(2)

# Insert some missing values and outliers to demonstrate data cleaning
# Add missing values
missing_indices = np.random.choice(df.index, size=5, replace=False)
df.loc[missing_indices, 'Degradation_Efficiency'] = np.nan

# Add outliers
outlier_indices = np.random.choice(df.index, size=3, replace=False)
df.loc[outlier_indices, 'Degradation_Efficiency'] = 150.5 # Impossible value

# Using abspath for robustness running from anywhere
script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, '../data/raw')
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, 'photocatalysis_experiments.csv')
df.to_csv(output_path, index=False)
print(f"Raw data generated at {output_path}")
