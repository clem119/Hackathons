import imports
from scipy.stats import levene
from Q4 import training_set,test

training_loads = training_set.loc[:,'Load']
test_loads = test.loc[:,'Load']

stat,p = levene(training_loads,test_loads)
print('stat value :',stat," p-value :",p)

