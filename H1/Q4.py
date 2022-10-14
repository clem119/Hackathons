from Q1 import ElecPowerCapa
import math
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from scipy import stats

fig = plt.figure(figsize=(20,20))

r = ElecPowerCapa()
Results=r[0]+r[1]

GammaStyle = dict(color='red', linewidth=4)
InvGaussStyle = dict(color='purple', linewidth=4)

sns.distplot(
    Results,
    hist=None,
    kde=False, 
    fit=stats.gamma, 
    fit_kws=GammaStyle,
    )


sns.distplot(
    Results, 
    hist=None,
    kde=False, 
    fit=stats.invgauss, 
    fit_kws=InvGaussStyle,
    label="label 2"
    )



plt.xlabel("Electric power capacity (MW)")
plt.ylabel("Nb of occurrence") 
plt.title("Electric power capacity (MW) from the 1/1/2017 to the 1/1/2021")

fig.legend(labels=['Gamma fit','Inverse Gaussian fit'])

plt.show()