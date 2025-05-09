bøger = {}
bogID = 1

def start():
    brugersvar = input("Halløj med dig, vil registrere en bog eller læse en? ")
    brugersvar = brugersvar.upper() # VI laver svaret til uppercase for mindre fejl
    if brugersvar == "REGISTRER" or brugersvar == "REG":
        brugersvar = ""
        registrereEnBog()
    elif brugersvar == "LÆSE" or brugersvar == "LÆS":
        brugersvar = ""
        læse()
    elif brugersvar == "TEST":
        brugersvar = ""
        Addbog()
    else:
        brugersvar = ""
        print("FORKERT PRØV IGEN")
        start()


def læse():
    for bogID, bog in bøger.items():
        print(f"Bog ID: {bogID}")
        for key, value in bog.items():
            print(f"{key}: {value}")
    læseMuligheder()

def læseMuligheder():
    brugersvar = input("Vil du læse eller vudere en bog? ")
    brugersvar = brugersvar.upper()
    if brugersvar == "LÆSE" or brugersvar == "LÆS":
        læsBog()
    elif brugersvar == "VUDER":
        vuderBog()


def læsBog():
    print("læse!!")



def vuderBog():
    brugersvar = input("Hvilken bog vil du vurdere? ").strip().lower()
    fundet = False
    for bog in bøger.values():
        if bog["Titel"].strip().lower() == brugersvar:
            print("Bog fundet:")
            print("Titel:", bog["Titel"])
            print("Vurdering:", bog["Vudering"])
            fundet = True
            brugersvar = input("Hvilken vudering vil du give fra 1-10? ")
            bog["Vudering"] = brugersvar
            print(bog["Vudering"])
            start()
    if not fundet:
        print("Ingen bog med den titel blev fundet.")





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
        bøger[bogID]["Vudering"] = 0
        print("korrekt din bog er nu indlæst!")
        bogID += 1
        print(bøger)
        start()
    else:
        print("FORKERT")
        registrereEnBogISBN()

def Addbog():
    bøger[1] = {}  # Her laver vi et nested dict!
    bøger[bogID]["Titel"] = "TestTitel"
    bøger[bogID]["Genre"] = "TestGenre"
    bøger[bogID]["Forfatter"] = "TestForfatter"
    bøger[bogID]["ISBN"] = "1234567891011"
    bøger[bogID]["status"] = "ulæst"
    bøger[bogID]["Vudering"] = 0
    start()


start()

#Note lav hver bog til en class i stedet