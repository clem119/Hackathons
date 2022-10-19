from Q1 import ElecPowerCapa
import time
import math
from typing import List
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

r = ElecPowerCapa()
Results=r[0]+r[1]

sns.distplot(
    Results,
    kde=False, 
    bins=60,
    hist_kws=dict(color='brown', edgecolor='slategrey')
)

plt.xlabel("Electric power capacity (MW)")
plt.ylabel("Nb") 
plt.title("Electric power capacity (MW) from the 1/1/2017 to the 1/1/2021")
plt.show()
