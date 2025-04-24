from random import randint
be = False
zahlenrate = False
start = 10
admipass = "1234567890ßqwertzuiopüasdfghjklöäyxcvbnm"
liste = []
les = open("speihello.txt","r")
for li in les:
    liste.append(li)
les.close()
lean = open("speihello.txt","w")
lean.write("")
lean.close()
benpas = {}
while True:
    a = input("Erstelle benutzername: ")
    b = input("Passwort: ")
    if a in benpas:
        print("Diesen Benutzername giebt es schon")
    else:
        benpas[a] = b
        break
beenden = False
aus1 = 0
while beenden == False:
    a = input("Benutzername:")
    if a in benpas:
        b = input("Passwort:")
        if benpas[a] == b:
            while True:
                if be == True:
                    beenden = True
                    break
                print("1 Beenden")
                print("2 Sperren")
                print("3 Einkaufsliste")
                print("4 Zahlenratespiel")
                print("5 Passwort ändern")
                print("6 Neuen Account erstellen")
                print("7 Taschenrechner")
                print("8 Konsole")
                print("9 Roulet")
                print("10 Kontostand")
                print("11 Arbeit")
                print("12 Shop")
                print("13 Bouncing")
                aus = input("Was wählst du?: ")
                if aus == "1":
                    beenden = True
                    break
                elif aus == "2":
                    break
                elif aus == "3":
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
                            aus2 = input("Möchtest du wirklich beenden? J/n (Vor dem beenden wird gespeichert)")
                            if aus2 == "n":
                                aus1 = 0
                            elif aus2 == "J":
                                spei = open("speihello.txt","a")
                                for po in liste:
                                    spei.write(po)
                                    spei.write("\n")
                                spei.close()
                                aus1 = 0
                                break
                            else:
                                print("Falsche eingabe")
                        else:
                            print("Falsche eingabe")
                            aus1 = 0
                elif aus == "4":
                    if zahlenrate == True:
                        while True:
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
                    else:
                        print("Du must das Spiel erst Kaufen!")
                elif aus == "5":
                    ini2 = input("Passwort: ")
                    if ini2 == benpas[a]:
                        benpas[a] = input("Was ist das neue Passwort: ")
                    else:
                        print("Falsches Passwort")
                elif aus == "6":
                    ini = input("Passwort:")
                    if ini == benpas[a]:
                        c = input("Neuer Benutzername:")
                        d = input("Neues Passwort:")
                        if c in benpas:
                            print("Dieser Benutzername existiert schon")
                        else:
                            benpas[c] = d
                            print("Benutzer wurde hinzugefügt")
                elif aus == "7":
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
                elif aus == "8":
                    print("help for help")
                    while True:
                        ter = input(a + "@terminal|>")
                        if ter == "drucke":
                            pr = input("|:")
                            print(pr)
                        elif ter == "exit":
                            break
                        elif ter == "sudo":
                            we = input("Systempasswort:")
                            if we == admipass:
                                print(benpas)
                            else:
                                print("Falsches Passwort")
                        elif ter == "elist":
                            print(liste)
                        elif ter == "russrol":
                            while True:
                                print("Russisch Roulet Online")
                                vielPlay = int(input("Wie viele spieler (max. 6): "))
                                if vielPlay > 6:
                                    print("Zu viele Spieler")
                                elif vielPlay == 1:
                                    print("Du kannst nicht alleine spielen!")
                                elif vielPlay == 0:
                                    print("Schisser!")
                                    break
                                else:
                                    zahn = randint(0,5)
                                    if vielPlay == 2:
                                        print("Ein klassisches Duel!")
                                    an = 0
                                    deth = False
                                    while deth == False:
                                        while an < 6:
                                            vert = input("Bereit? ")
                                            if an == zahn:
                                                print("Du bist gestorben!")
                                                deth = True
                                                break
                                            else:
                                                print("Glück gehabt. der Nächste!")
                                                an = an + 1
                                    print("Noch mal spielen")
                                    noch = input("Y/n ")
                                    if noch == "Y":
                                        deth = False
                                    else:
                                        break
                        elif ter == "help":
                            print("exit -beendet die Konsole | drucke -gibt deinen verher eingegebenen Text aus")
                            print("sudo -zeigt alle gespeicherten Benutzer und deren Passwörter | elist -zeigt alles was in der Einkausliste steht")
                            print("russrol -startet Russisch Roulet | shut down -fährt das programm runter")
                            print("money -zeigt dein Kontostand an | ")
                        elif ter == "ha€k":
                            print("hacking...")
                            print("50 50 chance of success")
                            gh = input("Sure? Y/n ")
                            if gh == "Y":
                                print("hacking...")
                                f = randint(1,2)
                                if f == 1:
                                    print("hacking successful")
                                    start = start + 50
                                else:
                                    print("Error")
                                    print("Emergency shut down")
                                    be = True
                                    break
                            else :
                                print("going back")
                        elif ter == "shut down":
                            hj = input("Wirklich beenden? J/n ")
                            if hj == "J":
                                be = True
                                break
                            else :
                                print("Abbruch")
                        elif ter == "money":
                            print(start)
                        else:
                            print("Dieser Befehl existiert nicht.")
                elif aus == "9":
                    print("Willkommen bei Roulet!")
                    bb = input("Spielen? Y/n ")
                    if bb == "n":
                        print("Schade...")
                    elif bb == "Y":
                        while True:
                            geld = int(input("Wie viel möchten sie wetten? "))
                            if geld > start:
                                print("Du hast zu wenig geld.")
                            elif geld == 0:
                                break
                            else:
                                jack = randint(0,6)+randint(0,30)
                                start = start - geld
                                print("Auf was möchtest du wetten")
                                print("1 Rot(x2)")
                                print("2 Schwarz(x2)")
                                print("3 Bestimmte Zahl(x30)")
                                print("4 Grün(x15)")
                                en = int(input(">"))
                                if en == 4:
                                    print("Es ist ...")
                                    print(jack)
                                    if jack == 0 or jack == 36:
                                        print("DU HAST GEWONNEN")
                                        start = start + geld * 15
                                        print("Du hast jetzt ",start,"€.")
                                    else:
                                        print("Oh nein du hast ",geld,"€ verloren")
                                elif en == 1:
                                    print("Es ist ...")
                                    print(jack)
                                    if jack % 2 != 0:
                                        print("Du hast gewonnen!")
                                        start = start + geld * 2
                                        print("Du hast jetzt ",start,"€.")
                                    else:
                                        print("Oh nein du hast ",geld,"€ verloren")
                                elif en == 2:
                                    print("Es ist ...")
                                    print(jack)
                                    if jack % 2 == 0:
                                        print("Du hast gewonnen!")
                                        start = start + geld * 2
                                        print("Du hast jetzt ",start,"€.")
                                    else:
                                        print("Oh nein du hast ",geld,"€ verloren")
                                elif en == 3:
                                    yxc = int(input("Welche Zahl wählst du? "))
                                    if yxc == jack:
                                        print("DU HAST GEWONNEN!!!!!")
                                        start = start + geld * 30
                                        print("DU HAST JETZT ",start,"€!!!")
                                else:
                                    print("Falsche Eingabe")
                elif aus == "10":
                    print(start,"€")
                elif aus == "11":
                    while True:
                        print("1 Additionsaufgaben(1€ pro Aufgabe)")
                        print("2 Subtraktionsaufgaben(1€ pro Aufgabe)")
                        print("3 Multiplikationsaufgaben(1€ pro Aufgabe)")
                        print("4 Beenden")
                        bbb = int(input("Was wählst du? "))
                        if bbb == 1:
                            r1 = randint(10,1000)
                            r2 = randint(10,1000)
                            print(r1,"+",r2)
                            cc = int(input("="))
                            if cc == r1 + r2:
                                print("Richtig! +1€")
                                start = start + 1
                            else:
                                print("Falsch ")
                        elif bbb == 2:
                            r1 = randint(10,1000)
                            r2 = randint(10,1000)
                            print(r1,"-",r2)
                            cc = int(input("="))
                            if cc == r1 - r2:
                                print("Richtig! +1€")
                                start = start +1
                            else :
                                print("Falsch ")
                        elif bbb == 3:
                            r1 = randint(1,20)
                            r2 = randint(1,20)
                            print(r1,"x",r2)
                            cc = int(input("="))
                            if cc == r1 * r2:
                                print("Richtig +1€")
                                start = start + 1
                            else:
                                print("Falsch ")
                        elif bbb == 4:
                            break
                        else :
                            print("Falsche Eingabe")
                elif aus == "12":
                    while True:
                        print("Shop")
                        print("Guthaben:",start,"€")
                        print("1 Beenden")
                        if zahlenrate == False:
                            print("2 Zahlenratespiel 40€")
                        df = int(input("Was wählst du? "))
                        if df == 1:
                            break
                        elif df == 2:
                            if zahlenrate == False:
                                v = input("Kaufen J/n ")
                                if v == "J":
                                    if start >= 40:
                                        zahlenrate = True
                                        start = start - 40
                                        print("Erfolgreich gekauft")
                                    else:
                                        print("Zu wenig geld")
                                elif v == "n":
                                    print("nicht gekauft")
                                else:
                                    print("Falsche Eingabe")
                            else:
                                print("Artikel wurde schon gekauft")
                        elif df == 3:
                            print("Noch nicht fertig")
                elif aus == "13":
                    print("Bouncing")
                    w = int(input("Wie lange?"))
                    ab = 0
                    while ab < w:
                        print(" #")
                        print("  #")
                        print("   #")
                        print("    #")
                        print("     #")
                        print("      #")
                        print("       #")
                        print("      #")
                        print("     #")
                        print("    #")
                        print("   #")
                        print("  #")
                        print(" #")
                        print("#")
                        ab = ab + 1
                else: 
                    print("Falsche eingabe")
        else:
            print("Falsches Passwort")
    else:
        print("Dieser Benutzername existiert nicht") 
