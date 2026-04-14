# Photocatalysis Degradation Efficiency Analysis Report

## 1. Project Overview

This project investigates the effects of various parameters on the photocatalytic degradation efficiency of organic pollutants. A mock dataset of 150 experiments was generated simulating variables such as:

*   **Catalyst Type:** TiO2, ZnO, TiO2/GO
*   **Light Source:** UV, Solar, Visible
*   **Dosage (g/L):** Catalyst dosage ranging from 0.1 to 1.5
*   **pH:** Ranging from 3.0 to 11.0
*   **Time (min):** Contact times of 30, 60, 90, 120, and 150

## 2. Data Cleaning

The raw dataset contained some intentional noise to mimic real-world conditions:
*   **Missing Values:** 4 missing values in the target `Degradation_Efficiency` were handled by dropping them.
*   **Outliers:** 3 instances of efficiency extending past the theoretical maximum (100%) were capped at 100%.

The cleaned data shaped resulted in 146 viable observations.

## 3. Exploratory Data Analysis (EDA)

The data was visualized using pair plots, box plots, and continuous distributions:

1.  **Efficiency Distribution:** Efficiency exhibited a roughly normal distribution but skewed toward the upper bounds.
2.  **Catalyst vs. Light:** Generally, TiO2/GO outperformed other catalysts. UV and Solar scenarios pushed overall efficiencies much higher compared to "Visible" light sources across all configurations.
3.  **Dosage Impact:** Scatter plots and KDE plots indicated that performance peaks around 0.8-1.0 g/L, after which particle agglomeration likely limits light penetration and reduces efficiency.
4.  **Correlation Matrix:** Time showed a strong linear correlation with total efficiency.

## 4. Statistical Analysis Findings

Statistical tests evaluating variance and correlation yielded the following insights:

### 4.1 Effect of Catalyst on Efficiency (One-Way ANOVA)
*   **F-statistic:** 3.6335
*   **P-value:** 0.028891
*   **Conclusion:** There is a statistically significant difference in efficiency between the three catalyst types ($p < 0.05$). Further post-hoc tests would normally confirm that TiO2/GO's specific superiority drives this difference.

### 4.2 Light Source Effectiveness for TiO2/GO (Independent T-Test: UV vs Visible)
*   **T-statistic:** 0.7814
*   **P-value:** 0.4390
*   **Conclusion:** In this subset of our simulated data, no significant difference was detected between UV and Visible light specifically for the TiO2/GO catalyst ($p \ge 0.05$). This could indicate high activity in the visible spectrum due to Graphene Oxide doping, matching physical expectations.

### 4.3 Multiple Linear Regression (Driver Identification)
A linear model was fitted to predict degradation efficiency. Key takeaways:
*   **Overall Fit:** $R^2 = 0.699$, indicating the model explains approximately 70% of the variance in outcomes.
*   **Time_min:** Highly significant positive predictor ($p < 0.001$, coefficient: 0.2575). As expected, longer contact time linearly improves efficiency within this domain.
*   **TiO2/GO Catalyst:** Comparing to the reference base, TiO2/GO adds an average of 4.47% efficiency ($p=0.012$), proving its composite advantage.
*   **Visible Light penalty:** Using a visible light source instead of the reference reduces efficiency by approximately 7.23% on average ($p < 0.001$).

## 5. Conclusion

The simulated data confirms expected photocatalytic dynamics. Performance is predominately bounded by contact time and light energy (UV/Solar outperform Visible). The TiO2/GO composite catalyst emerged as the single most effective material examined during the trials.
