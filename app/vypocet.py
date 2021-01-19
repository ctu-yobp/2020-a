from math import atan2, cos, sin, pi, sqrt, acos
from sqlite3.dbapi2 import connect
import sqlite3 as sql
from data import Databaze

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
            sigma = 400*pi/200 - (b_ori[key]['smer']*pi/200 - atan2(y_dif, x_dif))
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

        # print(stan)
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

    def davka(cesta, stanovisko,orientace):
        xy_orientace = {}
        mereni_body = {}

        try:
            query='select CB, X, Y from gps_sour where CB is " {} "'.format(str(orientace))
            orientace_sour=Databaze.sql_query(cesta,query)
            CB=int(orientace_sour[0][0])
            xy_orientace[CB] = {}
            xy_orientace[CB]['x'] = orientace_sour[0][1]
            xy_orientace[CB]['y'] = orientace_sour[0][2]



            query='select Orientace, Delka, Zenitka, Smer,kod from mereni where Stanovisko is " {} "'.format(str(stanovisko))
            body_sour=Databaze.sql_query(cesta,query)

            for i in range(0,len(body_sour)):

                CB=int(body_sour[i][0])
                delka=body_sour[i][1]*sin(body_sour[i][2]*pi/200)
                smer=body_sour[i][3]


                mereni_body[CB] = {}
                mereni_body[CB]['delka'] = delka
                mereni_body[CB]['smer'] = smer
                if CB==int(orientace):
                    xy_orientace[CB]['delka']=body_sour[i][1]*sin(body_sour[i][2])
                    xy_orientace[CB]['smer']=smer

            # print(mereni_body)
            query='select X,Y from gps_sour where CB is " {} "'.format(str(stanovisko))
            stan_sour=Databaze.sql_query(cesta,query)

            stanovisko = {'X': 0, 'Y': 0}
            stanovisko['X'] = stan_sour[0][0]
            stanovisko['Y'] = stan_sour[0][1]


            body = vypocty.rajon(xy_orientace, stanovisko, mereni_body)


            con=sql.connect(cesta)
            c=con.cursor()
            for i in range(0,len(body)):
                CB=body_sour[i][0]
                X=vypocty.zaokrouhleni(body[CB]['x'],3)
                Y=vypocty.zaokrouhleni(body[CB]['y'],3)
                kod=body_sour[i][4]

                if CB<4000:
                    query='insert into gps_sour (CB, X, Y, kod) values (" {} ", {}, {}, " {} ") '.format(CB, str(X) ,str(Y), kod)

                    c.execute(query)

            con.commit()
            con.close()
            return i
        except IndexError:
            print('Data nejsou soucasti projektu!!')
