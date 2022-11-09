
from imports import *
from Q2 import X, Y, f1, p_values

#part 1

column_headers = list(X.columns.values)
counter = 0
total = 0

string = ""

for i in range(len(p_values)):
    if p_values[i] <= 0.05:
        counter += 1
    else:
        string += "\n"
        X = X.drop(column_headers[i], axis='columns')
        string+=f"{column_headers[i]}"
    total+=1

print("=============================================")
print(f"Only {counter} coefficients over {total} were at least 95% significant.")
print(f"The following {total-counter} column(s) have been dropped:")
print(string)
print("=============================================\n")

#computing the linear regression
f2 = sm.OLS(Y,X).fit()
S2 = f2.summary()

#part 2

#print answers

RES = [
    [f1.fvalue, f2.fvalue],
    [f1.rsquared, f2.rsquared], 
    [f1.llf, f2.llf],
    [f1.aic, f2.aic],
    [f1.bic, f2.bic]
    ]

d = pd.DataFrame(RES, columns = ["BEFORE", "AFTER"], index=["F-Statistic", "R2", "Log-Likelihood", "AIC", "BIC"])

print("=============================================")
print(d)
print("=============================================\n")
