import Q1
import time
import math
from typing import List
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats
from Q4_Beauvechain import WindBeauvechain

a=3.99
pdf_gamma = stats.gamma(WindBeauvechain, a,loc=0,scale=1)
print(pdf_gamma)
list(WindBeauvechain).sort()
plt.xlabel('x-values')
plt.ylabel('PDF_gamma_values')
plt.title("Probability density funciton of gamma distribution")
plt.show()