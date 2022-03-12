# MAP-DP for multivariate Gaussian data
# 
# This code loads up a csv file containing the data generate from a three component Gaussian mixture model.
# We then apply the MAP-DP algorithm using a Normal-Wishart likelihood for the data.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.ion()
import mapdp_nw as mapdp
# read in data
d = pd.read_csv('toydata.csv')
N = d.shape[0]
X = d[['X_1', 'X_2']].values.T
Z = d['Z'].values
# Set up Normal-Wishart MAP-DP prior parameters
N0 = 0.5            # Prior count (concentration parameter)
m0 = X.mean(1)[:, None]    # Normal-Wishart prior mean
a0 = 10             # Normal-Wishart prior scale
c0 = 10/float(N)    # Normal-Wishart prior degrees of freedom
B0 = np.diag(1/(0.05*X.var(1)))  # Normal-Wishart prior precision
# # Run MAPDP to convergence
mu, z, K, E = mapdp.mapdp_nw(X, N0, m0, a0, c0, B0)
# # Plotting
plt.figure(figsize=(10,5))
for j in range(1,K+1):
    i = (Z == j);
    plt.plot(X[0, i], X[1,i], '.')
plt.title('Ground truth')

plt.figure(figsize=(10,5))
for j in range(K):
    i = (z == j);
    plt.plot(X[0, i], X[1,i], '.')
plt.title('MAPDP estimated clusters')

plt.figure(figsize=(10,5))
plt.plot(E, '-b')
plt.title('MAPDP objective function')

