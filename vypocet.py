from math import atan2, cos, sin, pi, acos
from sqlite3.dbapi2 import connect

# (X, Y) : LOKALNI SOURADNICE
# (x, y) : SOURADNICE S-JTSK


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


# test_points = {503: {'x': 1044278.81, 'y': 834640.46, 'delka': 289.367, 'smer': 20.3894}, 504: {'x': 1044292.22, 'y': 834620.52, 'delka': 280.67, 'smer': 25.3950}}
# vyp_stanovisko(test_points)


def main():
    xy_orientace = {}
    mereni_body = {}

    with connect('import_do_databaze\\projekt.db') as con:
        cur = con.cursor()

        cur.execute('SELECT (SUBSTR(CB,2,4)) as CB, AVG(X), AVG(Y) FROM gps_sour group by 1;')
        radky = cur.fetchall()
        for CB, x, y in radky:
            CB = int(CB)
            if CB > 4000:
                xy_orientace[CB] = {}
                xy_orientace[CB]['x'] = x
                xy_orientace[CB]['y'] = y

        cur.execute('SELECT Orientace as CB, Delka, Smer from mereni;')
        radky = cur.fetchall()
        for CB, delka, smer in radky:
            CB = int(CB)
            if CB > 4000:
                try:
                    xy_orientace[CB]['delka'] = delka
                    xy_orientace[CB]['smer'] = smer
                except KeyError:
                    xy_orientace[CB] = {}
                    xy_orientace[CB]['delka'] = delka
                    xy_orientace[CB]['smer'] = smer
            else:
                mereni_body[CB] = {}
                mereni_body[CB]['delka'] = delka
                mereni_body[CB]['smer'] = smer

    # print(xy_orientace)
    # print(mereni_body)

    stanovisko = vyp_stanovisko(xy_orientace)
    body = rajon(xy_orientace, stanovisko, mereni_body)

    with connect('import_do_databaze\\projekt.db') as con:
        cur = con.cursor()

        cur.execute('DROP TABLE IF EXISTS vysledky')
        cur.execute('CREATE TABLE IF NOT EXISTS vysledky (id int PRIMARY KEY, CB text,Y double,X double)')
        id = 1
        with open("results.txt", "w") as f:
            f.write("Protokol vypoctu\nBod, Y, X\n")
            for key in body.keys():
                cur.execute(f"INSERT INTO vysledky VALUES ({id},{key},{body[key]['y']},{body[key]['x']})")
                f.write(f"{key}, {body[key]['y']}, {body[key]['x']}\n")
                id += 1


main()

# P1 = [1011445.66, 853704.65]
# P2 = [1011270.35, 852501.72]
# S1 = 703.84
# S2 = 846.61
# print(prot_delek(P1, P2, S1, S2))
