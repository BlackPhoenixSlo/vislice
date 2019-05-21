import model

def izpis_igre(igra):
    text="""
    Število preostalih poskusov:{0}
    {1}
    Napačne črke {2}: {3}
    """.format(
        model.STEVILO_DOVOLJENIH_NAPAK-len(igra.napacne_crke()),
        igra.pravilni_del_gesla(),
        len(igra.napacne_crke()),
        igra.nepravilni_ugibi())
    return text

def izpis_zmage(igra):
    text="Bravo Uganil si geslo {0}".format(igra.geslo)
    return text

def izpis_poraza(igra):
    text="Jooooj, izgubil si, geslo je bilo {0}".format(igra.geslo)
    return text

def zahtevaj_vnos(igra):
    return input("Vnesi črko: ")

def pozeni_vmesnik():
    igra= model.nova_igra()
    b=zahtevaj_vnos(igra)
    print(izpis_igre(igra))

    while 1:
        b=zahtevaj_vnos(igra)
        rez=igra.ugibaj(b)


        if (rez == model.PORAZ):
            print(izpis_zmage(igra))
            return

        if (rez == model.ZMAGA):
            print(izpis_zmage(igra))
            return

        print(izpis_igre(igra))
    
pozeni_vmesnik()