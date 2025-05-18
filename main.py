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
        start() # Opstart igen

def læseMuligheder():
    brugersvar = input("Vil du læse eller vudere en bog? ").upper() # Spørg bruger
    if brugersvar == "LÆSE" or brugersvar == "LÆS": # Checker svar
        læsBog() # Gå til
    elif brugersvar == "VUDER": #  Checker svar
        vuderBog() # Gå til
    else:
        læseMuligheder()


def læsBog():
    brugersvar = input("Hvilken bog vil du læse? ").strip().upper() #Strip for mere klar string til at sammenligning
    for bog in bøger.values(): # looper dict
        if bog["Titel"].strip().upper() == brugersvar: # Check om brugersvar er det samme som i dict
            print("Titel:", bog["Titel"]) # Printer titel af bog
            print("Forfatter: ", bog["Forfatter"]) # Printer forfatter af bog
            brugersvar = input("Vil du gerne læse den bog? ").upper()
            if brugersvar == "JA": # Checker brugersvar
                print("Du har nu læst den...")
                brugersvar = input("Vil du vuder bogen? ").upper()
                bog["status"] = "læst" # bogen bliver læst inde i dictet
                if brugersvar == "JA": # Checker om
                    brugersvar = input("Hvilken vudering vil du give fra 1-10? ")
                    bog["Vudering"] = brugersvar # opdater variable inde i dict
                    print(bog["Vudering"])
                    start()
                start()
            start()
        else:
            læsBog()




def vuderBog():
    brugersvar = input("Hvilken bog vil du vurdere? ").strip().upper()
    fundet = False
    for bog in bøger.values():
        if bog["Titel"].strip().upper() == brugersvar: # Checker om title matcher med brugers input
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
        bøger[bogID]["Titel"] = title # Vi indlæser title varibalen ind i dict
        registrereEnBogGenre() # Gå til

    else:
        bekræftelse = ""
        registrereEnBog()

def registrereEnBogGenre(): # gerne indskrivning
    genre = input("Hvilken genre er bogen? ")
    bekræftelse = input("Bekræft at du sikker med ja eller nej! Genren er " + genre + " ").upper()
    if bekræftelse == "JA":
        bøger[bogID]["Genre"] = genre
        registrereEnBogForfatter()
    else:
        registrereEnBogGenre()
        bekræftelse = ""


def registrereEnBogForfatter(): # her indskrives forfatter
    forfatter = input("Hvad hedder forfatteren? ")
    bekræftelse = input("Bekræft at du sikker med ja eller nej! Forfatteren er " + forfatter + " ").upper()
    if bekræftelse == "JA":
        bøger[bogID]["Forfatter"] = forfatter
        registrereEnBogISBN()
    else:
        registrereEnBogForfatter()


def registrereEnBogISBN(): # Her laver vi ISBN nummer til bogen
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

def Addbog(): # Vi laver test bog
    bøger[1] = {}  # Her laver vi et nested dict!
    bøger[bogID]["Titel"] = "TestTitel"
    bøger[bogID]["Genre"] = "TestGenre"
    bøger[bogID]["Forfatter"] = "TestForfatter"
    bøger[bogID]["ISBN"] = "1234567891011"
    bøger[bogID]["status"] = "ulæst"
    bøger[bogID]["Vudering"] = 0
    start()

start() # Opstart af programmet

#Note lav hver bog til en class i stedet