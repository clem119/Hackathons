from imports import *

df2 = pd.read_csv("H2/Data_energy_load.csv", sep=";")

df2["Date"] = pd.to_datetime(df2["Date"], format='%d-%m-%Y')

LOAD_DATA = np.array(df2["Load"])

fig, ax = plt.subplots(figsize=(15, 15))

plt.plot([i for i in range(len(df2["Date"]))], LOAD_DATA, color="slategrey")
plt.xlabel("Time")
plt.ylabel("Consumption")

colors = [
    "firebrick",
    "brown",
    "indianred",
    "lightcoral"
]
for i in range(4):
    plt.axvline(x = i*8760, 
    color = colors[i],
    linewidth=5
    )


ax.legend([
    "DATA", 
    "02/01/2015", 
    "02/01/2016", 
    "02/01/2017", 
    "02/01/2018"
    ])
ax.set_xticks([])
plt.title("Time series of consumption")
plt.show()