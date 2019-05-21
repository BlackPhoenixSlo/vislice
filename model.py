STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA ='-'
ZMAGA='W'
PORAZ='X' 
bazen_besed=[]
a = 0

def napolnibesede():
    bazen_besed.clear()
    with open ('vaja11/vislice/besede.txt', encoding='utf-8') as vhod:
        for i in vhod:
            bazen_besed.append(i[:-1])

import math
class Igra:

    def __init__(self, geslo):
        self.geslo=geslo.upper()
        self.crke=[]

    def napacne_crke(self):
        return [c for c in self.crke if c not in self.geslo]

    def pravilne_crke(self):
        return [c for c in self.crke if c in self.geslo]
    
    def zmaga(self):
        for x in self.geslo:
            if not x in self.crke:
                return False
        return True

    def poraz(self):
        if len(self.napacne_crke())>STEVILO_DOVOLJENIH_NAPAK:
            return True
        return False

    def pravilni_del_gesla(self):
        s=''
        for i in self.geslo:
            if i in self.pravilne_crke():
                s= s+i
            else:
                s= s+'_'
        return s
    
    def nepravilni_ugibi(self):
        s=''
        for i in self.napacne_crke():
                s= s+i+' '
        return s[:-1]

    def ugibaj(self, crka):
        crka=crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        
        self.crke.append(crka)
        if self.zmaga():
            return ZMAGA
        if self.poraz():
            return PORAZ
        if not crka in self.geslo.upper():
            return NAPACNA_CRKA
        return PRAVILNA_CRKA

import random

def nova_igra():
    napolnibesede()
    return Igra(bazen_besed[int(random.randrange(1,len(bazen_besed)))])



