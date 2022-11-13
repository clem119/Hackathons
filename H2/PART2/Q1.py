from imports import *

df2 = pd.read_csv("H2/Data_energy_load.csv", sep=";")

new_dates = []

for i in df2.iterrows():
    string = i[1][0]
    modif = f'20{string[6:]}{string[3:5]}{string[:2]}'
    new_dates.append(modif)

df2 = df2.drop(["Date"], axis=1)
df2.insert(0, "Date", new_dates, True)

df2["Date"] = pd.to_datetime(df2["Date"], format='%Y%m%d', errors='ignore')
for i in df2["Date"]:
    print(i)

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