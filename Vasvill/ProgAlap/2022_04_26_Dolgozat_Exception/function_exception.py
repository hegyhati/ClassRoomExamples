class NincsKedv(Exception):
    pass
class DiakKirohan(Exception):
    pass

import random

def Mirko_kapcsold_fel_a_lampat():
    print('Mirko: meh...')
    kedv = random.randint(1,3)
    if kedv == 1:
        print("Mirko: Ok, felkapcsolom.")
    elif kedv == 2:
        print("Mirko: nincs kedvem.")
        raise NincsKedv
    elif kedv == 3:
        print("Mirko: elegem van, leptem.")
        raise DiakKirohan('Mirko') 
    print('Mirko: fel van kapcsolva!')

def Gabor_kapcsold_fel_a_lampat():
    print('Gabor: ertem, mindjart...')
    siker = False
    while not siker:
        try:
            print('Gabor: Mirko, kapcsold fel a lampat.')
            Mirko_kapcsold_fel_a_lampat()
            siker = True
        except NincsKedv:
            print("Gabor: Mirko, nem erdekel.")
    print('Gabor: fel van kapcsolva!')

def Norbi_kapcsold_fel_a_lampat():
    print('Norbi: ertem, mindjart...')
    print('Norbi: Gabor, kapcsold fel a lampat.')
    Gabor_kapcsold_fel_a_lampat()
    print('Norbi: fel van kapcsolva!')

try:
    print('Mate: Norbi, kapcsold fel a lampat.')
    Norbi_kapcsold_fel_a_lampat()
    print('Mate: Koszi hogy felkapcsoltatok a lampat.')
except DiakKirohan as student:
    print(f'Mate: Beirom {student}-t hianyzonak, es maradunk akkor sotetben.')