# systemove knihovny
import sqlite3 as sql
import logging

# vlastni knihovny
from config import LOG_LEVEL, LOG_FORMAT

logging.basicConfig(format=LOG_FORMAT)
loggerStd = logging.getLogger('standard')
loggerStd.setLevel(LOG_LEVEL)

class Databaze():

    # # kostruktor databaze
    # def __init__(self):
    #     # # projekt=DB_CONFIG["nazev_projektu"]+'.db'
    #     # con=sql.connect(projekt)
    #     # con.close()

    #vytvori databazi se jmenem z 'projekt'
    def vytvoreni(self, nazev,cesta):
        """
        Vytvori databazi
        """

        self.projekt=cesta+nazev+'.db'
        con=sql.connect(self.projekt)
        con.close()
        # return projekt

    # vytvori pripojeni, posle davku a uzavre spojeni s databazi
    def posli_davku(self, davka):
        """
        Inicializuje spojeni s databazi, posle sql davku a ukonci spojeni.
        """
        con = sql.connect(self.projekt)
        try:
            con.executescript(davka)
            loggerStd.info('{} DAVKA POSLÁNA'.format(davka) )
        except sql.IntegrityError:
            # TODO: vypisujici se tabulka by se mela univerzalne prenaset, v importech je narvana natvrdo
            loggerStd.warning('{} UZ EXISTUJE! NELZE VLOZIT DO: {} (tabulka: {})'.format(davka, self.projekt, self.tabulka) )

        con.close()

    #vytvori v databazi tabulku pro import souradnic + self.tabulka je tu natvrdo
    def vytvor_tabulku(self, tabulka, schema):
        """
        Vytvori tabulku v databazi.
        """
        self.tabulka = tabulka
        query = 'CREATE TABLE IF NOT EXISTS {} ({})'.format(tabulka, schema)
        self.posli_davku(query)

    #smaze zadana data z zadane tabulky
    def smazat(self, tabulka, objekt_mazani):
        """
        Smaze datum v databazove tabulce.
        """
        query = 'DELETE {} FROM {}'.format(objekt_mazani, tabulka)
        self.posli_davku(query)

    # TODO: prepsat do unverzalni podoby importu + self.tabulka je tu natvrdo
    # importuje souradnice do databaze
    def importuj_sour(self, cesta_data):

        id=1
        with open(cesta_data, 'r') as f:
            for radek in f.read().splitlines():
                CB, Y, X, Z, kod = radek.split(' ')

                query='INSERT INTO gps_sour VALUES({}, " {} ", {}, {}, {}, " {} ")'.format(id, CB,Y, X, Z, kod)
                self.tabulka = 'gps_sour'
                self.posli_davku(query)

                id=id+1
        self.pocet_bodu=id

    # TODO: prepsat do unverzalni podoby importu
    #importuje mereni do databaze
    def importuj_mereni(self, cesta_data):

        id=1
        with open(cesta_data, 'r') as f:
            for radek in f.read().splitlines():
                if radek[0:4]=='09F1':
                    stan=radek[4:8]
                    ori=radek[8:12]
                    delka=radek[12:18]
                    zenitka=radek[22:30]
                    smer=radek[32:40]
                    kod=radek[42:]

                    query='INSERT INTO mereni VALUES({},  {} , {}, {}, {}, {}," {} ")'.format(id, stan, ori, delka, zenitka, smer,kod)
                    self.tabulka = 'mereni'
                    self.posli_davku(query)

                    id=id+1
        self.pocet_mereni=id

    #pristup k databazi
    def sql_query(nazev_databaze,dotaz):
        con=sql.connect(nazev_databaze)
        c=con.cursor()
        c.execute(dotaz)
        radky=c.fetchall()
        con.close()

        return radky

    def zapis_info(self,cesta):
        # zapise informace o projektu do tabulky "projekt"

        #odebrani jmena souboru z cesty
        cesta_inv=cesta[::-1]
        pozice=cesta_inv.find('/')
        cesta_konecna=cesta[0:len(cesta)-pozice]

        # zapis informaci
        con=sql.connect(self.projekt)
        c=con.cursor()
        query='insert into  projekt ("{}","{}","{}","{}") values ("{}","{}",{},{})'.format('nazev','cesta','pocet_bodu','pocet_mereni',self.projekt,cesta_konecna,str(self.pocet_bodu),str(self.pocet_mereni))

        c.execute(query)

        con.commit()
        con.close()

    def pridani_bodu(cesta, query):
        # zapise spocteny bod
        con=sql.connect(cesta)
        c=con.cursor()
        c.execute(query)
        con.commit()
        con.close()

    def export2txt(cesta_projekt,cesta):
        # export seznamu souradnic do textaku
        sour=Databaze.sql_query(cesta_projekt,'select * from gps_sour')

        protokol = open(cesta,'a')
        for i in range(0,len(sour)):
            cb=sour[i][1]
            Y=str(sour[i][2])
            X=str(sour[i][3])
            Z=str(sour[i][4])
            kod=sour[i][5]
            radek='{} {} {} {} {} \n'.format(cb,Y,X,Z,kod)
            protokol.write(radek)

        protokol.close()
