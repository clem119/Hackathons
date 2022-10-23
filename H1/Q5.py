import math 
from scipy import stats
from Q4 import getDistributionParameters, WindBeauvechain, WindElsenborn

def printResults(array, place):

    #extract fitted gamma parameters
    alpha, loc, scale = getDistributionParameters(array)[0]

    #Gamma values for Wind speed in KM/H
    Expectation = stats.gamma.mean(alpha, loc, scale)
    Median = stats.gamma.median(alpha, loc, scale)
    Std = stats.gamma.std(alpha, loc, scale)
    Percentil = stats.gamma.ppf([0.05, 0.95],alpha, loc, scale) #put in an array the value for 5% and 95%

    #constants
    PI = math.pi
    RHO = 1.2
    S = (32**2)*PI

    #take a wind speed in km/h and convert in MW
    def windToPower(windSpeed):
        windSpeed = (windSpeed/3.6)**3
        Pk=8*0.5*RHO*S*windSpeed
        Pe = Pk*0.42 #because of the betz limit
        Pe = Pe/(10**6) #convert  in MW
        return Pe

    #convert values to power
    powerExpectation = windToPower(Expectation)
    powerMedian = windToPower(Median)
    powerStd = windToPower(Std)
    powerPercentil5 = windToPower(Percentil[0])
    powerPercentil95 = windToPower(Percentil[1])

    print("=====================================================================")
    print(f"Value gamma distribution for {place}:")
    print(f"Expected power for {place} (MW): {powerExpectation}")
    print(f"Median power for {place} (MW): {powerMedian}")
    print(f"Standard deviation of powers for {place} (MW): {powerStd}")
    print(f"5% and 95% percentiles of powers for {place} (MW): {powerPercentil5} and {powerPercentil95}")
    print("=====================================================================\n")

printResults(WindBeauvechain, "Beauvechain")
printResults(WindElsenborn, "Elsenborn")





