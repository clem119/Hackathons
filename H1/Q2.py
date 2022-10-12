import Q1
import time
import math
from typing import List
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

r = Q1.ElecPowerCapa()
Results=r[0]+r[1]

max=np.max(Results)
bins = [] # bins est l'argument qui permet de répartir les données en un certain nombre de barres verticales
for i in range(50): bins.append(i*max/50) # ici, l'argument bins est une liste qui comprend 50 intervales croissant linéairement entre 0 et la puissance max

plt.hist(Results, bins=bins, edgecolor='black')
plt.xlabel("Electric power capacity (MW)")
plt.ylabel("Nb") 
plt.title("Electric power capacity (MW) from the 1/1/2017 to the 1/1/2021")
plt.show()
