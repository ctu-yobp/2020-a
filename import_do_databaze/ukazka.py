from data import databaze


nazev_projektu='projekt'
cesta_sour='c:/Users/Jakub/Desktop/skola/magister/obp_projekt/PESL1120.txt'
cesta_mereni='c:/Users/Jakub/Desktop/skola/magister/obp_projekt/pesl1120.sdr'

projekt=databaze.vytvoreni(nazev_projektu)

databaze.vytvoreni_tabulka_gps_sour(projekt)
databaze.vytvoreni_tabulka_mereni(projekt)

databaze.mazani_sour(projekt)
databaze.mazani_mereni(projekt)

databaze.import_souradnic(cesta_sour,projekt)
databaze.import_mereni(cesta_mereni,projekt)

data=databaze.sql_query(projekt,'select * from gps_sour')
print(data[0][:])
