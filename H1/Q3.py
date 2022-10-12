from sys import stdout
from matplotlib import pyplot as plt
import math
import numpy as np
import Q1

Results=Q1.ElecPowerCapa()
x_e=Results[0]
x_b=Results[1]
x_global=x_b+x_e

x_b.sort()
x_e.sort()
x_global.sort()

XB_DATA = np.array(x_b)
XE_DATA = np.array(x_e)
XGLOBAL_DATA = np.array(x_global)

# mean
mean_b = XB_DATA.mean()
mean_e = XE_DATA.mean()
mean_global = XGLOBAL_DATA.mean()

# median
median_b = XB_DATA[len(XB_DATA)//2]
median_e = XE_DATA[len(XE_DATA)//2]
median_global = XGLOBAL_DATA[len(XGLOBAL_DATA)//2]

# standard deviation
std_dev_b = XB_DATA.std()
std_dev_e = XE_DATA.std()
std_dev_global = XGLOBAL_DATA.std()

# 95% percentile
quantile_95_b = np.quantile(XB_DATA, 0.95)
quantile_95_e = np.quantile(XE_DATA, 0.95)
quantile_95_global = np.quantile(XGLOBAL_DATA, 0.95)

# 5% percentile
quantile_05_b = np.quantile(XB_DATA, 0.05)
quantile_05_e = np.quantile(XE_DATA, 0.05)
quantile_05_global = np.quantile(XGLOBAL_DATA, 0.05)

# answer >> output
print(f"Beauvechain:\nmean: {mean_b} MW\nmedian: {median_b} MW\nstandard daviation: {std_dev_b} MW\n5% percentile: {quantile_05_b} MW\n95% percentile: {quantile_95_b} MW\n")
print(f"Elsenborn:\nmean: {mean_e} MW\nmedian: {median_e} MW\nstandard daviation: {std_dev_e} MW\n5% percentile: {quantile_05_e} MW\n95% percentile: {quantile_95_e} MW\n")
print(f"Global:\nmean: {mean_global} MW\nstandard daviation: {std_dev_global} MW\n")

######Graphes pour visualiser (pas dans la consigne)##########

#Graphe Beauvechain

max_b=x_b[-1]
max_e=x_e[-1]
max_global=max([max_b, max_e])

bins = [] # bins est l'argument qui permet de répartir les données en un certain nombre de barres verticales
for i in range(50): bins.append(i*max_b/50) # ici, l'argument bins est une liste qui comprend 50 intervales croissant linéairement entre 0 et la puissance max

fig, ax = plt.subplots(figsize=(12, 12))
plt.hist(XB_DATA, bins=bins, edgecolor='black')
plt.xlabel("Electric power capacity (MW)")
plt.ylabel("Nombre d'occurrences") 
plt.title("Electric power capacity (MW) from the 1/1/2017 to the 1/1/2021 (Beauvechain)")
plt.axvline(x = mean_b, color = 'red', label = 'mean')
plt.axvline(x = mean_b-std_dev_b, color = 'purple', label = 'mean-std_dev')
plt.axvline(x = mean_b+std_dev_b, color = 'purple', label = 'mean+std_dev')
plt.axvline(x = median_b, color = 'yellow', label = 'median')
ax.legend()
plt.show()

#Graphe Elsenborn

bins = [] # bins est l'argument qui permet de répartir les données en un certain nombre de barres verticales
for i in range(50): bins.append(i*max_e/50) # ici, l'argument bins est une liste qui comprend 50 intervales croissant linéairement entre 0 et la puissance max

fig, ax = plt.subplots(figsize=(12, 12))
plt.hist(x_e, bins=bins, edgecolor='black')
plt.xlabel("Electric power capacity (MW)")
plt.ylabel("Nombre d'occurrences") 
plt.title("Electric power capacity (MW) from the 1/1/2017 to the 1/1/2021 (Elsenborn)")
plt.axvline(x = mean_e, color = 'red', label = 'mean')
plt.axvline(x = mean_e-std_dev_e, color = 'purple', label = 'mean-std_dev')
plt.axvline(x = mean_e+std_dev_e, color = 'purple', label = 'mean+std_dev')
plt.axvline(x = median_e, color = 'yellow', label = 'median')
ax.legend()
plt.show()

#Graphe Global

bins = [] # bins est l'argument qui permet de répartir les données en un certain nombre de barres verticales
for i in range(50): bins.append(i*max_global/50) # ici, l'argument bins est une liste qui comprend 50 intervales croissant linéairement entre 0 et la puissance max

fig, ax = plt.subplots(figsize=(12, 12))
plt.hist(x_global, bins=bins, edgecolor='black')
plt.xlabel("Electric power capacity (MW)")
plt.ylabel("Nombre d'occurrences") 
plt.title("Electric power capacity (MW) from the 1/1/2017 to the 1/1/2021 (Global)")
plt.axvline(x = mean_global, color = 'red', label = 'mean')
plt.axvline(x = mean_global-std_dev_global, color = 'purple', label = 'mean-std_dev')
plt.axvline(x = mean_global+std_dev_global, color = 'purple', label = 'mean+std_dev')
plt.axvline(x = median_global, color = 'yellow', label = 'median')
ax.legend()
plt.show()