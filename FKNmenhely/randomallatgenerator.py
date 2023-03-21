from random import randint, choice
import datetime

x= datetime.datetime.now()

with open('allatoknevei.txt', 'r', encoding="utf-8") as f:
    allatnevek = f.readlines()
    
with open('kutyafajtak.txt', 'r', encoding="utf-8") as f:
    fajok = f.readlines()


with open('megjegyzes.txt', 'r', encoding="utf-8") as f:
    megjegyzes1 = f.readlines()






kutyak = []
for i in range(1, 250):
    allat_nev = allatnevek[randint(0, len(allatnevek)-1)].rstrip()
    szul_ev = f"{randint(2015, 2020)}-{randint(1, 12)}-{randint(1, 28)}"
    
    
    
    
    neme = choice(["kan", "szuka"])
    kutya_fajok = fajok[randint(0, len(fajok)-1)].rstrip() #tipus volt a kutya_fajok
    eu_allapot = choice(["egészséges", "közepes","rossz"])
    ivar_ivartalanitott = randint(0,1)
    suly = randint(1,30)
    fog_allapot = choice(["egészséges", "közepes","rossz"])
    testi_allapot = choice(["egészséges", "közepes","rossz"])
    #ismerteto resz
    
    ismertetojegyek = choice(["kicsi", "közepes","nagy"])
    ismertetojegyek2 = choice(["fekete", "barna","fehér","szürke","vörös","arany","sárga","tigriscsíkos","foltos"])
    ismertetojegyek3 = choice(["fekete", "barna","rózsaszín","sötétbarna","vörös"])
    ismertetojegyek4 = choice(["kék", "barna","zöld"])
    
    #megjegyzes 
    megjegyzes = megjegyzes1[randint(0, len(megjegyzes1)-1)].rstrip()
   
#-------------------------
    chip = randint(0,1)
    orokbeadas = randint(0,1)
    befogadas_datuma = f"{randint(2021, 2023)}-{randint(1, 12)}-{randint(1, 28)}"
    
    #---------------csv-be------
    kutya = f"{i};{allat_nev};{szul_ev};{x.year-int(szul_ev[:4])};{neme};{kutya_fajok};{eu_allapot};{ivar_ivartalanitott};{suly};{fog_allapot};{testi_allapot};{ismertetojegyek} {ismertetojegyek2} {ismertetojegyek3} {ismertetojegyek4};{megjegyzes};{chip};{orokbeadas};{befogadas_datuma}"
    kutyak.append(kutya)

    
with open('kutyak.csv', 'w', encoding="utf-8") as f:
    for kutya in kutyak:
        f.write(f"{kutya}\n")