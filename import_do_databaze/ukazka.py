# systemove knihovny
import os

# vlastni knihovny
from data import Databaze
from config import DB_CONFIG, DATA_CONFIG  # import konfigurace databaze a dat


databaze = Databaze()

databaze.vytvoreni(DB_CONFIG["nazev_projektu"])

databaze.vytvor_tabulku(DB_CONFIG["tabulka_souradnic"], DB_CONFIG["schema_tabulky_souradnic"])
databaze.vytvor_tabulku(DB_CONFIG["tabulka_mereni"], DB_CONFIG["schema_tabulky_mereni"])

# databaze.smazat(DB_CONFIG["tabulka_souradnic"], '')
# databaze.smazat(DB_CONFIG["tabulka_mereni"], '')

databaze.importuj_sour(DATA_CONFIG['cesta_sour'])
databaze.importuj_mereni(DATA_CONFIG['cesta_mereni'])

# data=Databaze.sql_query(projekt,'select * from gps_sour')
# print(data[0][:])
