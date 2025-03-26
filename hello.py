blesung = open("hellospeicherungbenutzer.txt","r")
benpas = {}
for i in blesung:
    benpas[i] = i
blesung.close()
while True:
    a = input("Erstelle benutzername: ")
    b = input("Passwort: ")
    if a in benpas:
        print("Diesen Benutzername giebt es schon")
    else:
        benpas[a] = b
        break
liste = []
beenden = False
aus1 = 0
while beenden == False:
    a = input("Benutzername:")
    if a in benpas:
        b = input("Passwort:")
        if benpas[a] == b:
            while True:
                print("1 Beenden")
                print("2 Sperren")
                print("3 Einkaufsliste")
                print("4 Zahlenratespiel")
                print("5 Passwort ändern")
                print("6 Neuen Account erstellen")
                print("7 Taschenrechner")
                aus = int(input("Was wählst du?: "))
                if aus == 1:
                    bspeicherung = open("hellospeicherungbenutzer.txt","w")
                    for a in benpas:
                        bspeicherung.write("\n",a)
                    bspeicherung.close()
                        
                    beenden = True
                    break
                elif aus == 2:
                    break
                elif aus == 3:
                    while True:
                        while aus1 == 0:
                            print("Einkaufsliste")
                            print("1 Hinzufügen")
                            print("2 Entfernen")
                            print("3 Anzeigen")
                            print("4 Beenden")
                            aus1 = int(input("Was wählst du?: "))
                        while aus1 == 1:
                            liste.append(input("Was möchtest du hinzufügen?: "))
                            aus1 = int(input("Willst du noch etwas hinzufügen? Ja = 1 Nein = 0: "))
                        while aus1 == 2:
                            print(liste)
                            liste.remove(input("Was möchtest du entfernen?: "))
                            aus1 = int(input("Möchtest du noch etwas entfernen? 2 = Ja 0 = Nein "))
                        if aus1 == 3:
                            print(liste)
                            aus1 = 0
                        elif aus1 == 4:
                            aus2 = input("Möchtest du wirklich beenden? J/n ")
                            if aus2 == "n":
                                aus1 = 0
                            elif aus2 == "J":
                                aus1 = 0
                                break
                            else:
                                print("Falsche eingabe")
                        else:
                            print("Falsche eingabe")
                            aus1 = 0
                elif aus == 4:
                    while True:
                        from random import randint
                        baum = int(input("Bis zu welcher Möchtest du raten? "))
                        zahl = randint(1,baum)
                        ver = baum + 1
                        hn = 0
                        while ver != zahl:
                            ver = int(input("Dein versuch! "))
                            hn = hn + 1
                            if ver == 1234567890:
                                print(zahl)
                                break
                            elif ver > zahl:
                                print("Kleiner! ")
                            elif ver < zahl:
                                print("Größer! ")
                        print("Richtig!!! ")
                        print("Du hast " + str(hn) + " Versuche gebraucht.")
                        if hn == 1:
                            print("Du hässlicher Cheater!!!")
                        elif int(hn) < 6:
                            if hn != 1:
                                print("Du Glückspilz!")
                        elif hn > 10:
                            print("Du hast aber verloren da du mehr als 10 Versuche gebraucht hast.")
                        aus3 = input("Möchtest du noch mal spielen? J/n: ")
                        if aus3 == "J":
                            print("OK!")
                        elif aus3 == "n":
                            break
                        else:
                            print("Falsche eingabe")
                elif aus == 5:
                    ini2 = input("Passwort: ")
                    if ini2 == benpas[a]:
                        benpas[a] = input("Was ist das neue Passwort: ")
                    else:
                        print("Falsches Passwort")
                elif aus == 6:
                    ini = input("Passwort:")
                    if ini == benpas[a]:
                        c = input("Neuer Benutzername:")
                        d = input("Neues Passwort:")
                        if c in benpas:
                            print("Dieser Benutzername existiert schon")
                        else:
                            benpas[c] = d
                            print("Benutzer wurde hinzugefügt")
                elif aus == 7:
                    while True:
                        ers = float(input("erste Zahl:"))
                        zwei = float(input("zweite Zahl:"))
                        re = input("Welches Rechenzeichen(+,*,-,:,modulo)")
                        if re == "+":
                            print(ers + zwei)
                        elif re == "*":
                            print(ers * zwei)
                        elif re == "-":
                            print(ers - zwei)
                        elif re == ":":
                            print(ers / zwei)
                        elif re == "modulo":
                            print(ers % zwei)
                        else:
                            print("Rechenzeichen nict verfügbar")
                        aus4 = input("Möchtest du noch etwas rechnen? J/n:")
                        if aus4 == "J":
                            print("OK")
                        elif aus4 == "n":
                            break
                        else:
                            print("Falsche eingabe")
                else:
                    print("Falsche eingabe")
        else:
            print("Falsches Passwort")
    else:
        print("Dieser Benutzername existiert nicht")