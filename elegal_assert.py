def testat_string(x):
    if x == "eLegal ist toll!":
        print("Richtig!")
    elif type(x) != type("test"):
        print("Es wurde keine Zeichenkette eingegeben.\n Wurden die Anfuehrungszeichen vergessen?")
    elif (type(x) == type("test")) and (x != "eLegal ist toll!"):
        print("Der ausgegebene Text war leider falsch :(")
    elif (type(x) == type("test")) and (x.upper() == "eLegal ist toll!".upper()):
        print("Gross- und Kleinschreibung ist wichtig!")


def klausurenschnitt_check(x):
    print(x)
    if x == 7:
        print("Korrekt der Schnitt ist 7")
        return
    else:
        print("Dein berechneter Schnitt war falsch")
        return


def write_a_function_check(x):
    def type_check():
        pass

    if type(x) != type(type_check):
        print('Du hast keine Funktion deklariert. Hast du an das "def" gedacht?')

    else:
        print("Super, du hast erfolgreich eine Funktion deklariert")