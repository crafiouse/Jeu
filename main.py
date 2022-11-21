from os import system
import platform
def clear():
    if platform.system()== "Windows":
        system('cls')
    else:
        system('clear') 
        
from time import sleep
from persos import*
a=input("quel est ton nom jeune aventurier\n")
test=Protagonistes(a,4,20)
test.choix_classe
perso=Protagonistes(classe)
clear()
sleep(2)
perso.choix_classe
print(f"L'aventure du jeune {perso.nom} commence")
sleep(2)
clear()
mechant=Protagonistes("valentin",5,30)
perso.attaquer(mechant)

#definir random les potions du sorcier
