import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Set style
sns.set_theme(style="whitegrid")

# Load processed data
script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, '../data/processed/photocatalysis_cleaned.csv')
df = pd.read_csv(input_path)

fig_dir = os.path.join(script_dir, '../results/figures')
table_dir = os.path.join(script_dir, '../results/tables')
os.makedirs(fig_dir, exist_ok=True)
os.makedirs(table_dir, exist_ok=True)

# 1. Exploratory Data Analysis (EDA)

# 1.1 Distribution of Degradation Efficiency
plt.figure(figsize=(8, 6))
sns.histplot(df['Degradation_Efficiency'], bins=15, kde=True, color='skyblue')
plt.title('Distribution of Degradation Efficiency (%)', fontsize=14)
plt.xlabel('Efficiency (%)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, 'efficiency_distribution.png'), dpi=300)
plt.close()

# 1.2 Catalyst vs Efficiency (Boxplot)
plt.figure(figsize=(10, 6))
sns.boxplot(x='Catalyst', y='Degradation_Efficiency', hue='Light_Source', data=df)
plt.title('Catalyst Performance Across Light Sources', fontsize=14)
plt.xlabel('Catalyst Type')
plt.ylabel('Degradation Efficiency (%)')
plt.legend(title='Light Source')
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, 'catalyst_vs_light.png'), dpi=300)
plt.close()

# 1.3 Dosage impact
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Dosage_g_L', y='Degradation_Efficiency', hue='Catalyst', data=df, s=100, alpha=0.7)
sns.kdeplot(x='Dosage_g_L', y='Degradation_Efficiency', data=df, levels=5, color="k", linewidths=1)
plt.title('Effect of Catalyst Dosage on Efficiency', fontsize=14)
plt.xlabel('Dosage (g/L)')
plt.ylabel('Degradation Efficiency (%)')
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, 'dosage_impact.png'), dpi=300)
plt.close()

# 1.4 Correlation Matrix
plt.figure(figsize=(8, 6))
numeric_df = df[['Dosage_g_L', 'pH', 'Time_min', 'Degradation_Efficiency', 'Efficiency_Rate']]
corr = numeric_df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1, fmt='.2f')
plt.title('Correlation Matrix of Continuous Variables', fontsize=14)
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, 'correlation_matrix.png'), dpi=300)
plt.close()

# 2. Statistical Analysis
stats_path = os.path.join(table_dir, 'stats_summary.txt')
with open(stats_path, 'w') as f:
    f.write("=== STATISTICAL ANALYSIS REPORT ===\n\n")

    # 2.1 ANOVA: Does Catalyst type significantly affect efficiency?
    f.write("1. One-Way ANOVA: Effect of Catalyst on Efficiency\n")
    f.write("-" * 50 + "\n")
    model_cat = ols('Degradation_Efficiency ~ C(Catalyst)', data=df).fit()
    anova_table = sm.stats.anova_lm(model_cat, typ=2)
    f.write(anova_table.to_string())
    f.write("\n\n")
    
    if anova_table['PR(>F)'][0] < 0.05:
        f.write("Conclusion: There is a statistically significant difference in efficiency between catalysts types (p < 0.05).\n\n")
    else:
        f.write("Conclusion: No significant difference found between catalysts (p >= 0.05).\n\n")

    # 2.2 T-Test: UV vs Visible light for TiO2/GO
    f.write("2. Independent T-Test: UV vs Visible Light for TiO2/GO\n")
    f.write("-" * 50 + "\n")
    uv_data = df[(df['Catalyst'] == 'TiO2/GO') & (df['Light_Source'] == 'UV')]['Degradation_Efficiency']
    vis_data = df[(df['Catalyst'] == 'TiO2/GO') & (df['Light_Source'] == 'Visible')]['Degradation_Efficiency']
    
    if len(uv_data) > 0 and len(vis_data) > 0:
        t_stat, p_val = stats.ttest_ind(uv_data, vis_data, nan_policy='omit')
        f.write(f"T-statistic: {t_stat:.4f}\n")
        f.write(f"P-value:     {p_val:.4e}\n\n")
        
        if p_val < 0.05:
            f.write("Conclusion: UV light leads to significantly different efficiency compared to Visible light for TiO2/GO.\n\n")
        else:
            f.write("Conclusion: No significant difference between UV and Visible light for TiO2/GO.\n\n")
    else:
        f.write("Not enough data to perform T-Test.\n\n")
        
    # 2.3 Multiple Regression
    f.write("3. Multiple Linear Regression\n")
    f.write("-" * 50 + "\n")
    # Convert categorical to dummies
    df_reg = pd.get_dummies(df[['Degradation_Efficiency', 'Dosage_g_L', 'pH', 'Time_min', 'Catalyst', 'Light_Source']], drop_first=True)
    X = df_reg.drop('Degradation_Efficiency', axis=1)
    # Add constant before sm.OLS
    X = sm.add_constant(X)
    
    # Cast boolean columns to integers so statmodels doesn't fail
    for col in X.columns:
        if X[col].dtype == 'bool':
            X[col] = X[col].astype(int)

    y = df_reg['Degradation_Efficiency']
    
    model_reg = sm.OLS(y, X).fit()
    f.write(model_reg.summary().as_text())
    
print("EDA and Statistical Analysis completed. Results saved in 'results/'")
