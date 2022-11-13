from imports import *
from pingouin import ttest
from Q1 import df2, LOAD_DATA

p_11 = df2.loc[df2['Hour'] == 10]
p_11 = np.array(p_11["Load"])

p_13 = df2.loc[df2['Hour'] == 12]
p_13 = np.array(p_13["Load"])



result = stats.ttest_rel(p_11, p_13)
result2 = ttest(p_11, p_13, correction = False)
test = np.array(result2["p-val"])

print("We use here a Student test")
print("=============================================")
"""print("P-value =",  result.pvalue)"""
print("stat value =",  result2["T"][0])
print("p-value =" , result2["p-val"][0])
print("=============================================")