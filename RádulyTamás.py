import random
"""torleszto = int(input("Hány hónapig törlesztette a hitelt: "))
ossz = 0
for i in range(torleszto):
    torlesztoreszlet = round(random.randint(12000,17000),-2)
    ossz += torlesztoreszlet
    print(f"Az {i+1}. hónap törlesztőrészlete: {torlesztoreszlet}")

print(f"{torleszto} alatt összesen {ossz} Ft-ot törlesztett.")
"""
"""user = "raduly_tamas"
passwd = "Alma24*"
tries = 0

tfelhasznalo = input("kérem a felhasználónevet: ")
tjelszo = input("kérem a jelszót: ")

while True:
    if tfelhasznalo == user and tjelszo == passwd:
        print("-------- Sikeres belépés! -------- ")
        break
    elif tries <=4:
        
        print("Nincs ilyen felhasználó - jelszó páros a rendszerben, próbálja újra. ")
        print(f"Még {5-tries} próbálkozása van! ")
        tries += 1
        tfelhasznalo = input("kérem a felhasználónevet: ")
        tjelszo = input("kérem a jelszót: ")
    else:
        print("--------- Sikertelen belépés, nincs több lehetősége--------")
        break"""

input("Nyomj entert a dobáshoz!")
tripla = 0
dupla = 0
ossz = 0
while True:
    edob = random.randint(1,6)
    mdob = random.randint(1,6)
    hdob = random.randint(1,6)
    print(f"Első dobás: {edob}   Második dobás: {mdob}", end="   ")
    print(f"Harmadik dobás: {hdob}")
    ossz+=1
    if edob == 6 and mdob == 6 and hdob == 6:
        tripla += 1
        print(f"Dupla dobások száma: {dupla} ")
        print(f"Tripla dobások száma: {tripla} ")
        print(f"Összes dobás: {ossz} ")
        break
    elif edob == mdob and edob == hdob and mdob == hdob:
        tripla += 1
    elif edob == mdob or edob == hdob or mdob == hdob:
        dupla += 1