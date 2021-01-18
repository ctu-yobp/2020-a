# systemove knihovny
import os
import logging

# vlastni knihovny

# nastavi uroven logovani - rekne jaka uroven logu se ma v terminalu vypisovat (dobre pro vizualizaci co se na pozadi deje a pro odchytavani problemu)
# urovne jsou vzestupne: DEBUG, INFO, WARNING, ERROR, CRITICAL
# pro nastaveni urovne napr. WARNING se logy s urovni INFO a DEBUG nebudou vypisovat, logy s urovni DEBUG a vice (takze ERROR a CRITICAL) se vypisou
LOG_LEVEL = logging.INFO
LOG_FORMAT = '%(asctime)-15s %(levelname)s %(message)s' # nastavi format vypisujiciho logu (cas, uroven logu, zprava)

# konfigurace pro databazi
DB_CONFIG = {
    'nazev_projektu': 'projekt',
    'tabulka_souradnic': 'gps_sour',
    'tabulka_mereni': 'mereni',
    'tabulka_projekt': 'projekt',
    'schema_tabulky_souradnic': 'id int PRIMARY KEY, CB text,Y double,X double,Z double,kod text',
    'schema_tabulky_mereni': 'id int PRIMARY KEY, Stanovisko int,Orientace int,Delka double,Zenitka double,Smer double,Kod text',
    'schema_importu_souradnic': 'id int PRIMARY KEY, CB text,Y double,X double,Z double,kod text',
    'schema_importu_mereni': 'id int PRIMARY KEY, Stanovisko int,Orientace int,Delka double,Zenitka double,Smer double,Kod text',
    'schema_projekt': 'nazev text, cesta text, pocet_bodu int, pocet_mereni int'
}

# konfigurace dat
DATA_CONFIG = {
    'cesta_sour': os.path.join(os.path.dirname(__file__)) + '\..\data\PESL1120.txt',
    'cesta_mereni': os.path.join(os.path.dirname(__file__))+ '\..\data\pesl1120.sdr',
}
