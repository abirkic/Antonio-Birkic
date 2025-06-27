import random

class Fahrzeug:
    def __init__(self, marke, kategorie, modell, grundpreis):
        self.marke = marke
        self.kategorie = kategorie
        self.modell = modell
        self.grundpreis = grundpreis
        self.konfiguration = None
        self.zusatzoptionen = []
        self.garantie = 0
        self.rabatt = 0

    def set_konfiguration(self, konfiguration):
        self.konfiguration = konfiguration

    def add_zusatzoption(self, option):
        self.zusatzoptionen.append(option)

    def set_garantie_und_rabatt(self, garantie, rabatt):
        self.garantie = garantie
        self.rabatt = rabatt

    def berechne_endpreis(self):
        kosten_konfig = self.konfiguration.berechne_gesamtpreis() if self.konfiguration else 0
        kosten_optionen = sum(option.preis for option in self.zusatzoptionen)
        endpreis = self.grundpreis + kosten_konfig + kosten_optionen + self.garantie - self.rabatt
        return endpreis

    def drucke_zusammenfassung(self):
        print("\nKonfigurationsübersicht:")
        print(f"Modell: {self.modell} - {self.grundpreis} EUR")
        if self.konfiguration:
            self.konfiguration.drucke_konfiguration()
        if self.zusatzoptionen:
            print("Zusätzliche Optionen:")
            for option in self.zusatzoptionen:
                print(f" - {option.name}: {option.preis} EUR")
        print(f"Garantie: {self.garantie} EUR")
        print(f"Rabatt: -{self.rabatt} EUR")

    def drucke_rechnung(self, bezahlt, restgeld):
        endpreis = self.berechne_endpreis()
        print("\n------------------------------")
        print("          RECHNUNG")
        print("------------------------------")
        print(f"Modell: {self.modell} - {self.grundpreis} EUR")
        if self.konfiguration:
            self.konfiguration.drucke_konfiguration(kurz=True)
        if self.zusatzoptionen:
            for option in self.zusatzoptionen:
                print(f"Zusätzliche Option: {option.name} - {option.preis} EUR")
        print(f"Garantie: {self.garantie} EUR")
        print(f"Rabatt: -{self.rabatt} EUR")
        print(f"Endpreis: {endpreis} EUR")
        print(f"Bezahlt: {bezahlt} EUR")
        print(f"Restgeld: {restgeld} EUR")
        print("------------------------------")
        print("Danke für Ihren Einkauf bei United Cars AG!")
        print("------------------------------")


class Konfiguration:
    def __init__(self):
        self.optionen = {
            "Aussenfarbe": {"Rot": 500, "Gelb": 500, "Blau": 400, "Orange": 600, "Grün": 600, "Violett": 600, "Schwarz": 600, "Weiß": 300, "Grau": 350,
                            "Gelb-Grün": 1200, "Blau-Grün": 1200, "Blau-Violett": 1200, "Rot-Violett": 1200, "Rot-Orange": 1200, "Gelb-Orange": 1200, "Türkis": 600,
                            "Magenta": 600, "Cyan": 600, "Indigo": 600, "Rosa": 600, "Beige": 600, "Braun": 600, "Lila": 600, "Mintgrün": 600, "Ocker": 600},
            "Reifengröße": {"13 Zoll": 0, "14 Zoll": 0, "15 Zoll": 0, "16 Zoll": 200, "17 Zoll": 0, "18 Zoll": 200, "19 Zoll": 400, "20 Zoll": 2500,
                            "21 Zoll": 3400, "22 Zoll": 4000, "23 Zoll": 5000, "24 Zoll": 6000},
            "Sitzausstattung": {"Stoff": 0, "Leder": 5000, "Alcantara": 2000, "Velours": 2000, "Kunstleder": 1500,
                                "Nappaleder": 3500, "Wildleder": 4000, "Textil": 2000, "Mikrofaser": 5000, "Vinyl": 6000},
            "Getriebeart": {"Manuell": 0, "Automatik": 2000, "Halbautomatik": 3000, "CVT (stufenloses Getriebe)": 3200,
                            "Doppelkupplungsgetriebe (DSG)": 3500, "Tiptronic": 2800, "SMG (Sequenzielles manuelles Getriebe)": 4000,
                            "Automatisiertes Schaltgetriebe (ASG)": 3300, "Hydramatic": 2900, "Powershift": 3600}
        }
        self.ausgewaehlte_optionen = {}

    def zufalls_konfiguration(self):
        print("Erstelle eine zufällige Konfiguration...")
        for kategorie, moeglichkeiten in self.optionen.items():
            auswahl = random.choice(list(moeglichkeiten.keys()))
            self.ausgewaehlte_optionen[kategorie] = auswahl
            print(f" - {kategorie}: {auswahl} - {moeglichkeiten[auswahl]} EUR")

    def benutzer_konfiguration(self):
        print("Bitte konfigurieren Sie Ihr Fahrzeug:")
        for kategorie, moeglichkeiten in self.optionen.items():
            print(f"\nVerfügbare Optionen für {kategorie}:")
            for i, (option, preis) in enumerate(moeglichkeiten.items(), 1):
                print(f"{i}. {option} - {preis} EUR")
            while True:
                try:
                    auswahl = int(input(f"Geben Sie die Nummer der gewünschten {kategorie} ein: ")) - 1
                    if 0 <= auswahl < len(moeglichkeiten):
                        gewaehlt = list(moeglichkeiten.keys())[auswahl]
                        self.ausgewaehlte_optionen[kategorie] = gewaehlt
                        break
                    else:
                        print("Ungültige Auswahl, bitte erneut versuchen.")
                except ValueError:
                    print("Bitte eine gültige Zahl eingeben.")

    def berechne_gesamtpreis(self):
        gesamt = 0
        for kategorie, option in self.ausgewaehlte_optionen.items():
            gesamt += self.optionen[kategorie][option]
        return gesamt

    def drucke_konfiguration(self, kurz=False):
        if kurz:
            print(f"Konfigurationskosten: {self.berechne_gesamtpreis()} EUR")
        else:
            print("Gewählte Konfiguration:")
            for kategorie, option in self.ausgewaehlte_optionen.items():
                preis = self.optionen[kategorie][option]
                print(f" - {kategorie}: {option} - {preis} EUR")


class Zusatzoption:
    def __init__(self, name, preis):
        self.name = name
        self.preis = preis


class Zahlung:
    @staticmethod
    def bezahle(endpreis):
        while True:
            try:
                betrag = float(input(f"Bitte zahlen Sie mindestens {endpreis} EUR: "))
                if betrag < endpreis:
                    print("Der Betrag ist zu niedrig.")
                else:
                    restgeld = betrag - endpreis
                    print(f"Bezahlt: {betrag} EUR")
                    print(f"Restgeld: {restgeld} EUR")
                    return betrag, restgeld
            except ValueError:
                print("Ungültige Eingabe, bitte eine Zahl eingeben.")


class FahrzeugKonfigurator:
    def __init__(self):
        self.fahrzeug = None

    def begruessung(self):
        print("Willkommen beim United Cars AG Autokonfigurator!")
        print("Hier können Sie Ihr Traumauto ganz bequem von zu Hause aus konfigurieren")
        print("Lassen Sie uns anfangen!")

    def waehle_automarke(self):
        marken = ["Alfa Romeo", "Aston Martin", "Audi", "Bentley", "BMW", "Bugatti",
        "Dacia", "Ferrari", "Fiat", "Ford", "Jaguar", "Jeep", "Lamborghini",
        "Land Rover", "Maserati", "McLaren", "Mercedes-Benz", "Mitsubishi",
        "Opel", "Peugeot", "Renault", "Rimac", "Rolls-Royce", "SEAT",
        "Skoda", "Subaru", "Suzuki", "Tatra", "Tesla", "Toyota", "Volkswagen",
        "Volvo"]
        print("Bitte wählen Sie eine Automarke:")
        for i, marke in enumerate(marken, 1):
            print(f"{i}. {marke}")
        while True:
            try:
                auswahl = int(input("Auswahl: ")) - 1
                if 0 <= auswahl < len(marken):
                    return marken[auswahl]
                else:
                    print("Ungültige Auswahl, bitte erneut versuchen.")
            except ValueError:
                print("Bitte eine Zahl eingeben.")

    def waehle_kategorie(self):
        kategorien = ["Kleinwagen", "Kompaktklasse", "Mittelklasse", "Oberklasse",
        "Sportwagen", "Cabrios", "Kombis", "Vans", "Geländewagen", "Elektroautos"]
        print("Bitte wählen Sie eine Fahrzeugkategorie:")
        for i, kat in enumerate(kategorien, 1):
            print(f"{i}. {kat}")
        while True:
            try:
                auswahl = int(input("Auswahl: ")) - 1
                if 0 <= auswahl < len(kategorien):
                    return kategorien[auswahl]
                else:
                    print("Ungültige Auswahl, bitte erneut versuchen.")
            except ValueError:
                print("Bitte eine Zahl eingeben.")

    def zeige_modelle_und_preise(self, marke, kategorie):
        # Beispielhafte Modell-Preise
        daten = {
            "Alfa Romeo": {
                       "Kleinwagen": [("MiTo", 15000)],
                     "Mittelklasse": [("Giulia", 29500)],
                    "Kompaktklasse": [("Giulietta", 18000)],
                             "SUVs": [("Stelvio", 45000)],
                       "Sportwagen": [("Giulia", 80000), ("Stelvio Quadrifoglio", 90000)]
},
          "Aston Martin": {
                       "Sportwagen": [("Vantage", 120000), ("DBS Superleggera", 200000), ("DBX", 210000)],
                       "Oberklasse": [("DB11", 150000)]
},
                  "Audi": {
                       "Kleinwagen": [("A1", 23000), ("A2", 23000)],
                    "Kompaktklasse": [("A3", 34000)],
                     "Mittelklasse": [("A4", 38450)],
                       "Oberklasse": [("A6", 54200), ("A7", 69000), ("A8", 93000)],
                       "Sportwagen": [("RS3", 65000), ("RS4", 79000), ("RS5", 86000), ("RS6", 119000), ("RS7", 135000), ("TT RS", 74000), ("R8", 145000)],
                          "Cabrios": [("A5 Cabriolet", 48350)],
                             "SUVs": [("Q2", 28500), ("Q3", 37000), ("Q5", 49000), ("Q7", 67000), ("Q8", 77000)],
                     "Elektroautos": [("e-tron", 52950)]
},
               "Bentley": {
                             "SUVs": [("Bentayga", 197800), ("Bentayga EWB (Extended Wheelbase)", 230000)],
                       "Oberklasse": [("Flying Spur", 250000), ("Flying Spur Mulliner", 280000), ("Flying Spur EWB", 300000)],
                     "Grand Tourer": [("Continental GT", 220000), ("Continental GT Convertible (GTC)", 240000), ("Continental GT Bacalar", 350000)],
               "Klassische Modelle": [("Mulsanne", 300000), ("Bacalar", 350000)],
                    "Sondermodelle": [("Azure", 248000), ("Bentayga Azure", 260000), ("Bentayga S", 275000), ("Bentayga EWB Mulliner", 290000)]
},
                  "BMW": {
                       "Kleinwagen": [("1er Serie", 45000)],
                    "Kompaktklasse": [("2er Serie", 57000)],
                     "Mittelklasse": [("3er Serie", 75000)],
                       "Oberklasse": [("5er Serie", 85000), ("7er Serie", 120000), ("8er Serie", 130000)],
                       "Sportwagen": [("M2", 60000), ("M3", 85000), ("M4", 90000), ("M5", 110000), ("M8", 150000)],
                          "Cabrios": [("4er Serie Convertible", 60000)],
                             "SUVs": [("X1", 45000), ("X3", 65000), ("X5", 85000), ("X6", 95000), ("X7", 120000), ("iX", 77000), ("X3 M", 90000), ("X5 M", 130000)],
                     "Elektroautos": [("i3", 35000), ("i4", 57000), ("iX", 77000), ("i4 M50", 65000)]
}, 
              "Bugatti": {
                       "Sportwagen": [("Chiron", 3399000), ("Divo", 5000000), ("Centodieci", 8600000), ("Bolide", 4000000), ("La Voiture Noire", 12000000),
                                      ("Chiron Super Sport", 3927000), ("Chiron Pur Sport", 3199000), ("Veyron", 1900000), ("Veyron Supersport", 2100000), ("Tourbillion", 2500000)
    ]
},
                "Dacia": {
                       "Kleinwagen": [("Sandero", 10000)],
                              "SUV": [("Duster", 15000)],
                           "Kombis": [("Logan", 10500)]
},
              "Ferrari": {
                       "Sportwagen": [("Portofino", 215000), ("Roma", 220000), ("F8 Tributo", 276000), ("812 Superfast", 339000), ("SF90 Stradale", 430000),
                                      ("Enzo Ferrari", 650000), ("F40", 1200000), ("F50", 1500000), ("F60", 2500000), ("LaFerrari", 1500000), ("296 GTB", 323000),
                                      ("Testarossa", 200000), ("288 GTO", 2500000), ("F12 Berlinetta", 319000), ("Ferrari 599 GTB Fiorano", 317000),
                                      ("Ferrari 812 GTS", 370000), ("Ferrari 488 GTB", 160000), ("Ferrari 348", 140000), ("Ferrari 328", 120000),
                                      ("Ferrari 308", 100000), ("Ferrari 246", 800000), ("Ferrari 250 GTO", 50000000), ("Ferrari 250 GT", 1000000), ("Ferrari 212 Inter", 1200000)
    ]
},
                 "Fiat": {
                       "Kleinwagen": [("500", 12000), ("Panda", 10500)],
                    "Kompaktklasse": [("Tipo", 17000), ("Punto", 15000), ("Abarth 124 Spider", 27000)]
},
                 "Ford": {
                       "Kleinwagen": [("Fiesta", 18000)],
                    "Kompaktklasse": [("Focus", 22000)],
                     "Mittelklasse": [("Mondeo", 28000)],
                       "Oberklasse": [("Edge", 42000)],
                       "Sportwagen": [("Fiesta ST", 25000), ("Focus ST", 32000), ("Mustang GT", 55000), ("Mustang Mach 1", 65000), ("Shelby GT500", 80000)],
                          "Cabrios": [("Mustang Convertible", 45000)],
                           "Kombis": [("Mondeo Turnier", 30000)],
                             "SUVs": [("Kuga", 35000), ("EcoSport", 25000), ("Explorer", 50000)],
                     "Elektroautos": [("Mustang Mach-E", 48000)]
},
               "Jaguar": {
                     "Mittelklasse": [("XE", 45000), ("XF", 60000)],
                       "Oberklasse": [("XJ", 85000)],
                       "Sportwagen": [("F-Type", 75000), ("XE SV Project 8", 150000)],
                             "SUVs": [("E-Pace", 40000), ("F-Pace", 55000), ("I-Pace", 80000)]
},
                 "Jeep": {
                     "Geländewagen": [("Renegade", 24000), ("Compass", 27000), ("Cherokee", 35000),
                                      ("Grand Cherokee", 40000), ("Wrangler", 39000), ("Grand Cherokee Trackhawk", 90000)
    ]
},
          "Lamborghini": {
                       "Sportwagen": [("Huracan", 3399000), ("Aventador", 4000000), ("Urus", 2000000), ("Revuelto", 5000000),
                                      ("350 GT", 1500000), ("Miura", 1200000), ("Espada", 1000000), ("Countach", 800000),
                                      ("Diablo", 600000), ("Murciélago", 500000), ("Gallardo", 400000), ("LM002", 300000)
    ]
},
           "Land Rover": {
                     "Geländewagen": [("Defender", 50000), ("Discovery", 60000), ("Range Rover", 90000),
                                      ("Evoque", 40000), ("Range Rover Sport SVR", 115000)
    ]
},
             "Maserati": {
                     "Mittelklasse": [("Ghibli", 70000)],
                       "Oberklasse": [("Quattroporte", 120000)],
                             "SUVs": [("Levante", 80000)],
                       "Sportwagen": [("Ghibli Trofeo", 115000), ("Levante Trofeo", 125000)]
},
              "McLaren": {
                       "Sportwagen": [("720S", 250000), ("GT", 200000), ("570S", 170000), ("Artura", 200000), ("Senna", 950000)]
},
        "Mercedes-Benz": {
                       "Kleinwagen": [("A-Klasse", 30000)],
                    "Kompaktklasse": [("B-Klasse", 35000), ("C-Klasse", 42000), ("CLA", 40000)],
                     "Mittelklasse": [("E-Klasse", 55000)],
                       "Oberklasse": [("S-Klasse", 94000), ("CLS", 80000)],
                       "Sportwagen": [("A 45 AMG", 55000), ("C 63 AMG", 72000), ("E 63 AMG", 102000), ("S 63 AMG", 140000),("GLA 45 AMG", 65000), ("GLE 63 AMG", 120000), ("AMG GT", 130000)],
                          "Cabrios": [("E-Klasse Cabriolet", 65000)],
                           "Kombis": [("E-Klasse T-Modell", 60000)],
                             "SUVs": [("GLA", 40000), ("GLB", 45000), ("GLC", 50000), ("GLE", 60000), ("GLS", 80000), ("G-Klasse", 130000)],
                     "Elektroautos": [("EQC", 67000), ("EQS", 95000)]
},
           "Mitsubishi": {
                       "Kleinwagen": [("Mirage", 12000)],
                     "Mittelklasse": [("Lancer", 22000)],
                             "SUVs": [("Outlander", 25000), ("Pajero", 30000), ("Eclipse Cross", 24000)],
                       "Sportwagen": [("Lancer Evolution", 38000)]
},
                 "Opel": {
                       "Kleinwagen": [("Corsa", 15000)],
                    "Kompaktklasse": [("Astra", 20000)],
                     "Mittelklasse": [("Insignia", 30000)],
                             "SUVs": [("Mokka", 23000), ("Crossland X", 21000), ("Grandland X", 28000)],
                       "Sportwagen": [("Corsa GSi", 25000)]
},
              "Peugeot": {
                       "Kleinwagen": [("108", 14000), ("208", 16000)],
                    "Kompaktklasse": [("308", 22000)],
                             "SUVs": [("2008", 20000), ("3008", 27000), ("5008", 30000)]
},
              "Renault": {
                       "Kleinwagen": [("Twingo", 13000)],
                    "Kompaktklasse": [("Clio", 15000), ("Megane", 20000)],
                             "SUVs": [("Kadjar", 25000), ("Captur", 18000)],
                     "Elektroautos": [("Zoe", 32000)],
                       "Sportwagen": [("Clio RS", 25000), ("Megane RS", 33000)]
},
                "Rimac": {
                       "Sportwagen": [("Rimac Concept_One", 980000), ("Rimac Concept_S", 1500000), ("Rimac Nevera", 2200000), ("Rimac Nevera R", 2500000)]
},
          "Rolls-Royce": {
                       "Oberklasse": [("Ghost", 250000), ("Phantom", 450000)],
                       "Sportwagen": [("Wraith", 300000), ("Dawn", 320000)],
                             "SUVs": [("Cullinan", 330000)]
},
                 "SEAT": {
                       "Kleinwagen": [("Ibiza", 17000)],
                    "Kompaktklasse": [("Leon", 22000)],
                             "SUVs": [("Arona", 20000), ("Ateca", 25000), ("Tarraco", 30000)],
                       "Sportwagen": [("Leon Cupra", 35000)]
},
               "Skoda": {
                       "Kleinwagen": [("Fabia", 13000)],
                    "Kompaktklasse": [("Octavia", 19000)],
                     "Mittelklasse": [("Superb", 30000)],
                             "SUVs": [("Karoq", 25000), ("Kodiaq", 32000)],
                       "Sportwagen": [("Octavia RS", 35000)]
},
              "Subaru": {
                       "Kleinwagen": [("Impreza", 20000)],
                     "Mittelklasse": [("Legacy", 25000)],
                             "SUVs": [("Outback", 30000), ("Forester", 35000), ("Ascent", 40000)],
                       "Sportwagen": [("WRX STI", 45000)]
},
              "Suzuki": {
                       "Kleinwagen": [("Swift", 16000), ("Ignis", 15000)],
                    "Kompaktklasse": [("Baleno", 18000)],
                             "SUVs": [("Vitara", 24000), ("S-Cross", 26000), ("Jimny", 22000)],
                       "Sportwagen": [("Swift Sport", 21000)]
},
               "Tatra": {
                     "Geländewagen": [("T700", 120000), ("T87", 60000), ("T815", 80000)]
},
               "Tesla": {
                     "Elektroautos": [("Model S", 80000), ("Model 3", 50000), ("Model X", 90000),("Model Y", 60000), ("Model S Plaid", 130000), ("Model 3 Performance", 70000)]
},
              "Toyota": {
                       "Kleinwagen": [("Aygo", 12000), ("Yaris", 15000)],
                    "Kompaktklasse": [("Corolla", 20000)],
                     "Mittelklasse": [("Camry", 24000)],
                       "Oberklasse": [("Avalon", 35000)],
                       "Sportwagen": [("Supra", 50000), ("GR Yaris", 38000), ("86", 29000), ("GR Corolla", 40000)],
                             "SUVs": [("C-HR", 25000), ("RAV4", 30000), ("Highlander", 35000), ("Land Cruiser", 85000)],
                     "Elektroautos": [("Mirai", 50000)],
                           "Kombis": [("Corolla Touring Sports", 22000)]
},
          "Volkswagen": {
                       "Kleinwagen": [("Up!", 14000)],
                    "Kompaktklasse": [("Polo", 17000), ("Golf", 25000)],
                     "Mittelklasse": [("Passat", 32000)],
                       "Oberklasse": [("Arteon", 40000)],
                       "Sportwagen": [("Golf GTI", 35000), ("Golf R", 40000), ("Arteon R", 45000)],
                           "Kombis": [("Passat Variant", 35000)],
                             "SUVs": [("Tiguan", 30000), ("T-Roc", 25000), ("Touareg", 50000)],
                     "Elektroautos": [("ID.3", 30000), ("ID.4", 40000), ("ID. Buzz", 45000)]
},
               "Volvo": {
                       "Kleinwagen": [("V40", 25000)],
                     "Mittelklasse": [("S60", 30000), ("V60", 35000)],
                       "Oberklasse": [("S90", 45000), ("V90", 50000)],
                             "SUVs": [("XC40", 35000), ("XC60", 40000), ("XC90", 50000)],
                     "Elektroautos": [("XC40 Recharge", 60000)],
                       "Sportwagen": [("S60 Polestar Engineered", 70000)]
}



        }
        if marke in daten and kategorie in daten[marke]:
            modelle = daten[marke][kategorie]
            print(f"Verfügbare Modelle für {marke} {kategorie}:")
            for i, (modell, preis) in enumerate(modelle, 1):
                print(f"{i}. {modell} - {preis} EUR")
            return modelle
        else:
            print("Keine Modelle gefunden.")
            return []

    def waehle_modell(self, modelle):
        while True:
            try:
                auswahl = int(input("Bitte wählen Sie ein Modell: ")) - 1
                if 0 <= auswahl < len(modelle):
                    return modelle[auswahl]
                else:
                    print("Ungültige Auswahl.")
            except ValueError:
                print("Bitte eine Zahl eingeben.")

    def konfigurieren_ja_nein(self):
        while True:
            antwort = input("Möchten Sie das Fahrzeug konfigurieren? (Ja/Nein): ").strip().lower()
            if antwort in ["ja", "nein"]:
                return antwort == "ja"
            else:
                print("Bitte mit 'Ja' oder 'Nein' antworten.")

    def weitere_optionen_ja_nein(self):
        while True:
            antwort = input("Möchten Sie weitere Optionen hinzufügen? (Ja/Nein): ").strip().lower()
            if antwort in ["ja", "nein"]:
                return antwort == "ja"
            else:
                print("Bitte mit 'Ja' oder 'Nein' antworten.")

    def waehle_weitere_option(self):
        optionen = {
            "Navigationssystem": 1200,
            "Sitzheizung": 400,
            "Sitzbelüftung": 600,
            "Massagefunktion": 800,
            "Komplettes Optionspaket": 3000
        }
        print("Verfügbare zusätzliche Optionen:")
        for i, (name, preis) in enumerate(optionen.items(), 1):
            print(f"{i}. {name} - {preis} EUR")
        while True:
            try:
                auswahl = int(input("Wählen Sie eine Option: ")) - 1
                if 0 <= auswahl < len(optionen):
                    name = list(optionen.keys())[auswahl]
                    preis = optionen[name]
                    print(f"Sie haben {name} gewählt. Preis: {preis} EUR")
                    return Zusatzoption(name, preis)
                else:
                    print("Ungültige Auswahl.")
            except ValueError:
                print("Bitte eine Zahl eingeben.")

    def berechne_garantie_und_rabatt(self, preis_option):
        garantie = random.choice([500, 1000, 1500])
        rabatt = random.choice([0, 100, 200, 300])
        print(f"Garantie: {garantie} EUR, Rabatt: {rabatt} EUR")
        return garantie, rabatt

    def start(self):
        self.begruessung()
        marke = self.waehle_automarke()
        kategorie = self.waehle_kategorie()
        modelle = self.zeige_modelle_und_preise(marke, kategorie)
        if not modelle:
            print("Programm beendet, da keine Modelle verfügbar sind.")
            return

        modell, grundpreis = self.waehle_modell(modelle)
        self.fahrzeug = Fahrzeug(marke, kategorie, modell, grundpreis)

        if self.konfigurieren_ja_nein():
            konfig = Konfiguration()
            konfig.benutzer_konfiguration()
            self.fahrzeug.set_konfiguration(konfig)
        else:
            konfig = Konfiguration()
            konfig.zufalls_konfiguration()
            self.fahrzeug.set_konfiguration(konfig)

        while self.weitere_optionen_ja_nein():
            option = self.waehle_weitere_option()
            self.fahrzeug.add_zusatzoption(option)

        garantie, rabatt = self.berechne_garantie_und_rabatt(0)
        self.fahrzeug.set_garantie_und_rabatt(garantie, rabatt)

        self.fahrzeug.drucke_zusammenfassung()

        endpreis = self.fahrzeug.berechne_endpreis()

        bezahlt, restgeld = Zahlung.bezahle(endpreis)

        self.fahrzeug.drucke_rechnung(bezahlt, restgeld)


if __name__ == "__main__":
    fk = FahrzeugKonfigurator()
    fk.start()
