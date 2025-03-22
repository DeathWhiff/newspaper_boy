### sonstiges.py ###
import random
from datetime import datetime, timedelta
import locale

# Lokalisierung setzen
locale.setlocale(locale.LC_TIME, "de_DE.UTF-8")

import discord_bot.wetter as wetter

def get_today_date():
    fiktive_zeit = wetter.fiktive_zeit
    if fiktive_zeit:
        return fiktive_zeit.strftime("%A, %d. %B %Y")  # Beispiel: "Mittwoch, 15. Januar 2025"
    return datetime.now().strftime("%A, %d. %B %Y")

# Funktion: Einen Tag weitergehen
def advance_day():
    fiktive_zeit = wetter.fiktive_zeit
    if fiktive_zeit:
        fiktive_zeit += timedelta(days=1)
        wetter.save_weather_data()
        print(f"Die fiktive Zeit wurde auf {fiktive_zeit.strftime('%Y-%m-%d')} gesetzt.")
    else:
        print("Keine fiktive Zeit gesetzt. Kann nicht vorwärts gehen.")



# Zufallszahl generieren
def generate_random_number(x):
    return random.randint(0, x) if x > 0 else ValueError("Die Obergrenze muss größer als 0 sein.")
