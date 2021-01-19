
class path():

    def ubrani_souboru(cesta_nazvu):
         cesta_inv=cesta_nazvu[::-1] #invertuje cestu
         pozice=cesta_inv.find('/') #najde poradi posledniho lomitka
         cesta_konecna=cesta_nazvu[0:len(cesta_nazvu)-pozice] # odstrani z cesty nazev souboru a ponecha jen slozku

         return cesta_konecna

def pozdrav():
    print("----------------------------------")
    print("Nazdar šprte!   -   здраво нероди!")
    print("----------------------------------")
