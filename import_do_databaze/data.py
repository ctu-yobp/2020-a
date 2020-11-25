class databaze:


    #vytvori databazi se jmenem z 'projekt'
    def vytvoreni(nazev):
        import sqlite3 as sql
        projekt=nazev+'.db'
        con=sql.connect(projekt)
        con.close()
        return projekt

    #vytvori v databazi tabulku pro import souradnic
    def vytvoreni_tabulka_gps_sour(nazev_databaze):
        import sqlite3 as sql
        con=sql.connect(nazev_databaze)
        query='CREATE TABLE IF NOT EXISTS gps_sour (id int PRIMARY KEY, CB text,Y double,X double,Z double,kod text)'
        con.executescript(query)
        con.close()

    #vytvori v databazi tabulku pro import mereni
    def vytvoreni_tabulka_mereni(nazev_databaze):
        import sqlite3 as sql
        con=sql.connect(nazev_databaze)
        query='CREATE TABLE IF NOT EXISTS mereni (id int PRIMARY KEY, Stanovisko int,Orientace int,Delka double,Zenitka double,Smer double,Kod text)'
        con.executescript(query)
        con.close()

    #po zavolani smaze vsechna data z tabulky souradnic
    def mazani_sour(nazev_databaze):
        import sqlite3 as sql
        con=sql.connect(nazev_databaze)
        con.executescript('DELETE FROM  gps_sour')
        con.close()

    #po zavolani smaze vsechna data z tabulky mereni
    def mazani_mereni(nazev_databaze):
        import sqlite3 as sql
        con=sql.connect(nazev_databaze)
        con.executescript('DELETE FROM  mereni')
        con.close()

    #importuje souradnice do databaze
    def import_souradnic(cesta,nazev_databaze):
        import sqlite3 as sql
        con=sql.connect(nazev_databaze)

        id=1
        with open(cesta, 'r') as radky:
            for radky in radky.read().splitlines():
                CB, Y, X, Z, kod = radky.split(' ')

                query='INSERT INTO gps_sour VALUES({}, " {} ", {}, {}, {}, " {} ")'.format(id, CB, Y, X, Z, kod)
                con.execute(query)

                id=id+1

        con.commit()
        con.close()

    #importuje mereni do databaze
    def import_mereni(cesta, nazev_databaze):
        import sqlite3 as sql
        con=sql.connect(nazev_databaze)

        id=1
        with open(cesta, 'r') as radky:
            for radky in radky.read().splitlines():
                if radky[0:4]=='09F1':
                    stan=radky[4:8]
                    ori=radky[8:12]
                    delka=radky[12:18]
                    zenitka=radky[22:30]
                    smer=radky[32:40]
                    kod=radky[42:]

                    query='INSERT INTO mereni VALUES({},  {} , {}, {}, {}, {}," {} ")'.format(id, stan, ori, delka, zenitka, smer,kod)
                    con.execute(query)

                    id=id+1

        con.commit()
        con.close()

    #pristup k databazi
    def sql_query(nazev_databaze,dotaz):
        import sqlite3 as sql
        con=sql.connect(nazev_databaze)
        c=con.cursor()
        c.execute(dotaz)
        radky=c.fetchall()
        con.close()

        return radky
