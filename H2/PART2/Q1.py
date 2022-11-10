from imports import *

df = pd.read_csv("H2/Data_energy_load.csv", sep=";")

df["Date"] = pd.to_datetime(df["Date"])

#C'est juste les loads en fonction du temps
LOAD_DATA = np.array(df["Load"])

plt.plot([i for i in range(len(df["Date"]))], LOAD_DATA)
plt.xlabel("Time")
plt.ylabel("Consumption")
plt.show()

#print(df)