def start():
    print("Halløj med dig, vil registrere en bog eller læse en?")
    brugersvar = input("")
    brugersvar = brugersvar.upper()
    if brugersvar == "REGISTRER" or "REG":
        registrereEnBog()
    elif brugersvar == "LÆSE":
        læse()
    else:
        print("FORKERT PRØV IGEN")
        start()


def læse():
    print("Læse")

def registrereEnBog():
    title = input("Hvad er navnet på bogen?")
    title = str(title)
    bekræftelseAfTitle = input("Bekræft at du sikker med ja eller nej! Titlen er " + title)
    bekræftelseAfTitle = bekræftelseAfTitle.upper()
    if bekræftelseAfTitle == "JA":
        registrereEnBogGenre()
    else:
        registrereEnBog()



def registrereEnBogGenre():
    print("erkgpoerogore")



start()

