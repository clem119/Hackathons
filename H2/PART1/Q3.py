
from imports import *
from Q2_1 import X, Y

#part 1
#computing the linear regression
f2 = sm.OLS(Y,X).fit()
print(f2.summary())

#part 2

#getting the coefs, p-values and intercept
coefs = f2.summary2().tables[1]['Coef.']
p_values2 = f2.pvalues

#compute log-likelihood

#compute AIC

#compute BIC

#print answers
print("=============================================")
print('F-Statistic: ',f2.fvalue)
print('R2: ',f2.rsquared)
print("=============================================\n")

print("=============================================")
print(f"p-values:\n\n{p_values2[1:]}")
print("=============================================\n")


# source:
# https://www.earthinversion.com/statistics/maximum-likelihood-estimation-with-examples-in-python/

def lik(parameters, x, y): 
    m = parameters[0] 
    b = parameters[1] 
    sigma = parameters[2] 
    
    y_exp = m * x + b 
        
    L = np.sum(np.log(stats.norm.pdf(y - y_exp, loc = 0, scale=sigma)))
    return -L


def constraints(parameters):
    sigma = parameters[2]
    return sigma

cons = {
    'type': 'ineq',
    'fun': constraints
}

for x in X.to_numpy():
    lik_model = scipy.optimize.minimize(lik, np.ones(len(Y))*0.5, args=(x, Y,), constraints=cons)
    print(lik_model)

def likelihood(yi, xi, beta):
    L = 0
