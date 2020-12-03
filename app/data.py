# systemove knihovny
import sqlite3 as sql
import logging

# vlastni knihovny
from config import LOG_LEVEL, LOG_FORMAT

logging.basicConfig(format=LOG_FORMAT)
loggerStd = logging.getLogger('standard')
loggerStd.setLevel(LOG_LEVEL)

class Databaze():

    # kostruktor databaze
    # def __init__(self):
    #     projekt=DB_CONFIG["nazev_projektu"]+'.db'
    #     con=sql.connect(projekt)
    #     con.close()

    #vytvori databazi se jmenem z 'projekt'
    def vytvoreni(self, nazev):
        """
        Vytvori databazi
        """        
        self.projekt=nazev+'.db'
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

                query='INSERT INTO gps_sour VALUES({}, " {} ", {}, {}, {}, " {} ")'.format(id, CB, Y, X, Z, kod)
                self.tabulka = 'gps_sour'
                self.posli_davku(query)

                id=id+1

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


    #pristup k databazi
    def sql_query(nazev_databaze,dotaz):
        con=sql.connect(nazev_databaze)
        c=con.cursor()
        c.execute(dotaz)
        radky=c.fetchall()
        con.close()

        return radky
