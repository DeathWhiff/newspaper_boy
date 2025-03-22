import pandas as pd

# Manuelle Zuordnung von Branchen, Typen und Kursbewegungen
def create_companies_dataframe():
    
    # unternehmen mit aktienwerten, branchen, typen und kursbewegungen
    companies = [
        # historische unternehmen
        ("general_electric", 120, "industrie", "niedriges_risiko", "steigend"),
        ("singer_sewing_machines", 8, "konsumgueter", "wachstum", "fallend"),
        ("standard_oil", 250, "energie", "dividende", "stagnierend"),
        ("carnegie_steel", 180, "industrie", "hochrisiko", "fallend"),
        ("ford_motor_company", 300, "industrie", "familiengefuehrt", "steigend"),
        ("bayer_ag", 270, "pharma", "niedriges_risiko", "stagnierend"),
        ("siemens_ag", 350, "industrie", "dividende", "steigend"),
        ("aeg", 220, "technologie", "wachstum", "fallend"),
        ("krupp_ag", 270, "industrie", "hochrisiko", "fallend"),
        ("royal_dutch_shell", 290, "energie", "dividende", "stagnierend"),
        ("coca_cola_company", 310, "konsumgueter", "niedriges_risiko", "steigend"),
        ("procter_gamble", 270, "konsumgueter", "dividende", "stagnierend"),
        ("nestlé", 280, "konsumgueter", "niedriges_risiko", "stagnierend"),
        ("unilever", 260, "konsumgueter", "dividende", "steigend"),
        ("pepsico", 250, "konsumgueter", "wachstum", "fallend"),
        ("dupont", 300, "chemie", "dividende", "steigend"),
        ("ibm", 400, "technologie", "niedriges_risiko", "stagnierend"),
        ("philips", 250, "technologie", "wachstum", "stagnierend"),
        ("panasonic", 220, "technologie", "dividende", "fallend"),
        ("westinghouse_electric", 270, "energie", "hochrisiko", "fallend"),
        ("rolls_royce", 310, "industrie", "dividende", "steigend"),
        ("lloyds_banking_group", 230, "finanzen", "niedriges_risiko", "fallend"),
        ("jp_morgan", 500, "finanzen", "dividende", "stagnierend"),
        ("deutsche_bank", 450, "finanzen", "hochrisiko", "fallend"),
        ("hsbc", 420, "finanzen", "niedriges_risiko", "stagnierend"),
        ("barclays", 380, "finanzen", "wachstum", "fallend"),
        ("american_tobacco_company", 180, "konsumgueter", "dividende", "stagnierend"),
        ("wrigley_company", 150, "konsumgueter", "wachstum", "steigend"),
        ("harley_davidson", 220, "konsumgueter", "hochrisiko", "fallend"),
        ("gillette_company", 210, "konsumgueter", "dividende", "steigend"),
        ("goodyear_tire_rubber_company", 200, "industrie", "niedriges_risiko", "fallend"),
        ("kodak", 100, "technologie", "hochrisiko", "fallend"),
        ("bell_telephone_company", 250, "technologie", "dividende", "stagnierend"),
        ("nokia", 230, "technologie", "wachstum", "stagnierend"),
        ("alstom", 180, "industrie", "dividende", "fallend"),
        ("thyssen_ag", 270, "industrie", "hochrisiko", "fallend"),
        ("lockheed_corporation", 350, "industrie", "niedriges_risiko", "stagnierend"),
        ("boeing", 400, "industrie", "dividende", "steigend"),
        ("northrop_grumman", 380, "industrie", "niedriges_risiko", "stagnierend"),
        ("medica", 370, "pharma", "dividende", "steigend"),
        ("merck", 360, "pharma", "niedriges_risiko", "stagnierend"),
        ("eli_lilly_and_company", 340, "pharma", "wachstum", "stagnierend"),
        ("johnson_johnson", 410, "pharma", "dividende", "steigend"),
        ("heineken", 250, "konsumgueter", "dividende", "fallend"),
        ("anheuser_busch", 270, "konsumgueter", "niedriges_risiko", "stagnierend"),
        ("molson_coors_brewing", 220, "konsumgueter", "wachstum", "fallend"),
        ("louis_vuitton", 400, "konsumgueter", "dividende", "steigend"),
        ("chanel", 450, "konsumgueter", "familiengefuehrt", "stagnierend"),
        ("cartier", 350, "konsumgueter", "familiengefuehrt", "fallend"),
        ("prada", 300, "konsumgueter", "dividende", "steigend"),
        ("hermes", 420, "konsumgueter", "familiengefuehrt", "stagnierend"),
        ("gucci", 370, "konsumgueter", "wachstum", "stagnierend"),
        ("harrods", 180, "einzelhandel", "familiengefuehrt", "fallend"),

        # fiktive unternehmen
        ("eisenbach_maschinenbau", 15, "industrie", "familiengefuehrt", "fallend"),
        ("felgenstein", 12, "finanzen", "hochrisiko", "fallend"),
        ("silberbach_textilien", 18, "konsumgueter", "wachstum", "steigend"),
        ("neuhoff_handelsunion", 23, "konsumgueter", "dividende", "stagnierend"),
        ("kaiser_motorenwerke", 27, "industrie", "familiengefuehrt", "stagnierend"),
        ("nordstrom_bergbau", 32, "energie", "hochrisiko", "fallend"),
        ("hintersee_brauerei", 14, "konsumgueter", "familiengefuehrt", "stagnierend"),
        ("ritterstahl_ag", 30, "industrie", "wachstum", "steigend"),
        ("tannenholz_moebelbau", 11, "konsumgueter", "familiengefuehrt", "stagnierend"),
        ("goldhafen_logistik", 25, "industrie", "niedriges_risiko", "steigend"),
        ("seewald_dampfschifffahrt", 22, "transport", "hochrisiko", "fallend"),
        ("adlerkron_chemie", 28, "chemie", "dividende", "stagnierend"),
        ("blaufeld_pharmaceutics", 35, "pharma", "niedriges_risiko", "steigend"),
        ("rostbruecke_eisenwerke", 24, "industrie", "hochrisiko", "fallend"),
        ("koblenz_energiesysteme", 31, "energie", "wachstum", "steigend"),
        ("bernstein_elektrogeraete", 18, "technologie", "dividende", "stagnierend"),
        ("kronenburg_zementwerke", 20, "industrie", "niedriges_risiko", "steigend"),
        ("feuerstein_gaswerke", 40, "energie", "familiengefuehrt", "fallend"),
        ("wellenberg_papierfabrik", 16, "konsumgueter", "wachstum", "stagnierend"),
        ("schwarzbach_textilwaren", 14, "konsumgueter", "familiengefuehrt", "fallend"),
        ("himmelberg_uhrenmanufaktur", 18, "konsumgueter", "wachstum", "steigend"),
        ("waldgruen_forstwirtschaft", 13, "landwirtschaft", "familiengefuehrt", "stagnierend"),
        ("duenenstadt_baugesellschaft", 21, "bau", "niedriges_risiko", "stagnierend"),
        ("stahlberg_werkzeugfabrik", 27, "industrie", "dividende", "steigend"),
        ("glasheim_optik", 20, "technologie", "wachstum", "stagnierend"),
        ("kupferhain_metallwerke", 25, "industrie", "hochrisiko", "fallend"),
        ("falkenauge_fernglaeser", 17, "konsumgueter", "wachstum", "stagnierend"),
        ("eichenwald_holzhandel", 15, "landwirtschaft", "familiengefuehrt", "steigend"),
        ("loewenstein_automobilwerke", 33, "industrie", "dividende", "steigend"),
        ("eisbach_kuehltechnik", 28, "technologie", "wachstum", "fallend"),
        ("greifenberg_versicherung", 37, "finanzen", "niedriges_risiko", "stagnierend"),
        ("silberwald_juweliere", 19, "konsumgueter", "familiengefuehrt", "steigend"),
        ("mondschein_verlag", 13, "medien", "hochrisiko", "fallend"),
        ("bachlauf_stahlwerke", 22, "industrie", "wachstum", "steigend"),
        ("drachenfels_energie", 34, "energie", "dividende", "fallend"),
        ("windkamm_turbinnenbau", 30, "technologie", "niedriges_risiko", "steigend"),
        ("edelbach_praezisionstechnik", 26, "technologie", "familiengefuehrt", "stagnierend"),
        ("lichttal_elektronik", 29, "technologie", "dividende", "stagnierend"),
        ("steinbruch_baumaschinen", 31, "industrie", "hochrisiko", "fallend"),
        ("kuehnbach_stahlwalzwerke", 32, "industrie", "familiengefuehrt", "steigend"),
        ("adlerschwinge_flugtechnik", 35, "industrie", "niedriges_risiko", "stagnierend"),
        ("wiesengrund_landwirtschaft", 18, "landwirtschaft", "familiengefuehrt", "steigend"),
        ("seidenfaden_weberei", 16, "konsumgueter", "wachstum", "fallend"),
        ("nordwind_dampftechnik", 23, "technologie", "hochrisiko", "fallend"),
        ("sternentaler_banken", 39, "finanzen", "niedriges_risiko", "stagnierend"),
        ("rubingold_schmuckwaren", 20, "konsumgueter", "familiengefuehrt", "stagnierend"),
        ("birkental_maschinenbau", 24, "industrie", "dividende", "steigend"),
        ("hirschgrund_jagdtechnik", 17, "technologie", "wachstum", "fallend"),
    ]



    # DataFrame erstellen
    columns = ["Unternehmen", "Aktienwert", "Branche", "Aktientyp", "Kursbewegung"]
    return pd.DataFrame(companies, columns=columns)
def create_events_dataframe():
    events = [
    # Ereignisse für die Branche "Industrie"
    ("Neue Fabriken eröffnet", "industrie", "very positive", 20),
    ("Produktionsengpass aufgrund von Maschinenausfällen", "industrie", "negative", -10),
    ("Patentstreit um mechanische Spinnmaschine", "industrie", "very negative", -15),
    ("Neue Dampfmaschine in England eingeführt", "industrie", "very positive", 30),
    ("Probleme mit Rohstofflieferanten", "industrie", "negative", -10),
    ("Erfindung einer neuen Webmaschine", "industrie", "very positive", 25),
    ("Maschinen müssen gewartet werden", "industrie", "negative", -5),
    ("Arbeiterstreik in der Textilfabrik", "industrie", "very negative", -20),
    ("Stahl wird aus Deutschland geliefert", "industrie", "positive", 15),
    ("Kohle wird billiger", "industrie", "positive", 15),
    ("Subventionen von der Regierung für neue Maschinen", "industrie", "positive", 15),
    ("Neue Fabriken wurden angekündigt", "industrie", "positive", 10),
    ("Partnerschaft mit einem Rohstofflieferanten", "industrie", "positive", 5),
    ("Fusion mit einer anderen Textilfabrik", "industrie", "very positive", 35),
    ("Mehr Zufuhr an Rohstoffen aus Kolonien", "industrie", "very positive", 30),
    ("Probleme mit Transportwegen", "industrie", "negative", -10),
    ("Produktionskosten steigen durch steigende Rohstoffpreise", "industrie", "negative", -15),
    ("Erfindung der Arbeitshandschuhe", "industrie", "very positive", 15),
    ("Erhöhung der Löhne für Arbeiter", "industrie", "negative", -5),
    ("Neue Maschinen zur Textilproduktion", "industrie", "very positive", 25),
    ("Expansion ins Ausland in europäische Märkte", "industrie", "positive", 10),
    ("Rückruf von fehlerhaften Maschinen", "industrie", "very negative", -25),
    ("Verbesserung der Arbeitsqualität", "industrie", "positive", 15),
    ("Giftige Dämpfe legen das Staatskohlekraftwerk lahm", "industrie", "very negative", -25),

    # Ereignisse für die Branche "Konsumgüter"
    ("Nachfrage nach Textilien steigt", "konsumgueter", "very positive", 20),
    ("Neue Gesundheitsvorschriften für Lebensmittelproduktion", "konsumgueter", "negative", -5),
    ("Werbung für neue Produktlinien gestartet", "konsumgueter", "positive", 15),
    ("Verlust von Marktanteilen im Textilsektor", "konsumgueter", "very negative", -15),
    ("Erfolgreicher Launch einer neuen Textilkollektion", "konsumgueter", "very positive", 25),
    ("Verbraucher boykottieren Fabrikprodukte", "konsumgueter", "very negative", -20),
    ("Preissteigerung bei Stoffen", "konsumgueter", "negative", -10),
    ("Neue Vertriebskanäle für Textilprodukte", "konsumgueter", "positive", 20),
    ("Boom der Nachfrage durch industrielle Revolution im Nahrungsmittelsektor", "konsumgueter", "very positive", 30),
    ("Fusion mit einer großen Einzelhandelskette", "konsumgueter", "very positive", 25),
    ("Eröffnung eines neuen Verkaufsmarktes in der Stadt", "konsumgueter", "positive", 10),
    ("Produktrückruf bei schlechter Textilqualität", "konsumgueter", "very negative", -25),
    ("Verändertes Konsumverhalten in städtischen Gebieten", "konsumgueter", "negative", -5),
    ("Saisonale Nachfrage nach Winterkleidung", "konsumgueter", "positive", 10),
    ("Starke Konkurrenz durch neue Fabriken", "konsumgueter", "negative", -20),
    ("Neue Verpackungsmethoden für Textilien", "konsumgueter", "positive", 10),
    ("Zollvorschriften für Textilimporte verschärft", "konsumgueter", "negative", -15),
    ("Produktinnovationen im Bereich Bekleidung", "konsumgueter", "very positive", 20),
    ("Transportkosten steigen durch schlechte Infrastruktur", "konsumgueter", "negative", -10),
    ("Neue Exportmärkte für Textilien erschlossen", "konsumgueter", "positive", 20),
    ("Einführung von Kundenbindungsprogrammen", "konsumgueter", "positive", 5),

    # Ereignisse für die Branche "Energie"
    ("Steinkohlepreis steigt", "energie", "positive", 15),
    ("Regulierung zur Kohlenutzung verschärft", "energie", "very negative", -20),
    ("Neue Kohlenbergwerke entdeckt", "energie", "very positive", 25),
    ("Investition in Dampfkraftwerke", "energie", "very positive", 30),
    ("Wetterbedingte Unterbrechung der Kohlenförderung", "energie", "negative", -10),
    ("Bau einer neuen Dampfkraftanlage", "energie", "positive", 20),
    ("Umstellung auf effizientere Maschinen", "energie", "very positive", 30),
    ("Zertifikate für qualitativ hochwertige Kohlenförderung erhalten", "energie", "positive", 10),
    ("Sinkende Kohlenproduktion", "energie", "very negative", -20),
    ("Energiekrise durch Kohlenmangel", "energie", "very negative", -30),
    ("Preisregulierung durch die Regierung", "energie", "negative", -25),
    ("Neue Eisenbahnlinie für Kohlelieferung eröffnet", "energie", "positive", 15),
    ("Wettbewerb durch alternative Energiequellen wächst", "energie", "negative", -10),
    ("Fusion zweier Bergbauunternehmen", "energie", "positive", 20),
    ("Investition in Dampflokomotiven", "energie", "very positive", 25),
    ("Kohlenpreise stark gestiegen", "energie", "positive", 15),
    ("Unfall in einer Stahlwerkstatt", "energie", "very negative", -20),
    ("Förderung von erneuerbaren Energiequellen durch die Regierung", "energie", "very positive", 25),
    ("Neue Kohlevorkommen entdeckt", "energie", "positive", 20),
    ("Neue Technologien in der Kohlenverstromung", "energie", "positive", 20),

    # Ereignisse für die Branche "Pharmazeutische Industrie"
    ("Neues Medikament gegen Tuberkulose entwickelt", "pharma", "very positive", 25),
    ("Patent abgelaufen für Heilmittel", "pharma", "negative", -15),
    ("Durchbruch in der medizinischen Forschung", "pharma", "very positive", 20),
    ("Produktionsrückruf aufgrund von Fehlern", "pharma", "very negative", -30),
    ("Neue Partnerschaft mit medizinischen Forschungsinstituten", "pharma", "positive", 15),
    ("Zulassung für neue Schmerzmittel in Mitteleuropa", "pharma", "very positive", 25),
    ("Pharmaunternehmen fusionieren", "pharma", "very positive", 30),
    ("Hohe Nachfrage nach Medikamenten während Epidemien", "pharma", "positive", 20),
    ("Lieferengpässe bei medizinischen Rohstoffen", "pharma", "negative", -20),
    ("Erhöhung der Forschungsausgaben für neue Heilmittel", "pharma", "positive", 10),
    ("Regierung führt neue Vorschriften für Medikamente ein", "pharma", "negative", -15),
    ("Preisregulierung für Medikamente", "pharma", "negative", -10),
    ("Neue Entdeckung von Impfstoffen gegen Krankheiten", "pharma", "very positive", 30),
    ("Erfolgreiche klinische Studie für neues Medikament", "pharma", "very positive", 25),
    ("Patentverlängerung für wichtiges Medikament", "pharma", "very positive", 20),
    ("Kritik an den hohen Preisen für Medikamente", "pharma", "negative", -20),
    ("Expansion in neue Märkte wie Amerika", "pharma", "very positive", 30),
    ("Regierungsauftrag für die Lieferung von Medikamenten", "pharma", "positive", 20),
    ("Erste Impfungen durchgeführt", "pharma", "positive", 10),
    ("Neue Behandlungsmethoden für schwerwiegende Krankheiten vorgestellt", "pharma", "very positive", 25),
    ("Kooperation mit Biotech-Unternehmen zur Forschung", "pharma", "positive", 15),

    # Ereignisse für die Branche "Finanzen"
    ("Zinssätze sinken, Kredite werden günstiger", "finanzen", "positive", 15),
    ("Fusion von zwei großen Banken angekündigt", "finanzen", "very positive", 25),
    ("Regulatorische Probleme im Bankensektor", "finanzen", "very negative", -20),
    ("Erstes Aktienunternehmen", "finanzen", "positive", 10),
    ("Bankenpolitik gelockert", "finanzen", "negative", -10),
    ("Wirtschaftlicher Aufschwung fördert Finanzmärkte", "finanzen", "very positive", 30),
    ("Neue Papierwährung eingeführt", "finanzen", "very positive", 20),
    ("Neue Anlagestrategien erfolgreich", "finanzen", "very positive", 25),
    ("Kreditvergabe nimmt zu", "finanzen", "positive", 15),
    ("Zinserhöhung durch die Zentralbank", "finanzen", "negative", -15),
    ("Steigende Banküberfälle auf Banken", "finanzen", "very negative", -25),
    ("Neue Finanzprodukte für Fabriken eingeführt", "finanzen", "positive", 10),
    ("Kapitalerhöhung durch Bank im Aufschwung", "finanzen", "very positive", 20),
    ("Erfolgreicher Börsengang einer Bank", "finanzen", "very positive", 30),
    ("Steuergesetzgebung verändert", "finanzen", "negative", -15),
    ("Bankenfusion in Verhandlung", "finanzen", "positive", 25),
    ("Investitionen in Kohlenminen und Maschinen", "finanzen", "positive", 10),
    ("Geld verliert an Wert", "finanzen", "negative", -20),
    ("Bessere Quartalszahlen als erwartet", "finanzen", "positive", 20),
    ("Neue Kooperation mit Zahlungssystemen", "finanzen", "positive", 10),
    ("Großer Brandt im Bankenviertel", "finanzen", "very negative", -25),
]


    # DataFrame erstellen
    columns = ["description", "branche", "impact", "change"]
    return pd.DataFrame(events, columns=columns)

# CSV speichern
def save_to_csv(df, filename="discord_bot/boerse.csv"):
    df.to_csv(filename, index=False, encoding="utf-8")
    print(f"CSV-Datei '{filename}' erfolgreich erstellt!")
    
def save_to_csv_events(df, filename="discord_bot/events.csv"):
    df.to_csv(filename, index=False, encoding="utf-8")
    print(f"CSV-Datei '{filename}' erfolgreich erstellt!")

# Hauptprogramm
if __name__ == "__main__":
    df = create_companies_dataframe()
    df_events = create_events_dataframe()
    save_to_csv(df)
    save_to_csv_events(df_events)
    print(df)