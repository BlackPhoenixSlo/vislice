STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA ='-'
ZMAGA='W'
PORAZ='X' 
ZACETEK='Z'
bazen_besed=[]
a = 0

def napolnibesede():
    bazen_besed.clear()
    with open ('besede.txt', encoding='utf-8') as vhod:
        for i in vhod:
            bazen_besed.append(i[:-1])

import math
class Igra:

    def __init__(self, geslo):
        self.geslo=geslo.upper()
        self.crke=[]

    def napacne_crke(self):
        return [c for c in self.crke if c not in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

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



class Vislice:
    def __init__(self):
        self.igre = {}

    def prost_id_igre(self):
        return len(self.igre)

    def nova_igra(self):
        id =self.prost_id_igre()
        self.igre[id]=(nova_igra(),ZACETEK)
        return id

    def ugibaj(self,id_igre,crka):
        igra, _ = self.igre[id_igre]
        poskus = igra.ugibaj(crka)
        self.igre[id_igre] = (igra,poskus)



##################

v= Vislice()
v.nova_igra()
v.nova_igra()
print(v.igre)