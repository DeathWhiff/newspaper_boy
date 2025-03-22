import os
import discord
from dotenv import load_dotenv
import random
from datetime import datetime, timedelta
import locale
import json
import pandas as pd
import json
import os
import random
import pandas as pd
from datetime import datetime



# Pfad zur Speicherdatei
STORAGE_FILE = "json_data.json"

# Globale Variablen
fiktive_zeit = None
wettervorhersage = {
    "temperatur_vormittags": None,
    "zustand_vormittags": None,
    "temperatur_nachmittags": None,
    "zustand_nachmittags": None,
    "temperatur_nachts": None,
    "zustand_nachts": None
}

# Funktion, um Daten aus der Datei zu laden
def load_weather_data():
    global fiktive_zeit, wettervorhersage
    if os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, "r", encoding="utf-8") as file:  # Encoding hinzugefügt
            try:
                
                data = json.load(file)
                if "fiktive_zeit" in data and data["fiktive_zeit"]:
                    fiktive_zeit = datetime.strptime(data["fiktive_zeit"], "%Y-%m-%d")
                if "wettervorhersage" in data:
                    wettervorhersage.update(data["wettervorhersage"])
            except (json.JSONDecodeError, ValueError, KeyError):
                print("Fehler beim Laden der Daten. Datei wird ignoriert.")

# Funktion, um Daten in der Datei zu speichern
def save_weather_data():
    global fiktive_zeit, wettervorhersage
    with open(STORAGE_FILE, "w", encoding="utf-8") as file:  # Encoding hinzugefügt
        data = {
            "fiktive_zeit": fiktive_zeit.strftime("%Y-%m-%d") if fiktive_zeit else None,
            "wettervorhersage": wettervorhersage
        }
        json.dump(data, file, ensure_ascii=False, indent=4)  # ensure_ascii=False für Umlaute


# Funktion, um das Datum (fiktiv oder echt) im deutschen Format zurückzugeben
def get_today_date():
    global fiktive_zeit
    if fiktive_zeit:
        return fiktive_zeit.strftime("%A, %d. %B %Y")  # Beispiel: "Mittwoch, 15. Januar 2025"
    return datetime.now().strftime("%A, %d. %B %Y")

# Funktion: Einen Tag weitergehen
def advance_day():
    global fiktive_zeit
    if fiktive_zeit:
        fiktive_zeit += timedelta(days=1)
        save_weather_data()
        print(f"Die fiktive Zeit wurde auf {fiktive_zeit.strftime('%Y-%m-%d')} gesetzt.")
    else:
        print("Keine fiktive Zeit gesetzt. Kann nicht vorwärts gehen.")

# Funktion: Zufallszahl zwischen 0 und x generieren
def generate_random_number(x):
    if x > 0:
        return random.randint(0, x)
    else:
        raise ValueError("Die Obergrenze muss größer als 0 sein.")

# Erstellen der Wetterzustand-Tabelle
def create_weather_dataframe():
    data = [
        ["Sonnig", 0, 35, 200],
        ["Bewölkt", -5, 25, 150],
        ["Regnerisch", 0, 20, 100],
        ["Stürmisch", 0, 15, 20],
        ["Schneefall", -10, 5, 10],
        ["Klar", -5, 25, 10],
        ["Nebel", -5, 10, 5],
        ["Glatteis", -15, 0, 3],
        ["Hagel", -5, 15, 0.4],
        ["Dürre", 20, 40, 0.3],
        ["Heiß", 30, 45, 2],
        ["Kühl", 5, 15, 10],
        ["Schneesturm", -20, -5, 2],
        ["Sandsturm", 25, 45, 1],
        ["Windstill", 5, 20, 7],
        ["Gewitter", 15, 35, 6],
        ["Leichter Regen", 10, 20, 100],
        ["Starker Regen", 5, 15, 50],
        ["Kalt", -10, 10, 20],
        ["Frost", -10, 5, 7],
        ["Hitze", 35, 45, 3],
        ["Tropisch", 25, 35, 4],
        ["Nieselregen", 10, 20, 9],
        ["Schneematsch", -5, 5, 6],
        ["Überflutungen", 5, 20, 3],
        ["Gewittersturm", 10, 25, 4],
        ["Orkan", -5, 15, 0.1],
        ["Schauer", 5, 20, 10],
        ["Wolkenlos", -10, 30, 10],
        ["Nebelbank", -10, 5, 4],
        ["Föhn", 10, 25, 3],
        ["Trocken", 10, 35, 30],
        ["Kalt", -5, 10, 80],
        ["Schwül", 20, 35, 70],
    ]

    columns = ["Zustand", "Min-Temperatur", "Max-Temperatur", "Wahrscheinlichkeit"]
    return pd.DataFrame(data, columns=columns)

def create_forecast_next_day():
    global wettervorhersage
    global fiktive_zeit
    df_weather = create_weather_dataframe()
    
    # Aktuelle Vorhersage
    current_forecast = wettervorhersage
    if not fiktive_zeit:
        fiktive_zeit = datetime.now()

    # Bestimme die Jahreszeit und die optimale Temperatur
    monat = fiktive_zeit.month
    if 5 <= monat <= 7:  # Sommer: Mai, Juni, Juli
        optimal_temp = 20
        day_offset = 12  # Tagsüber 12 Grad wärmer im Sommer
    elif 11 <= monat or monat <= 1:  # Winter: November, Dezember, Januar
        optimal_temp = 0
        day_offset = 8  # Tagsüber 8 Grad wärmer im Winter
    else:  # Übergangszeit: Frühling und Herbst
        optimal_temp = 15
        day_offset = 5  # Übergangszeit: Tagsüber moderater Unterschied

    # Funktion zur Zustandsauswahl
    def select_weather_state(temperature):
        possible_states = df_weather[
            (df_weather["Min-Temperatur"] <= temperature) & 
            (df_weather["Max-Temperatur"] >= temperature)
        ]
        if not possible_states.empty:
            return possible_states.sample(weights=possible_states["Wahrscheinlichkeit"])["Zustand"].iloc[0]
        return "Wettervorhersage fällt heute aus"  # Fallback, falls keine passende Auswahl gefunden wird

    # Temperaturänderung unter Berücksichtigung der optimalen Temperatur berechnen
    def calculate_new_temperature(current_temp, optimal_temp, period):
        temp_delta = random.uniform(-3, 3)  # Zufällige Grundänderung
        correction_factor = (optimal_temp - current_temp) * 0.1  # Annäherung an die optimale Temperatur
        
        # Tagesabschnitt berücksichtigen
        if period in ["nachmittags"]:
           correction_factor = (optimal_temp + day_offset - current_temp) * 0.2
        else:
            correction_factor = (optimal_temp - current_temp) * 0.2
        return current_temp + temp_delta + correction_factor

    # Neue Temperaturen berechnen und Zustände auswählen
    forecast_next_day = {}
    for period in ["vormittags", "nachmittags", "nachts"]:
        current_temp = current_forecast[f"temperatur_{period}"]
        new_temp = round(calculate_new_temperature(current_temp, optimal_temp, period), 1)
        new_state = select_weather_state(new_temp)
        forecast_next_day[f"temperatur_{period}"] = new_temp
        forecast_next_day[f"zustand_{period}"] = new_state

    # Vorhersage aktualisieren
    wettervorhersage.update(forecast_next_day)
    save_weather_data()

    return forecast_next_day

