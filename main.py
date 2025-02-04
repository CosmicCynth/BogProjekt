def start():
    print("Halløj med dig, vil registrere en bog eller læse en?")
    brugersvar = input("")
    brugersvar = brugersvar.upper()
    if brugersvar == "REGISTRER":
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
    print("Bekræft at du sikker med ja eller nej! Titlen er " + title)




start()

