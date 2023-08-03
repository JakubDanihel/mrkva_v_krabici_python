
import random

print("""
      Mrkva v krabici je hra pre 2 hracov. Pozostava z 2 krabic a jednej mrkvy. Mrkva je nahodne vlozena do jedej z krabic. Nasledne su pre hracov rozdelene krabice a potom je do jendej z krabic umiestnena mrkva. Je nahodne zvoleny jeden z hracov co sa pozrie do svojej krabice pricom druhy hrac sa nepozera. Potom sa hrac co vyberal ako prvy rozhodne ci povie jednu z dvoch moznosti: "Mrkva je v mojej krabici." alebo "Mrkva nie je v mojej krabici". Nasledne sa druhy hrac rozhodne ci zmeni krabice alebo nie. Vyhra ten hrac ktory ziska mrkvu.
      """)

input("Stlac enter pre pokracovanie: ")

#zadanie mien hracov
hrac1 = input("Zadaj meno prveho hraca: ")
hrac2 = input("Zadaj meno druheho hraca: ")

menoHraca = hrac1[:11].center(11) + "    " + hrac2[:11].center(11)

#vykreslenie krabic
print("""Tu su dve krabice:
       __________      __________
      /         /|    /         /|
     +---------+ |   +---------+ |
     | CERVENA | |   |  ZLATA  | |
     | KRABICA | /   | KRABICA | /
     +---------+/    +---------+/ 
 """)

print()
print(menoHraca)
print()

#urcenie kto ma aku krabicu
print(hrac1 + ", mas cervenu krabicu.")
print(hrac2 + ", mas zlatu krabicu.")
print()

#hrac1 sa pozrie do krabice a druhy hrac sa nebude pozerat
print(hrac1 + ", pozries sa do svojej krabice.")
print(hrac2.upper() + ", zavri oci a nepozeraj sa!")
input("Ked " + hrac2 + " sa nebude pozerat stlac enter.")
print()

#urcenie ci hrac1 ma alebo nema mrkvu v krabici
print(hrac1 + " tu je obsah tvojej krabice.")

if random.randint(1, 2) == 1:
    mrkvaPrvaKrabica = True
else:
    mrkvaPrvaKrabica = False

if mrkvaPrvaKrabica:
    print("""
        __________
       |    WW    |
       |    WW    |
       |____||____|      __________
      /     ||   /|    /         /|
     +----------+ |   +---------+ |
     | CERVENA  | |   |  ZLATA  | |
     | KRABICA  | /   | KRABICA | /
     +----------+/    +---------+/ 
          (MRKVA!)""")
    print(hrac1)
else:
    print("""
        __________
       |          |
       |          |
       |__________|      __________
      /          /|    /         /|
     +----------+ |   +---------+ |
     | CERVENA  | |   |  ZLATA  | |
     | KRABICA  | /   | KRABICA | /
     +----------+/    +---------+/ 
    (Ziadna MRKVA!)""")

input("Stlac enter pre pokracovanie: ")

#zvolenie jednej z moznosti
print()
print(hrac1 + "povie jednu z nasledujucich viet pre " + hrac2 + ".")
print(" 1) Mrkva je v moje krabici.")
print(" 2) Mrkva nie je v moje krabici.")
print()
input("Stlac enter pre pokracovanie: ")

print()
print(hrac2 + ", chces zmenit krabice? ANO/NIE")

while True:
    odpoved = input("> ").upper()
    
    if not(odpoved.startswith("A") or odpoved.startswith("N")):
        print(hrac2 + ", prosim napis ANO alebo NIE.")
    else:
        break
    
prvaKrabica = "CERVENA "
druhaKrabica = "ZLATA "

#logika pre vymenie krabice
if odpoved.startswith("Y"):
    mrkvaPrvaKrabica = not mrkvaPrvaKrabica
    prvaKrabica, druhaKrabica = druhaKrabica, prvaKrabica
    
print("""
       __________      __________
      /         /|    /         /|
     +---------+ |   +---------+ |
     | {}| |   |  {} | |
     | KRABICA | /   | KRABICA | /
     +---------+/    +---------+/ 
      """.format(prvaKrabica, druhaKrabica))
print(menoHraca)

input("Stlac enter pre odhalenie vitaza ")
print()

if mrkvaPrvaKrabica:
    print("""
        __________
       |    WW    |
       |    WW    |
       |____||____|      __________
      /     ||   /|    /         /|
     +----------+ |   +---------+ |
     | {} | |   |  {} | |
     | KRABICA  | /   | KRABICA | /
     +----------+/    +---------+/ 
        """.format(prvaKrabica, druhaKrabica))
    
else:
    print("""
                        __________
                        |  WW     |
                        |  WW     |
        __________      |__||_____|
      /          /|    /   ||    /|
     +----------+ |   +---------+ |
     | {} | |   |  {} | |
     | KRABICA  | /   | KRABICA | /
     +----------+/    +---------+/ 
        """.format(prvaKrabica, druhaKrabica))
    
    
print(menoHraca)

#vypisanie vytaza
if mrkvaPrvaKrabica:
    print(hrac1 + " je vitaz!")
else:
    print(hrac2 + " je vitaz!")
    
print("Dakujem za hru!")
    
    