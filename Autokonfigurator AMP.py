import random

#Begrüßung
def begruessung():
    print("Willkommen beim United Cars AG Autokonfigurator!")
    print("Hier können Sie Ihr Traumauto ganz bequem von zu Hause aus konfigurieren")
    print("Lassen Sie uns anfangen!")

#Liste der Automarken
def waehle_automarke():
    automarken = [
        "Alfa Romeo", "Aston Martin", "Audi", "Bentley", "BMW", "Bugatti",
        "Dacia", "Ferrari", "Fiat", "Ford", "Jaguar", "Jeep", "Lamborghini",
        "Land Rover", "Maserati", "McLaren", "Mercedes-Benz", "Mitsubishi",
        "Opel", "Peugeot", "Renault", "Rimac", "Rolls-Royce", "SEAT",
        "Skoda", "Subaru", "Suzuki", "Tatra", "Tesla", "Toyota", "Volkswagen",
        "Volvo"
    ]

    while True:
        # Benutzer zur Auswahl einer Automarke auffordern
        print("Bitte wählen Sie eine Automarke:")
        for i, marke in enumerate(automarken, 1):
            print(f"{i}. {marke}")

        try:
            # Benutzer zur Eingabe der Nummer der gewünschten Automarke auffordern
            auswahl = int(input("Geben Sie die Nummer der gewünschten Automarke ein: ")) - 1

            # Überprüfen, ob die Auswahl gültig ist
            if 0 <= auswahl < len(automarken):
                ausgewaehlte_marke = automarken[auswahl]
                print(f"Sie haben {ausgewaehlte_marke} gewählt.")
                return ausgewaehlte_marke
            else:
                print("Ungültige Auswahl. Bitte versuchen Sie es erneut.")
        except ValueError:
            # Fehlerbehandlung bei ungültiger Eingabe
            print("Ungültige Eingabe. Bitte geben Sie eine gültige Zahl ein.")

#Liste der Kategorien
def waehle_kategorie():
    kategorien = [
        "Kleinwagen", "Kompaktklasse", "Mittelklasse", "Oberklasse",
        "Sportwagen", "Cabrios", "Kombis", "Vans", "Geländewagen", "Elektroautos"
    ]

#Wahl der Kategorie
    while True:
        # Benutzer zur Auswahl einer Kategorie auffordern
        print("Bitte wählen Sie eine Kategorie:")
        for i, kategorie in enumerate(kategorien, 1):
            print(f"{i}. {kategorie}")

        try:
            # Benutzer zur Eingabe der Nummer der gewünschten Kategorie auffordern
            auswahl = int(input("Geben Sie die Nummer der gewünschten Kategorie ein: ")) - 1

            # Überprüfen, ob die Auswahl gültig ist
            if 0 <= auswahl < len(kategorien):
                ausgewaehlte_kategorie = kategorien[auswahl]
                print(f"Sie haben {ausgewaehlte_kategorie} gewählt.")
                return ausgewaehlte_kategorie
            else:
                print("Ungültige Auswahl. Bitte versuchen Sie es erneut.")
        except ValueError:
            # Fehlerbehandlung bei ungültiger Eingabe
            print("Ungültige Eingabe. Bitte geben Sie eine gültige Zahl ein.")

#Liste der Modelle mit Preisen
def zeige_modelle_und_preise(automarke, kategorie):
    modelle_preise = {
        "Alfa Romeo":    {"Kleinwagen": {"MiTo": 15000},
                        "Mittelklasse": {"Giulia": 29500},
                       "Kompaktklasse": {"Giulietta": 18000},
                                "SUVs": {"Stelvio": 45000},
                          "Sportwagen": {"Giulia": 80000, "Stelvio Quadrifoglio": 90000}},
        
        "Aston Martin":  {"Sportwagen": {"Vantage": 120000, "DBS Superleggera": 200000, "DBX": 210000},
                          "Oberklasse": {"DB11": 150000}},
        
        "Audi":          {"Kleinwagen": {"A1": 23000}, 
                       "Kompaktklasse": {"A3": 34000}, 
                        "Mittelklasse": {"A4": 38450},
                          "Oberklasse": {"A6": 54200, "A7": 69000, "A8": 93000},
                          "Sportwagen": {"RS3": 65000, "RS4": 79000, "RS5": 86000, "RS6": 119000, "RS7": 135000, "TT RS": 74000, "R8": 145000},
                             "Cabrios": {"A5 Cabriolet": 48350},
                                "SUVs": {"Q2": 28500, "Q3": 37000, "Q5": 49000, "Q7": 67000, "Q8": 77000},
                        "Elektroautos": {"e-tron": 52950}},
        
        "Bentley":             {"SUVs": {"Bentayga": 197800, "Bentayga EWB (Extended Wheelbase)": 230000},
                          "Oberklasse": {"Flying Spur": 250000, "Flying Spur Mulliner": 280000, "Flying Spur EWB": 300000},
                        "Grand Tourer": {"Continental GT": 220000, "Continental GT Convertible (GTC)": 240000, "Continental GT Bacalar": 350000},
                  "Klassische Modelle": {"Mulsanne": 300000, "Bacalar": 350000},
                       "Sondermodelle": {"Azure": 248000, "Bentayga Azure": 260000, "Bentayga S": 275000, "Bentayga EWB Mulliner": 290000}},
        
        "BMW":           {"Kleinwagen": {"1er Serie": 45000},
                       "Kompaktklasse": {"2er Serie": 57000},
                        "Mittelklasse": {"3er Serie": 75000},
                          "Oberklasse": {"5er Serie": 85000, "7er Serie": 120000, "8er Serie": 130000},
                          "Sportwagen": {"M2": 60000, "M3": 85000, "M4": 90000, "M5": 110000, "M8": 150000},
                             "Cabrios": {"4er Serie Convertible": 60000},
                                "SUVs": {"X1": 45000, "X3": 65000, "X5": 85000, "X6": 95000, "X7": 120000, "iX": 77000, "X3 M": 90000, "X5 M": 130000},
                        "Elektroautos": {"i3": 35000, "i4": 57000, "iX": 77000, "i4 M50": 65000}},
       
        "Bugatti":       {"Sportwagen": {"Chiron": 3399000, "Divo": 5000000, "Centodieci": 8600000, "Bolide": 4000000, "La Voiture Noire": 12000000, 
                                         "Chiron Super Sport": 3927000, "Chiron Pur Sport": 3199000, "Veyron": 1900000, "Veyron Supersport": 2100000, 
                                         "Tourbillion": 2500000}},
        
        "Dacia":         {"Kleinwagen": {"Sandero": 10000}, 
                                 "SUV": {"Duster": 15000}, 
                              "Kombis": {"Logan": 10500}},
       
        "Ferrari":       {"Sportwagen": {"Portofino": 215000, "Roma": 220000, "F8 Tributo": 276000, "812 Superfast": 339000, "SF90 Stradale": 430000, 
                                         "Enzo Ferrari": 650000, "F40": 1200000, "F50": 1500000, "F60": 2500000, "LaFerrari": 1500000, "296 GTB": 323000, 
                                         "Testarossa": 200000, "288 GTO": 2500000, "F12 Berlinetta": 319000, "Ferrari 599 GTB Fiorano": 317000, 
                                         "Ferrari 812 GTS": 370000, "Ferrari 488 GTB": 160000, "Ferrari 348": 140000, "Ferrari 328": 120000, 
                                         "Ferrari 308": 100000, "Ferrari 246": 800000, "Ferrari 250 GTO": 50000000, "Ferrari 250 GT": 1000000, 
                                         "Ferrari 212 Inter": 1200000}},
        
        "Fiat":          {"Kleinwagen": {"500": 12000, "Panda": 10500},
                       "Kompaktklasse": {"Tipo": 17000, "Punto": 15000, "Abarth 124 Spider": 27000}},
        
        "Ford":          {"Kleinwagen": {"Fiesta": 18000},
                       "Kompaktklasse": {"Focus": 22000},
                        "Mittelklasse": {"Mondeo": 28000},
                          "Oberklasse": {"Edge": 42000},
                          "Sportwagen": {"Fiesta ST": 25000, "Focus ST": 32000, "Mustang GT": 55000, "Mustang Mach 1": 65000, "Shelby GT500": 80000},
                             "Cabrios": {"Mustang Convertible": 45000},
                              "Kombis": {"Mondeo Turnier": 30000},
                                "SUVs": {"Kuga": 35000, "EcoSport": 25000, "Explorer": 50000},
                        "Elektroautos": {"Mustang Mach-E": 48000}},
        
        "Jaguar":      {"Mittelklasse": {"XE": 45000, "XF": 60000},
                          "Oberklasse": {"XJ": 85000},
                          "Sportwagen": {"F-Type": 75000, "XE SV Project 8": 150000},
                                "SUVs": {"E-Pace": 40000, "F-Pace": 55000, "I-Pace": 80000}},
        
        "Jeep":        {"Geländewagen": {"Renegade": 24000, "Compass": 27000, "Cherokee": 35000, "Grand Cherokee": 40000, "Wrangler": 39000, 
                                         "Grand Cherokee Trackhawk": 90000}},
        
        "Lamborghini":   {"Sportwagen": {"Huracan": 3399000, "Aventador": 4000000, "Urus": 2000000, "Revuelto": 5000000,
                                         "350 GT": 1500000, "Miura": 1200000, "Espada": 1000000, "Countach": 800000,
                                         "Diablo": 600000, "Murciélago": 500000, "Gallardo": 400000, "LM002": 300000}},
        
        "Land Rover":  {"Geländewagen": {"Defender": 50000, "Discovery": 60000, "Range Rover": 90000, "Evoque": 40000, "Range Rover Sport SVR": 115000}},
        
        "Maserati":    {"Mittelklasse": {"Ghibli": 70000},
                          "Oberklasse": {"Quattroporte": 120000},
                                "SUVs": {"Levante": 80000},
                          "Sportwagen": {"Ghibli Trofeo": 115000, "Levante Trofeo": 125000}},
        
        "McLaren":       {"Sportwagen": {"720S": 250000, "GT": 200000, "570S": 170000, "Artura": 200000, "Senna": 950000}},
       
        "Mercedes-Benz": {"Kleinwagen": {"A-Klasse": 30000},
                       "Kompaktklasse": {"B-Klasse": 35000, "C-Klasse": 42000, "CLA": 40000},
                        "Mittelklasse": {"E-Klasse": 55000},
                          "Oberklasse": {"S-Klasse": 94000, "CLS": 80000},
                          "Sportwagen": {"A 45 AMG": 55000, "C 63 AMG": 72000, "E 63 AMG": 102000, "S 63 AMG": 140000, "GLA 45 AMG": 65000, 
                                          "GLE 63 AMG": 120000, "AMG GT": 130000},
                             "Cabrios": {"E-Klasse Cabriolet": 65000},
                              "Kombis": {"E-Klasse T-Modell": 60000},
                                "SUVs": {"GLA": 40000, "GLB": 45000, "GLC": 50000, "GLE": 60000, "GLS": 80000, "G-Klasse": 130000},
                        "Elektroautos": {"EQC": 67000, "EQS": 95000}},
        
        "Mitsubishi":    {"Kleinwagen": {"Mirage": 12000},
                        "Mittelklasse": {"Lancer": 22000},
                                "SUVs": {"Outlander": 25000, "Pajero": 30000, "Eclipse Cross": 24000},
                          "Sportwagen": {"Lancer Evolution": 38000}},
        
        "Opel":          {"Kleinwagen": {"Corsa": 15000},
                       "Kompaktklasse": {"Astra": 20000},
                        "Mittelklasse": {"Insignia": 30000},
                                "SUVs": {"Mokka": 23000, "Crossland X": 21000, "Grandland X": 28000},
                          "Sportwagen": {"Corsa GSi": 25000}},
        
        "Peugeot":       {"Kleinwagen": {"108": 14000, "208": 16000},
                       "Kompaktklasse": {"308": 22000},
                                "SUVs": {"2008": 20000, "3008": 27000, "5008": 30000}},
       
        "Renault":       {"Kleinwagen": {"Twingo": 13000},
                       "Kompaktklasse": {"Clio": 15000, "Megane": 20000},
                                "SUVs": {"Kadjar": 25000, "Captur": 18000},
                        "Elektroautos": {"Zoe": 32000},
                          "Sportwagen": {"Clio RS": 25000, "Megane RS": 33000}},
        
        "Rimac":         {"Sportwagen": {"Rimac Concept_One": 980000, "Rimac Concept_S": 1500000, "Rimac Nevera": 2200000, "Rimac Nevera R": 2500000}},
        
        "Rolls-Royce":   {"Oberklasse": {"Ghost": 250000, "Phantom": 450000},
                          "Sportwagen": {"Wraith": 300000, "Dawn": 320000},
                                "SUVs": {"Cullinan": 330000}},
        
        "SEAT":          {"Kleinwagen": {"Ibiza": 17000},
                       "Kompaktklasse": {"Leon": 22000},
                                "SUVs": {"Arona": 20000, "Ateca": 25000, "Tarraco": 30000},
                          "Sportwagen": {"Leon Cupra": 35000}},
        
        "Skoda":         {"Kleinwagen": {"Fabia": 13000},
                       "Kompaktklasse": {"Octavia": 19000},
                        "Mittelklasse": {"Superb": 30000},
                                "SUVs": {"Karoq": 25000, "Kodiaq": 32000},
                          "Sportwagen": {"Octavia RS": 35000}},
    
        "Subaru":        {"Kleinwagen": {"Impreza": 20000},
                        "Mittelklasse": {"Legacy": 25000},
                                "SUVs": {"Outback": 30000, "Forester": 35000, "Ascent": 40000},
                          "Sportwagen": {"WRX STI", 45000}},
        
        "Suzuki":        {"Kleinwagen": {"Impreza": 20000},
                        "Mittelklasse": {"Legacy": 25000},
                                "SUVs": {"Outback": 30000, "Forester": 35000, "Ascent": 40000},
                          "Sportwagen": {"WRX STI": 45000}},
        
        "Tatra":       {"Geländewagen": {"T700": 120000, "T87": 60000, "T815": 80000}},
        
        "Tesla":       {"Elektroautos": {"Model S": 80000, "Model 3": 50000, "Model X": 90000, "Model Y": 60000, "Model S Plaid": 130000, 
                                         "Model 3 Performance": 70000}},
        
        "Toyota":        {"Kleinwagen": {"Aygo": 12000, "Yaris": 15000},
                       "Kompaktklasse": {"Corolla": 20000},
                        "Mittelklasse": {"Camry": 24000},
                          "Oberklasse": {"Avalon": 35000},
                          "Sportwagen": {"Supra": 50000, "GR Yaris": 38000, "86": 29000, "GR Corolla": 40000},
                                "SUVs": {"C-HR": 25000, "RAV4": 30000, "Highlander": 35000, "Land Cruiser": 85000},
                        "Elektroautos": {"Mirai": 50000},
                              "Kombis": {"Corolla Touring Sports": 22000}},
        
        "Volkswagen":    {"Kleinwagen": {"Up!": 14000},
                       "Kompaktklasse": {"Polo": 17000, "Golf": 25000},
                        "Mittelklasse": {"Passat": 32000},
                          "Oberklasse": {"Arteon": 40000},
                          "Sportwagen": {"Golf GTI": 35000, "Golf R": 40000, "Arteon R": 45000},
                              "Kombis": {"Passat Variant": 35000},
                                "SUVs": {"Tiguan": 30000, "T-Roc": 25000, "Touareg": 50000},
                        "Elektroautos": {"ID.3": 30000, "ID.4": 40000, "ID. Buzz": 45000}},
        
        "Volvo":         {"Kleinwagen": {"V40": 25000},
                        "Mittelklasse": {"S60": 30000, "V60": 35000},
                          "Oberklasse": {"S90": 45000, "V90": 50000},
                                "SUVs": {"XC40": 35000, "XC60": 40000, "XC90": 50000},
                        "Elektroautos": {"XC40 Recharge": 60000},
                          "Sportwagen": {"S60 Polestar Engineered": 70000}},
    }

    # Überprüfen, ob die Automarke und Kategorie in den verfügbaren Modellen und Preisen enthalten sind
    while True:
        if automarke in modelle_preise and kategorie in modelle_preise[automarke]:
            print(f"Verfügbare Modelle und Preise für {automarke} - {kategorie}:")
            for i, (modell, preis) in enumerate(modelle_preise[automarke][kategorie].items(), 1):
                print(f"{i}. {modell}: {preis} EUR")
            return modelle_preise[automarke][kategorie]
        else:
            # Falls keine Modelle verfügbar sind, Benutzer zur Auswahl einer anderen Kategorie auffordern
            print(f"Keine Modelle verfügbar für {automarke} in der Kategorie {kategorie}.")
            kategorie = waehle_kategorie()  # Wähle eine andere Kategorie


def waehle_modell(modelle):
    while True:
        try:
            # Benutzer zur Eingabe der Nummer des gewünschten Modells auffordern
            auswahl = int(input("Geben Sie die Nummer des gewünschten Modells ein:")) - 1
            # Überprüfen, ob die Auswahl gültig ist
            if 0 <= auswahl < len(modelle):
                ausgewaehltes_modell = list(modelle.keys())[auswahl]
                preis = modelle[ausgewaehltes_modell]
                # Benutzer über die gewählte Option informieren
                print(f"Sie haben {ausgewaehltes_modell} gewählt. Der Preis beträgt {preis} EUR.")
                return ausgewaehltes_modell, preis
            else:
                print("Ungültige Auswahl. Bitte versuchen Sie es erneut.")
        except ValueError:
            print("Ungültige Eingabe. Bitte geben Sie eine gültige Zahl ein.")

    
def konfigurieren_ja_nein():
    while True:
        # Benutzer fragen, ob sie das Auto nach ihren Wünschen konfigurieren möchten
        antwort = input("Möchten Sie das Auto nach Ihren Wünschen konfigurieren? (Ja/Nein): ").strip().lower()
        if antwort in ["ja", "nein"]:
            return antwort == "ja"
        else:
            print("Ungültige Eingabe. Bitte antworten Sie mit 'Ja' oder 'Nein'.")


def zufalls_konfiguration():
    # Verfügbare Optionen für die Zufallskonfiguration
    aussenfarben =      {"Rot": 500, "Gelb": 500, "Blau": 400, "Orange": 600, "Grün": 600, "Violett": 600, "Schwarz": 600, "Weiß": 300, "Grau": 350,
                         "Gelb-Grün": 1200, "Blau-Grün": 1200, "Blau-Violett": 1200, "Rot-Violett": 1200, "Rot-Orange": 1200, "Gelb-Orange": 1200,  "Türkis": 600,
                         "Magenta": 600, "Cyan": 600, "Indigo": 600, "Rosa": 600, "Beige": 600, "Braun": 600, "Lila": 600, "Mintgrün": 600, "Ocker": 600}
    
    reifengroessen =    {"13 Zoll": 0, "14 Zoll": 0, "15 Zoll": 0, "16 Zoll": 200, "17 Zoll": 0, "18 Zoll": 200, "19 Zoll": 400, "20 Zoll": 2500, 
                         "21 Zoll": 3400, "22 Zoll": 4000, "23 Zoll": 5000, "24 Zoll": 6000}
    
    sitzausstattungen = {"Stoff": 0, "Leder": 5000, "Alcantara": 2000, "Velours": 2000, "Kunstleder": 1500,
                         "Nappaleder": 3500, "Wildleder": 4000, "Textil": 2000, "Mikrofaser": 5000, "Vinyl": 6000}
    
    getriebearten =     {"Manuell": 0, "Automatik": 2000, "Halbautomatik": 3000, "CVT (stufenloses Getriebe)": 3200, 
                         "Doppelkupplungsgetriebe (DSG)": 3500, "Tiptronic": 2800, "SMG (Sequenzielles manuelles Getriebe)": 4000,
                         "Automatisiertes Schaltgetriebe (ASG)": 3300, "Hydramatic": 2900, "Powershift": 3600}

    # Zufällige Auswahl der Optionen
    aussenfarbe = random.choice(list(aussenfarben.keys()))
    reifengroesse = random.choice(list(reifengroessen.keys()))
    sitzausstattung = random.choice(list(sitzausstattungen.keys()))
    getriebeart = random.choice(list(getriebearten.keys()))

    kosten_aussenfarbe = aussenfarben[aussenfarbe]
    kosten_reifengroesse = reifengroessen[reifengroesse]
    kosten_sitzausstattung = sitzausstattungen[sitzausstattung]
    kosten_getriebeart = getriebearten[getriebeart]

    # Zufällige Auswahl der Konfiguration und deren Kosten anzeigen
    print(f"Zufällige Außenfarbe: {aussenfarbe} - {kosten_aussenfarbe} EUR")
    print(f"Zufällige Reifengröße: {reifengroesse} - {kosten_reifengroesse} EUR")
    print(f"Zufällige Sitzausstattung: {sitzausstattung} - {kosten_sitzausstattung} EUR")
    print(f"Zufällige Getriebeart: {getriebeart} - {kosten_getriebeart} EUR")

    kosten_konfiguration = kosten_aussenfarbe + kosten_reifengroesse + kosten_sitzausstattung + kosten_getriebeart

    return kosten_konfiguration

def benutzer_konfiguration():
    optionen = {
         # Optionen für die Benutzerkonfiguration
        "Aussenfarbe": {"Rot": 500, "Gelb": 500, "Blau": 400, "Orange": 600, "Grün": 600, "Violett": 600, "Schwarz": 600, "Weiß": 300, "Grau": 350,
                        "Gelb-Grün": 1200, "Blau-Grün": 1200, "Blau-Violett": 1200, "Rot-Violett": 1200, "Rot-Orange": 1200, "Gelb-Orange": 1200,  "Türkis": 600,
                        "Magenta": 600, "Cyan": 600, "Indigo": 600, "Rosa": 600, "Beige": 600, "Braun": 600, "Lila": 600, "Mintgrün": 600, "Ocker": 600},
        
        "Reifengröße": {"13 Zoll": 0, "14 Zoll": 0, "15 Zoll": 0, "16 Zoll": 200, "17 Zoll": 0, "18 Zoll": 200, "19 Zoll": 400, "20 Zoll": 2500, 
                        "21 Zoll": 3400, "22 Zoll": 4000, "23 Zoll": 5000, "24 Zoll": 6000},
        
        "Sitzausstattung": {"Stoff": 0, "Leder": 5000, "Alcantara": 2000, "Velours": 2000, "Kunstleder": 1500,
                            "Nappaleder": 3500, "Wildleder": 4000, "Textil": 2000, "Mikrofaser": 5000, "Vinyl": 6000},
        
        "Getriebeart": {"Manuell": 0, "Automatik": 2000, "Halbautomatik": 3000, "CVT (stufenloses Getriebe)": 3200, 
                        "Doppelkupplungsgetriebe (DSG)": 3500, "Tiptronic": 2800, "SMG (Sequenzielles manuelles Getriebe)": 4000,
                        "Automatisiertes Schaltgetriebe (ASG)": 3300, "Hydramatic": 2900, "Powershift": 3600}
    }

    kosten_konfiguration = 0
    ausgewaehlte_optionen = {}

    for kategorie, auswahl_moeglichkeiten in optionen.items():
        # Optionen für jede Kategorie anzeigen
        print(f"Verfügbare Optionen für {kategorie}:")
        for i, (option, preis) in enumerate(auswahl_moeglichkeiten.items(), 1):
            print(f"{i}. {option} - {preis} EUR")

        while True:
            try:
                # Benutzer zur Eingabe der Nummer der gewünschten Option auffordern
                auswahl = int(input(f"Geben Sie die Nummer der gewünschten {kategorie} ein: ")) - 1

                # Überprüfen, ob die Auswahl gültig ist
                if 0 <= auswahl < len(auswahl_moeglichkeiten):
                    ausgewaehlte_option = list(auswahl_moeglichkeiten.keys())[auswahl]
                    # Gewählte Option und deren Preis hinzufügen
                    ausgewaehlte_optionen[kategorie] = ausgewaehlte_option
                    kosten_konfiguration += auswahl_moeglichkeiten[ausgewaehlte_option]
                    break
                else:
                    print("Ungültige Auswahl. Bitte versuchen Sie es erneut.")
            except ValueError:
                print("Ungültige Eingabe. Bitte geben Sie eine gültige Zahl ein.")

    print("Ihre Konfiguration:")
    # Zeige die gewählten Optionen und deren Preise
    for kategorie, option in ausgewaehlte_optionen.items():
        print(f"{kategorie}: {option} - {optionen[kategorie][option]} EUR")

    return kosten_konfiguration


def weitere_optionen_ja_nein():
    while True:
        # Benutzer fragen, ob sie weitere Optionen hinzufügen möchten
        antwort = input("Möchten Sie weitere Optionen hinzufügen? (Ja/Nein): ").strip().lower()
        if antwort in ["ja", "nein"]:
            return antwort == "ja"
        else:
            print("Ungültige Eingabe. Bitte antworten Sie mit 'Ja' oder 'Nein'.")


def waehle_weitere_option():
    weitere_optionen = {
        "Navigationssystem": 1200,
        "Sitzheizung": 400,
        "Sitzbelüftung": 600,
        "Massagefunktion": 800,
        "Komplettes Optionspaket": 3000
    }
  
    while True:
        # Verfügbare zusätzliche Optionen anzeigen
        print("Verfügbare zusätzliche Optionen:")
        for i, (option, preis) in enumerate(weitere_optionen.items(), 1):
            print(f"{i}. {option}: {preis} EUR")

        try:
            # Benutzer zur Eingabe der Nummer der gewünschten Option auffordern
            auswahl = int(input("Geben Sie die Nummer der gewünschten Option ein: ")) - 1

            # Überprüfen, ob die Auswahl gültig ist
            if 0 <= auswahl < len(weitere_optionen):
                ausgewaehlte_option = list(weitere_optionen.keys())[auswahl]
                preis_option = weitere_optionen[ausgewaehlte_option]
                print(f"Sie haben {ausgewaehlte_option} gewählt. Der Preis beträgt {preis_option} EUR.")
                return ausgewaehlte_option, preis_option
            else:
                print("Ungültige Auswahl. Bitte versuchen Sie es erneut.")
        except ValueError:
            print("Ungültige Eingabe. Bitte geben Sie eine gültige Zahl ein.")


def berechne_garantie_und_rabatt(preis_option):
    # Beispielhafte Garantiekosten und Rabattbeträge berechnen
    garantie = random.choice([500, 1000, 1500])  
    rabatt = random.choice([0, 100, 200, 300])  
    print(f"Garantie: {garantie} EUR")
    print(f"Rabatt: {rabatt} EUR")
    return garantie, rabatt

def zusammenfassung(gewaehltes_modell, preis_modell, konfigurationskosten, option, preis_option, garantie, rabatt):
    print("\nKonfigurationsübersicht:")
    # Zusammenfassung der gewählten Konfiguration anzeigen
    print(f"Modell: {gewaehltes_modell} - {preis_modell} EUR")
    print(f"Konfigurationskosten: {konfigurationskosten} EUR")
    print(f"Zusätzliche Option: {option} - {preis_option} EUR")
    print(f"Garantie: {garantie} EUR")
    print(f"Rabatt: -{rabatt} EUR")

def berechne_endpreis(preis_modell, konfigurationskosten, preis_option, garantie, rabatt):
    # Endpreis des konfigurierten Autos berechnen
    endpreis = preis_modell + konfigurationskosten + preis_option + garantie - rabatt
    print(f"\nDer Endpreis Ihres konfigurierten Autos beträgt {endpreis} EUR.")
    return endpreis

def bezahlung(endpreis):
    while True:
        try:
            # Benutzer zur Eingabe des zu zahlenden Betrags auffordern
            betrag = float(input("Bitte geben Sie den zu zahlenden Betrag ein: "))
            if betrag < endpreis:
                print(f"Der Betrag ist zu niedrig. Der zu zahlende Betrag muss mindestens {endpreis} EUR sein.")
                continue
            restgeld = betrag - endpreis
            print(f"Bezahlt: {betrag} EUR")
            print(f"Restgeld: {restgeld} EUR")
            return betrag, restgeld
        except ValueError:
            print("Ungültige Eingabe. Bitte geben Sie eine gültige Zahl ein.")

# Detaillierte Rechnung anzeigen
def rechnung(gewaehltes_modell, preis_modell, konfigurationskosten, option, preis_option, garantie, rabatt, endpreis, betrag, restgeld):
    print("\n------------------------------")
    print("          RECHNUNG")
    print("------------------------------")
    print(f"Modell: {gewaehltes_modell} - {preis_modell} EUR")
    print(f"Konfigurationskosten: {konfigurationskosten} EUR")
    print(f"Zusätzliche Option: {option} - {preis_option} EUR")
    print(f"Garantie: {garantie} EUR")
    print(f"Rabatt: -{rabatt} EUR")
    print(f"Endpreis: {endpreis} EUR")
    print(f"Bezahlt: {betrag} EUR")
    print(f"Restgeld: {restgeld} EUR")
    print("------------------------------")
    print("Danke für Ihren Einkauf bei United Cars AG!")
    print("------------------------------")

# Begrüßung anzeigen
begruessung()

# Automarke wählen
ausgewaehlte_marke = waehle_automarke()

# Kategorie wählen
ausgewaehlte_kategorie = waehle_kategorie()

# Modelle und Preise anzeigen
modelle = zeige_modelle_und_preise(ausgewaehlte_marke, ausgewaehlte_kategorie)

# Modell wählen
if modelle:
    ausgewaehltes_modell, preis_modell = waehle_modell(modelle)
    
    if konfigurieren_ja_nein():
        kosten_konfiguration = benutzer_konfiguration()
    else:
        kosten_konfiguration = zufalls_konfiguration()

    endpreis = preis_modell + kosten_konfiguration
    print(f"Der Endpreis Ihres konfigurierten Autos beträgt {endpreis} EUR.")

    # Weitere Optionen wählen
    if weitere_optionen_ja_nein():
        option, preis_option = waehle_weitere_option()
        garantie, rabatt = berechne_garantie_und_rabatt(preis_option)
    else:
        option, preis_option, garantie, rabatt = None, 0, 0, 0

    # Zusammenfassung und Endpreisberechnung
    zusammenfassung(ausgewaehltes_modell, preis_modell, kosten_konfiguration, option, preis_option, garantie, rabatt)
    endpreis = berechne_endpreis(preis_modell, kosten_konfiguration, preis_option, garantie, rabatt)

    # Bezahlung
    betrag, restgeld = bezahlung(endpreis)

    # Rechnung ausgeben
    rechnung(ausgewaehltes_modell, preis_modell, kosten_konfiguration, option, preis_option, garantie, rabatt, endpreis, betrag, restgeld)