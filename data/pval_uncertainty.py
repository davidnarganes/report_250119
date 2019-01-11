import numpy as np
from scipy.stats import ttest_ind as tt

# Create the variables a and b with 1000 observations
a = np.random.randn(1000)
b = np.random.randn(1000) + 1

# Calculate the pvalue with different sample sizes but same distributions
res_sample_size_big = tt(a,b)
res_sample_size_sml = tt(a[:200], b[:500])

# Results
res_sample_size_big.pvalue
[out]: 6.097333515056883e-110

res_sample_size_sml.pvalue
[out]: 3.0005159036515865e-31