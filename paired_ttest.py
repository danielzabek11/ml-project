import numpy as np
from scipy.stats import ttest_rel

effnet_accuracies = [0.9860, 0.9860, 0.9851, 0.9886, 0.9834]
densnet_accuracies = [0.9423, 0.9825, 0.972, 0.9667, 0.9658]

# Perform paired t-test
t_statistic, p_value = ttest_rel(effnet_accuracies, densnet_accuracies )

print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")
