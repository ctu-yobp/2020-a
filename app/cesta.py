
class path():

    def ubrani_souboru(cesta_nazvu):
         cesta_inv=cesta_nazvu[::-1] #invertuje cestu
         pozice=cesta_inv.find('/') #najde poradi posledniho lomitka
         cesta_konecna=cesta_nazvu[0:len(cesta_nazvu)-pozice] # odstrani z cesty nazev souboru a ponecha jen slozku

         return cesta_konecna

    def ziskej_cestu():
        # vraci cestu databaze
        with open('nazev.txt') as f:
            cesta=f.readlines()
        f.close()
        return cesta

    def zapis_cestu(cesta_projekt):
        soubor=open("nazev.txt","w")
        soubor.write(cesta_projekt)
        soubor.close()



def pozdrav():
    print("----------------------------------")
    print("Nazdar šprte!   -   здраво нероди!")
    print("----------------------------------")
