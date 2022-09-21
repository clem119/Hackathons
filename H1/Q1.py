import time

def ElecPowerCapa():

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
    PI = 3.14159265358979
    RHO = 1.2
    SPEEDLIMIT = 90/3.6
    d1 = Date("20170101")
    d2 = Date("20210101")
    total = 0

    #return un bolléen en fonction de si <date> se trouve chronologiquement entre <d1> et <d2>
    def IsBetween(date, d1, d2):
        if date.year < d1.year or date.year > d2.year: return False
        elif date.year == d2.year:
            if date.month > d2.month or date.day > d2.day: return False
        else: return True

    with open("Beauvechain.csv") as file1:
        with open("Elsenborn.csv") as file2:
            for file in [file1, file2]:
                for line in file.readlines()[1:]:
                    l = line.strip(" ").split(",") #formatage de la ligne
                    date = Date(l[1]) #utilisation de la classe Date définie ci-haut
                    speed = int(l[2]) #lecture des fichiers
                    if int(l[3]) == 0: #vérifie que le code d'erreur ne renseigne pas d'erreur
                        if IsBetween(date, d1, d2): #vérifie que <date> est bien entre <d1> et <d2>
                            if speed >= 0 and speed <= SPEEDLIMIT: #vérifie que la vitesse en m/s n'excéde pas 90km/h et soit positive
                                total += 0.5*RHO*((32**2)*PI)*speed/(10**6) #application de la formule de l'énoncé
        file2.close()
    file1.close()
    return total

        


##########################

print("Answer Q1: "+str(ElecPowerCapa())+" Mega Watts")