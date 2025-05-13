bøger = {} # tomt dict til at beholde alt for data
bogID = 1 #

def start():
    brugersvar = input("Halløj med dig, vil registrere en bog eller læse/vuder en? ").upper() # får bruger input
    if brugersvar == "REGISTRER" or brugersvar == "REG": # Check efter bruger svar
        brugersvar = "" # For at gøre brugersvar tom
        registrereEnBog() # Gå til
    elif brugersvar == "LÆSE" or brugersvar == "LÆS" or brugersvar == "VUDER": # Checker brugers svar
        brugersvar = ""
        læseMuligheder() # gå til
    elif brugersvar == "TEST": # checker igen
        brugersvar = "" # For at gøre brugersvar tom
        Addbog() # gå til
    else:
        brugersvar = "" # For at gøre brugersvar tom
        print("FORKERT PRØV IGEN") # Forkert
        start() # Opstart på

def læseMuligheder():
    brugersvar = input("Vil du læse eller vudere en bog? ").upper() #
    if brugersvar == "LÆSE" or brugersvar == "LÆS":
        læsBog()
    elif brugersvar == "VUDER":
        vuderBog()


def læsBog():
    brugersvar = input("Hvilken bog vil du læse? ").strip().upper()
    for bog in bøger.values():
        if bog["Titel"].strip().upper() == brugersvar:
            print("Bog fundet:")
            print("Titel:", bog["Titel"])
            print("Forfatter: ", bog["Forfatter"])
            brugersvar = input("Vil du gerne læse den bog? ").upper()
            if brugersvar == "JA":
                print("Du har nu læst den...")
                brugersvar = input("Vil du vuder bogen? ").upper()
                bog["status"] = "læst"
                if brugersvar == "JA":
                    brugersvar = input("Hvilken vudering vil du give fra 1-10? ")
                    bog["Vudering"] = brugersvar
                    print(bog["Vudering"])
                    start()
            start()




def vuderBog():
    brugersvar = input("Hvilken bog vil du vurdere? ").strip().upper()
    fundet = False
    for bog in bøger.values():
        if bog["Titel"].strip().upper() == brugersvar:
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
        vuderBog()





def registrereEnBog():
    title = input("Hvad er navnet på bogen? ")
    title = str(title)
    bekræftelse = input("Bekræft at du sikker med ja eller nej! Titlen er " + title + " ").upper()
    if bekræftelse == "JA":
        bøger[bogID] = {} # Her laver vi et nested dict!
        bøger[bogID]["Titel"] = title
        registrereEnBogGenre()

    else:
        bekræftelse = ""
        registrereEnBog()

def registrereEnBogGenre():
    genre = input("Hvilken genre er bogen? ")
    bekræftelse = input("Bekræft at du sikker med ja eller nej! Genren er " + genre + " ").upper()
    if bekræftelse == "JA":
        bøger[bogID]["Genre"] = genre
        registrereEnBogForfatter()
    else:
        registrereEnBogGenre()
        bekræftelse = ""


def registrereEnBogForfatter():
    forfatter = input("Hvad hedder forfatteren? ")
    bekræftelse = input("Bekræft at du sikker med ja eller nej! Forfatteren er " + forfatter + " ").upper()
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