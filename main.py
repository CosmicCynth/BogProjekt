bøger = {}
bogID = 1

def start():
    brugersvar = input("Halløj med dig, vil registrere en bog eller læse en?")
    brugersvar = brugersvar.upper() # VI laver svaret til uppercase for mindre fejl
    if brugersvar == "REGISTRER" or brugersvar == "REG":
        brugersvar = ""
        registrereEnBog()
    elif brugersvar == "LÆSE" or brugersvar == "LÆS":
        brugersvar = ""
        læse()
    else:
        brugersvar = ""
        print("FORKERT PRØV IGEN")
        start()


def læse():
    for bogID, bog in bøger.items():
        print(f"Bog ID: {bogID}")
        for key, value in bog.items():
            print(f"{key}: {value}")





def registrereEnBog():
    title = input("Hvad er navnet på bogen? ")
    title = str(title)
    bekræftelse = input("Bekræft at du sikker med ja eller nej! Titlen er " + title + " ")
    bekræftelse = bekræftelse.upper()
    if bekræftelse == "JA":
        bøger[bogID] = {} # Her laver vi et nested dict!
        bøger[bogID]["Titel"] = title
        registrereEnBogGenre()

    else:
        bekræftelse = ""
        registrereEnBog()

def registrereEnBogGenre():
    genre = input("Hvilken genre er bogen? ")
    bekræftelse = input("Bekræft at du sikker med ja eller nej! Genren er " + genre + " ")
    bekræftelse = bekræftelse.upper()
    if bekræftelse == "JA":
        bøger[bogID]["Genre"] = genre
        registrereEnBogForfatter()
    else:
        registrereEnBogGenre()
        bekræftelse = ""


def registrereEnBogForfatter():
    forfatter = input("Hvad hedder forfatteren? ")
    bekræftelse = input("Bekræft at du sikker med ja eller nej! Forfatteren er " + forfatter + " ")
    bekræftelse = bekræftelse.upper()
    if bekræftelse == "JA":
        bøger[bogID]["Forfatter"] = forfatter
        registrereEnBogISBN()
    else:
        registrereEnBogForfatter()


def registrereEnBogISBN():
    global bogID
    ISBN = input("Hvad er ISBN koden? (Den skal være 13 cifre) ")
    ISBN = str(ISBN)
    if len(ISBN) == 13:
        bøger[bogID]["ISBN"] = ISBN
        bøger[bogID]["status"] = "ulæst"
        print("korrekt din bog er nu indlæst!")
        bogID += 1
        print(bøger)
        start()
    else:
        print("FORKERT")
        registrereEnBogISBN()



start()
