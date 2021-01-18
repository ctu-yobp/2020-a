from math import atan2, cos, sin, pi, sqrt, acos
from sqlite3.dbapi2 import connect
import sqlite3 as sql

# (X, Y) : LOKALNI SOURADNICE
# (x, y) : SOURADNICE S-JTSK

class vypocty():

    def zaokrouhleni(cislo,pocet_mist):
        zao=round(cislo*10**pocet_mist)/10**pocet_mist

        return zao

    def delka(bod1, bod2):

        dx=bod1[0][1]-bod2[0][1]
        dy=bod1[0][0]-bod2[0][0]
        d=sqrt(dx*dx+dy*dy)
        return d

    def smernik(bod1, bod2):

        dx=-bod1[0][1]+bod2[0][1]
        dy=-bod1[0][0]+bod2[0][0]
        smernik=atan2(dy,dx)

        smernik = smernik*200/pi

        if smernik<0:
            smernik=smernik+400

        return smernik

    def rajon(b_ori, b_sta, b_mer):
        smernik = 0
        for key in b_ori.keys():
            y_dif = b_ori[key]['y'] - b_sta['Y']
            x_dif = b_ori[key]['x'] - b_sta['X']
            sigma = 400 - (b_ori[key]['smer'] - atan2(y_dif, x_dif))
            smernik += sigma
        smernik /= len(b_ori)

        for key in b_mer.keys():
            b_mer[key]['x'] = b_sta['X'] + b_mer[key]['delka'] + cos(sigma + b_mer[key]['smer'])
            b_mer[key]['y'] = b_sta['Y'] + b_mer[key]['delka'] + sin(sigma + b_mer[key]['smer'])

        # print(b_mer)
        return b_mer


    def vyp_stanovisko(b_ori):
        stan = {'X': 0, 'Y': 0}
        # Lokalni souradnice
        keys = list(b_ori.keys())
        b_ori[keys[0]]['X'] = 0
        b_ori[keys[0]]['Y'] = b_ori[keys[0]]['delka']
        b_ori[keys[1]]['X'] = b_ori[keys[1]]['delka'] * cos((100 + b_ori[keys[1]]['smer'] - b_ori[keys[0]]['smer']) * pi / 200)
        b_ori[keys[1]]['Y'] = b_ori[keys[1]]['delka'] * sin((100 + b_ori[keys[1]]['smer'] - b_ori[keys[0]]['smer']) * pi / 200)

        # Transformacni prvky
        A = [(b_ori[keys[0]]['x'], b_ori[keys[0]]['y']), (b_ori[keys[0]]['X'], b_ori[keys[0]]['Y'])]
        B = [(b_ori[keys[1]]['x'], b_ori[keys[1]]['y']), (b_ori[keys[1]]['X'], b_ori[keys[1]]['Y'])]

        a_1 = ((A[0][0] - B[0][0]) * (A[1][0] - B[1][0]) + (A[0][1] - B[0][1]) * (A[1][1] - B[1][1])) / ((A[1][0] - B[1][0]) ** 2 + (A[1][1] - B[1][1]) ** 2)
        a_2 = ((A[0][1] - B[0][1]) * (A[1][0] - B[1][0]) - (A[0][0] - B[0][0]) * (A[1][1] - B[1][1])) / ((A[1][0] - B[1][0]) ** 2 + (A[1][1] - B[1][1]) ** 2)

        # Souradnice stanoviska
        stan['X'] = A[0][0] + a_1 * (0 - A[1][0]) - a_2 * (0 - A[1][1])
        stan['Y'] = A[0][1] + a_1 * (0 - A[1][1]) + a_2 * (0 - A[1][0])

        print(stan)
        return stan

    def prot_delek(bod1, bod2, d1, d2):
        dx = bod1[0]-bod2[0]
        dy = bod1[1]-bod2[1]
        d12 = (dx**2 + dy**2)**(1/2)

        sigma12 = atan2(dy, dx) * 200/pi
        sigma21 = (sigma12 + 200)


        om1 = acos((d12**2 + d1**2 - d2**2)/(2 * d1 * d12)) * 200/pi
        om2 = acos((d12**2 + d2**2 - d1**2)/(2 * d12 * d2)) * 200/pi

        sigma2 = sigma12 + om2
        sigma1 = sigma21 - om1

        bX = bod2[0] + d2 * cos(sigma2*pi/200)
        bY = bod2[1] + d2 * sin(sigma2*pi/200)
        vysledny_bod = [bX, bY]
        return vysledny_bod

# bod1=[(1041118.761, 736712.811)]
# # bod2=[(1041100.213, 736749.135)]
# # bod=vypocty.prot_delek(bod1,bod2,100,100)
# # print(bod)



# test_points = {503: {'x': 1044278.81, 'y': 834640.46, 'delka': 289.367, 'smer': 20.3894}, 504: {'x': 1044292.22, 'y': 834620.52, 'delka': 280.67, 'smer': 25.3950}}

# b_ori={5001:{'x': 1044278.81, 'y': 834640.46, 'smer': 12}}
# b_sta={'X': 1044288.81, 'Y': 834650.46}
# b_mer={5003:{'delka': 100, 'smer': 36.69}}
# vys=vypocty.rajon(b_ori,b_sta,b_mer)
# print(vys[5003]['x'])


# # vypocty.vyp_stanovisko(test_points)
#
# # print(test_points)
#
# con=sql.connect("PESL1120.db")
# query1='select Y, X from gps_sour where CB is {}{}{}{}{} '.format('"',' ',str(1),' ','"')
# query2='select Y, X from gps_sour where CB is {}{}{}{}{} '.format('"',' ',str(2),' ','"')
#
# cur=con.cursor()
#
# cur.execute(query1)
# bod1=cur.fetchall()
#
# cur.execute(query2)
# bod2=cur.fetchall()
#
#
# print(bod1)
# print(bod2)
# con.commit()
# con.close()
#
# vypocty.delka(bod1,bod2)
# vypocty.smernik(bod1,bod2)


# def main():
#     xy_orientace = {}
#     mereni_body = {}
#
#     with connect('import_do_databaze\\projekt.db') as con:
#         cur = con.cursor()
#
#         cur.execute('SELECT (SUBSTR(CB,2,4)) as CB, AVG(X), AVG(Y) FROM gps_sour group by 1;')
#         radky = cur.fetchall()
#         for CB, x, y in radky:
#             CB = int(CB)
#             if CB > 4000:
#                 xy_orientace[CB] = {}
#                 xy_orientace[CB]['x'] = x
#                 xy_orientace[CB]['y'] = y
#
#         cur.execute('SELECT Orientace as CB, Delka, Smer from mereni;')
#         radky = cur.fetchall()
#         for CB, delka, smer in radky:
#             CB = int(CB)
#             if CB > 4000:
#                 try:
#                     xy_orientace[CB]['delka'] = delka
#                     xy_orientace[CB]['smer'] = smer
#                 except KeyError:
#                     xy_orientace[CB] = {}
#                     xy_orientace[CB]['delka'] = delka
#                     xy_orientace[CB]['smer'] = smer
#             else:
#                 mereni_body[CB] = {}
#                 mereni_body[CB]['delka'] = delka
#                 mereni_body[CB]['smer'] = smer
#
#     # print(xy_orientace)
#     # print(mereni_body)
#
#     stanovisko = vyp_stanovisko(xy_orientace)
#     body = rajon(xy_orientace, stanovisko, mereni_body)
#
#     with connect('import_do_databaze\\projekt.db') as con:
#         cur = con.cursor()
#
#         cur.execute('DROP TABLE IF EXISTS vysledky')
#         cur.execute('CREATE TABLE IF NOT EXISTS vysledky (id int PRIMARY KEY, CB text,Y double,X double)')
#         id = 1
#         for key in body.keys():
#             cur.execute(f"INSERT INTO vysledky VALUES ({id},{key},{body[key]['y']},{body[key]['x']})")
#             id += 1
#
#
# main()
