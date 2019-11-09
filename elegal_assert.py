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

def check_string_for_elegal(string):
    if string == "eLegal ist ein toller Verein, denn er stellt Bier.\nIch möchte nicht in dieser Zeile stehen.":
        print("Richtig !")
    else:
        print('Dein Input scheint falsch. Kleiner Tipp.\nEin Satz möchte gerne aus seiner Zeile in die Zeile darunter verschoben werden. In eine "Newline"')

def check_for_right_list(x):
    if type(x) == type([]):
        print("Du hast die komplette Liste ausgewählt. Denk an den Index.")
        return

    if x == "JURA":
        print("Super, alles richtig gemacht.")
        return
    else:
        if type(x) == str:
            print("Falsches Element. Dein gewähltes Element ist {}.".format(x))
            return
        else:
            print("Irgendetwas ist falsch.")
            return