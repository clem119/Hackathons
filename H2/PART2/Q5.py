from imports import *
from Q4 import test, predictData

predictedTest = predictData(test)
#print(predictedTest)

dayMean = test.groupby(test['Date'].dt.day)["Load"].mean().to_numpy()


predictDayMean = []
for i in range(34320, 35040, 24):
    dayConsuption = 0;
    for j in range(24):
        dayConsuption += predictedTest[i+j]
    predictDayMean.append(dayConsuption/24)

x_true = [i for i in range(30)]
MAE = mae(dayMean, predictDayMean)


print("Mean absolute error of the test set is :", MAE)

# plot the data

plt.plot(x_true,dayMean)
plt.errorbar(x_true, predictDayMean, MAE)
plt.title('forecast and real value with noise')
plt.xlabel('Load values')
plt.ylabel('days from 02/12/2018 and 31/12/2018')
plt.legend(['real values','forcast values'])
plt.show()
