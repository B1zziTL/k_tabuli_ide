#naimportovanie modulu random
import random

#zistenie vstupu, ulozenie ako integer
studenti = int(input("Počet študentov:"))
otazky = int(input("Počet otázok:"))

#podmienka na dodrzanie studenti < otazky
while studenti > otazky:
    #opakovanie vstupu
    otazky = int(input("Málo otázok! Nový počet otázok:"))

#vytvorenie zoznamov pomocou vstupu
pocet_studentov = list(range(1,studenti+1))
pocet_otazok = list(range(1,otazky+1))

def priradenie(): #funkcia na priradenie studentov k otazkam
    #zadefinovanie globalnej funkcie
    global studenti

    #zadefinovanie pomocnej funkcie
    parnost = 0

    for i in range(studenti): #cyklus na pocet opakovani zo vstupu
        #vyzrebovanie nahodnych hodnot
        poradie = random.choice(pocet_studentov)
        otazka = random.choice(pocet_otazok)

        #podmienka na zaistenia striedania parnych a neparnych otazok
        while (parnost % 2) == 0 and (otazka % 2) != 0:
            #opakovanie zrebovania
            otazka = random.choice(pocet_otazok)
        while (parnost % 2) != 0 and (otazka % 2) == 0:
            #opakovanie zrebovania
            otazka = random.choice(pocet_otazok)

        #zmena pomocnej premennej
        parnost += 1

        #odstranenie vyzrebovanyh hodnot zo zonamov
        pocet_studentov.remove(poradie)
        pocet_otazok.remove(otazka)

        #vypisanie pozadovanych hodnot
        print(str(i+1)+"."+" študent: "+str(poradie)+", otázka: "+str(otazka))

#zavolanie funkcie       
priradenie()            
    
