from sys import stdout
from matplotlib import pyplot as plt
import math
import numpy as np

class Date:
    #classe qui permet de stocker une date plus facilement à partir d'une string
    # "yyyymmdd" =>  [date.yyyy, date.mm, date.dd]
    def __init__(self, date):
        self.year = int(date[:4])
        self.month = int(date[4:6])
        self.day = int(date[6:])

    #return une rerprésentation de l'objet
    def  __str__(self):
        return(
            str(self.year)+"/"+str(self.month)+"/"+str(self.day)
        )

#constantes imposées dans l'énoncé
PI = math.pi
RHO = 1.2
SPEEDLIMIT = 90/3.6 # en m/s
d1 = Date("20170101")
d2 = Date("20210101")
Pk = 0
beauvechain = None
elsenborn = None

#return un bolléen en fonction de si <date> se trouve chronologiquement entre <d1> et <d2>
def IsBetween(date, d1, d2):
    if date.year < d1.year or date.year > d2.year: return False
    elif date.year == d2.year:
        if date.month > d2.month or date.day > d2.day: return False
        else: return True
    else: return True

############################################################################

with open("Beauvechain.csv") as file1:
    beauvechain = file1.readlines()[1:]
file1.close()

with open("Elsenborn.csv") as file2:
        elsenborn = file2.readlines()[1:]
file2.close()

# déclaration variables
max_b = 0
x_b = []

max_e = 0
x_e = []

max_global = 0
x_global = []


for line in beauvechain:
    l = line.strip(" ").split(",") #formatage de la ligne
    date = Date(l[1]) #utilisation de la classe Date définie ci-haut
    speed = int(l[2])/10 #m/s
    if int(l[3]) == 0: #vérifie que le code d'erreur ne renseigne pas d'erreur
        if IsBetween(date, d1, d2): #vérifie que <date> est bien entre <d1> et <d2>
            if speed >= 0 and speed <= SPEEDLIMIT: #vérifie que la vitesse en m/s n'excéde pas 90km/h et soit positive
                Pe = 0.42*0.5*RHO*((32**2)*PI)*speed**3/(10**6) #application de la formule de l'énoncé (en W)
                x_b.append(Pe)
                x_global.append(Pe)
                if Pe > max_b: max_b = Pe
                if Pe > max_global: max_global = Pe

for line in elsenborn:
    l = line.strip(" ").split(",") #formatage de la ligne
    date = Date(l[1]) #utilisation de la classe Date définie ci-haut
    speed = int(l[2])/10 #m/s
    if int(l[3]) == 0: #vérifie que le code d'erreur ne renseigne pas d'erreur
        if IsBetween(date, d1, d2): #vérifie que <date> est bien entre <d1> et <d2>
            if speed >= 0 and speed <= SPEEDLIMIT: #vérifie que la vitesse en m/s n'excéde pas 90km/h et soit positive
                Pe = 0.42*0.5*RHO*((32**2)*PI)*speed**3/(10**6) #application de la formule de l'énoncé (en W)
                x_e.append(Pe)
                x_global.append(Pe)
                if Pe > max_e: max_e = Pe
                if Pe > max_global: max_global = Pe

x_b.sort()
x_e.sort()
x_global.sort()

XB_DATA = np.array(x_b)
XE_DATA = np.array(x_e)
XGLOBAL_DATA = np.array(x_global)

# moyenne
mean_b = XB_DATA.mean()
mean_e = XE_DATA.mean()
mean_global = XGLOBAL_DATA.mean()

# médiane
median_b = XB_DATA[len(XB_DATA)//2]
median_e = XE_DATA[len(XE_DATA)//2]
median_global = XGLOBAL_DATA[len(XGLOBAL_DATA)//2]

# écart type
std_dev_b = XB_DATA.std()
std_dev_e = XE_DATA.std()
std_dev_global = XGLOBAL_DATA.std()

# 95% percentile
quantile_95_b = np.quantile(XB_DATA, 0.95)
quantile_95_e = np.quantile(XE_DATA, 0.95)
quantile_95_global = np.quantile(XGLOBAL_DATA, 0.95)

# 5% percentile
quantile_05_b = np.quantile(XB_DATA, 0.05)
quantile_05_e = np.quantile(XE_DATA, 0.05)
quantile_05_global = np.quantile(XGLOBAL_DATA, 0.05)

# réponse >> output
print(f"Beauvechain:\nmean: {mean_b} MW\nmedian: {median_b} MW\nstandard daviation: {std_dev_b} MW\n5% percentile: {quantile_05_b} MW\n95% percentile: {quantile_95_b} MW\n")
print(f"Elsenborn:\nmean: {mean_e} MW\nmedian: {median_e} MW\nstandard daviation: {std_dev_e} MW\n5% percentile: {quantile_05_e} MW\n95% percentile: {quantile_95_e} MW\n")
print(f"Global:\nmean: {mean_global} MW\nstandard daviation: {std_dev_global} MW\n")

######Graphes pour visualiser (pas dans la consigne)##########

#Graphe Beauvechain

bins = [] # bins est l'argument qui permet de répartir les données en un certain nombre de barres verticales
for i in range(50): bins.append(i*max_b/50) # ici, l'argument bins est une liste qui comprend 50 intervales croissant linéairement entre 0 et la puissance max

fig, ax = plt.subplots(figsize=(12, 12))
plt.hist(XB_DATA, bins=bins, edgecolor='black')
plt.xlabel("Electric power capacity (MW)")
plt.ylabel("Nombre d'occurrences") 
plt.title("Electric power capacity (MW) from the 1/1/2017 to the 1/1/2021 (Beauvechain)")
plt.axvline(x = mean_b, color = 'red', label = 'mean')
plt.axvline(x = mean_b-std_dev_b, color = 'purple', label = 'mean-std_dev')
plt.axvline(x = mean_b+std_dev_b, color = 'purple', label = 'mean+std_dev')
plt.axvline(x = median_b, color = 'yellow', label = 'median')
ax.legend()
plt.show()

#Graphe Elsenborn

bins = [] # bins est l'argument qui permet de répartir les données en un certain nombre de barres verticales
for i in range(50): bins.append(i*max_e/50) # ici, l'argument bins est une liste qui comprend 50 intervales croissant linéairement entre 0 et la puissance max

fig, ax = plt.subplots(figsize=(12, 12))
plt.hist(x_e, bins=bins, edgecolor='black')
plt.xlabel("Electric power capacity (MW)")
plt.ylabel("Nombre d'occurrences") 
plt.title("Electric power capacity (MW) from the 1/1/2017 to the 1/1/2021 (Elsenborn)")
plt.axvline(x = mean_e, color = 'red', label = 'mean')
plt.axvline(x = mean_e-std_dev_e, color = 'purple', label = 'mean-std_dev')
plt.axvline(x = mean_e+std_dev_e, color = 'purple', label = 'mean+std_dev')
plt.axvline(x = median_e, color = 'yellow', label = 'median')
ax.legend()
plt.show()

#Graphe Global

bins = [] # bins est l'argument qui permet de répartir les données en un certain nombre de barres verticales
for i in range(50): bins.append(i*max_global/50) # ici, l'argument bins est une liste qui comprend 50 intervales croissant linéairement entre 0 et la puissance max

fig, ax = plt.subplots(figsize=(12, 12))
plt.hist(x_global, bins=bins, edgecolor='black')
plt.xlabel("Electric power capacity (MW)")
plt.ylabel("Nombre d'occurrences") 
plt.title("Electric power capacity (MW) from the 1/1/2017 to the 1/1/2021 (Global)")
plt.axvline(x = mean_global, color = 'red', label = 'mean')
plt.axvline(x = mean_global-std_dev_global, color = 'purple', label = 'mean-std_dev')
plt.axvline(x = mean_global+std_dev_global, color = 'purple', label = 'mean+std_dev')
plt.axvline(x = median_global, color = 'yellow', label = 'median')
ax.legend()
plt.show()