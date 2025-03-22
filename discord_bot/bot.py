import os
import discord
from dotenv import load_dotenv
import random
from datetime import datetime, timedelta
import locale
import sys
sys.path.append('C:\\Users\\simon\\Downloads\\DISCORDBOT')

import discord_bot.aktien as aktien
import discord_bot.sonstige as sonstige
import discord_bot.wetter as wetter
import discord_bot.newspaper as newspaper


# Discord-Token (unverändert)
TOKEN = ''

# Intents initialisieren (auch für Nachrichten-Events)
intents = discord.Intents.default()
intents.messages = True  # Zugriff auf Nachrichten
intents.message_content = True

# Discord-Client mit den festgelegten Intents erstellen
client = discord.Client(intents=intents)

# Lokalisierung für Deutsch setzen
locale.setlocale(locale.LC_TIME, "de_DE.UTF-8")

# Pfad zur Speicherdatei
STORAGE_FILE = "json_data.json"

# Event: Bot ist online
@client.event
async def on_ready():
    print(f'{client.user} hat sich erfolgreich mit Discord verbunden!')

# Event: Wenn der Bot eine Nachricht empfängt
@client.event
async def on_message(message):
    
    global fiktive_zeit
    # Aktuelle Zeit abrufen
    now = datetime.now()

    # Fiktives Jahr aus dem vorhandenen datetime-Objekt extrahieren
    fiktives_jahr = wetter.fiktive_zeit.year
    
    fiktiver_day = wetter.fiktive_zeit.day
    now_day = now.day
    
    if now_day != fiktiver_day:
        wetter.create_forecast_next_day

    # Neue fiktive Zeit mit aktuellem Tag und Monat, aber fiktivem Jahr
    fiktive_zeit = datetime(year=fiktives_jahr, month=now.month, day=now.day)

    # Wetter-Objekt aktualisieren
    wetter.fiktive_zeit = fiktive_zeit

    # Verhindern, dass der Bot auf sich selbst antwortet
    if message.author == client.user:
        return

    # Begrüßung
    if message.content.lower() == "!zeitungsjunge":
        await message.channel.send("Ich bin der Zeitungsjunge!")

    # Aktuelles Datum abfragen
    elif message.content.lower() == "!zeitungsjunge welcher tag ist heute?":
        today_date = wetter.get_today_date()
        await message.channel.send(f"Heute ist {today_date}.")
        
    elif message.content.lower() == "!zeitungsjunge wie wird das wetter?":
        if wetter.wettervorhersage["temperatur_vormittags"] is not None and wetter.wettervorhersage["zustand_vormittags"] is not None:
            wetter_text = (
                f"Wetterbericht für heute:\n"
                f"Vormittags: {wetter.wettervorhersage['temperatur_vormittags']}°C, {wetter.wettervorhersage['zustand_vormittags']}\n"
                f"Nachmittags: {wetter.wettervorhersage['temperatur_nachmittags']}°C, {wetter.wettervorhersage['zustand_nachmittags']}\n"
                f"Nachts: {wetter.wettervorhersage['temperatur_nachts']}°C, {wetter.wettervorhersage['zustand_nachts']}"
            )
            await message.channel.send(wetter_text)
        else:
            await message.channel.send("Die Wettervorhersage ist aktuell nicht verfügbar. Versuche, die Zeit zu setzen oder eine neue Vorhersage zu generieren.")

    # Fiktive Zeit setzen
    elif message.content.lower().startswith("!zeitungsjunge setzte zeit auf: "):
        try:
            # Zeit aus der Nachricht extrahieren
            zeit_string = message.content[len("!zeitungsjunge setzte zeit auf: ") :].strip()
            fiktive_zeit = datetime.strptime(zeit_string, "%d %m %Y")
            wetter.fiktive_zeit = fiktive_zeit # Fiktive Zeit speichern
            await message.channel.send(f"Die fiktive Zeit wurde auf {sonstige.get_today_date()} gesetzt.")
        except ValueError:
            await message.channel.send("Bitte gebe das Datum im Format 'Tag Monat Jahr' an, z. B. '15 01 2025'.")

    # Wettervorhersage ausgeben
    elif message.content.lower() == "!zeitungsjunge wettervorhersage":
        
        if wetter.wettervorhersage["temperatur_vormittags"] is not None and wetter.wettervorhersage["zustand_vormittags"] is not None:
            wetter_text = (
                f"Wettervorhersage:\n"
                f"Vormittags: {wetter.wettervorhersage['temperatur_vormittags']}°C, {wetter.wettervorhersage['zustand_vormittags']}\n"
                f"Nachmittags: {wetter.wettervorhersage['temperatur_nachmittags']}°C, {wetter.wettervorhersage['zustand_nachmittags']}\n"
                f"Nachts: {wetter.wettervorhersage['temperatur_nachts']}°C, {wetter.wettervorhersage['zustand_nachts']}"
            )
            await message.channel.send(wetter_text)
        else:
            await message.channel.send("Die Wettervorhersage ist aktuell nicht verfügbar.")
            
    elif message.content.lower().startswith("!zeitungsjunge wie steht die aktie"):
        company_name = message.content[len("!zeitungsjunge wie steht die aktie "):].strip()
        stock_price = aktien.get_stock_price(company_name)
        if stock_price is not None:
            await message.channel.send(f"Der aktuelle Kurs der Aktie {company_name} beträgt {stock_price} .")
        else:
            await message.channel.send(f"Die Aktie {company_name} konnte nicht gefunden werden.")

    elif message.content.lower() == "!zeitungsjunge zeig mein depot":
        aktien.load_persons_data()
        person_name = message.author.name
        if person_name not in aktien.persons:
            await message.channel.send(f"Du hast noch kein Depot. Bitte registriere dich mit !zeitungsjunge starte dein depot.")
            return
        capital_var = aktien.persons[person_name]["capital"]
        await message.channel.send(f"Du hast:\n{capital_var}")
        portfolio = aktien.persons[person_name]["portfolio"]
        if not portfolio:
            await message.channel.send(f"Dein Depot ist leer.")
        else:
            depot_str = "\n".join([f"{company}: {quantity} Aktien" for company, quantity in portfolio.items()])
            await message.channel.send(f"Dein Depot:\n{depot_str}")

    elif message.content.lower().startswith("!zeitungsjunge kaufe"):
        try:
            parts = message.content.split(" ")
            company_name = parts[2]
            quantity = int(parts[3])
            person_name = message.author.name
            aktien.load_persons_data()
            if person_name not in aktien.persons:
                await message.channel.send(f"Du hast noch kein Depot. Bitte registriere dich mit !zeitungsjunge starte dein depot.")
                return
            response = aktien.buy_stock(person_name, company_name, quantity)
            await message.channel.send(response)
        except (IndexError, ValueError):
            await message.channel.send("Verwendung: !zeitungsjunge kaufe <Aktie> <Menge>")

    elif message.content.lower().startswith("!zeitungsjunge verkaufe"):
        try:
            parts = message.content.split(" ")
            company_name = parts[2]
            quantity = int(parts[3])
            person_name = message.author.name
            aktien.load_persons_data()
            response = aktien.sell_stock(person_name, company_name, quantity)
            await message.channel.send(response)
        except (IndexError, ValueError):
            await message.channel.send("Verwendung: !zeitungsjunge verkaufe <Aktie> <Menge>")

    elif message.content.lower() == "!zeitungsjunge portfolio wert":
        person_name = message.author.name
        aktien.load_persons_data()
        if person_name not in aktien.persons:
            await message.channel.send(f"Du hast noch kein Depot. Bitte registriere dich mit !zeitungsjunge starte dein depot.")
            return
        total_value, value = aktien.calculate_portfolio_value(person_name)
        await message.channel.send(f"Der Gesamtwert deines Depots beträgt {total_value} und zusätzlich hast du {value} Guthaben.")

    elif message.content.lower() == "!zeitungsjunge starte dein depot":
        person_name = message.author.name
        aktien.load_persons_data()
        if person_name in aktien.persons:
            await message.channel.send(f"Du hast bereits ein Depot.")
        else:
            aktien.persons[person_name] = {"capital": 1000, "portfolio": {}}
            aktien.save_persons_data()
            await message.channel.send(f"Dein Depot wurde erstellt und du hast 1000 Kapital.")

    elif message.content.lower() == "!zeitungsjunge dividenden auszahlen":
        aktien.load_persons_data()
        aktien.distribute_dividends()
        await message.channel.send("Dividenden wurden an alle Depots ausgezahlt.")
        
    elif message.content.lower() == "!zeitungsjunge nimm diesen groschen":
        person_name = message.author.name
        if person_name in aktien.persons:
            aktien.load_persons_data()
            aktien.get_more_money(person_name, -5)
            await message.channel.send("Vielen Dank!")
        else:
            await message.channel.send(f"Du hast kein Geld dabei. Na ganz toll!!")

    elif message.content.lower() == "!zeitungsjunge aktien simulieren":
        aktien.simulate_stock_prices()
        await message.channel.send("Die Aktienkurse wurden simuliert.")

    elif message.content.lower() == "!zeitungsjunge marktereignisse anwenden":
        impact, description = aktien.apply_market_events()
        await message.channel.send(f"Marktereignisse wurden angewendet. {description}. Die englische Börse indiziert: The impact is {impact} on the whole industry!")
        
    elif message.content.lower().startswith("!zeitungsjunge aktienwert ändern"):
        try:
            parts = message.content.split(" ")
            company_name = parts[3]
            value = float(parts[4])
            response = aktien.change_specific_company_value(company_name, value)
            await message.channel.send(response)
        except (IndexError, ValueError):
            await message.channel.send("Verwendung: !zeitungsjunge aktienwert ändern <Unternehmen> <Wert>")
    
    elif message.content.lower().startswith("!zeitungsjunge unternehmen info"):
        try:
            parts = message.content.split(" ")
            company_name = parts[3]
            response = aktien.get_all_information_about_a_company(company_name)
            await message.channel.send(str(response))
        except IndexError:
            await message.channel.send("Verwendung: !zeitungsjunge unternehmen info <Unternehmen>")
    
    elif message.content.lower().startswith("!zeitungsjunge portfolio info"):
        person_name = message.author.name
        response = aktien.get_portfolio_information(person_name)
        await message.channel.send(str(response))
        
    elif message.content.lower().startswith("!zeitungsjunge guthaben erhöhen"):
        try:
            parts = message.content.split(" ")
            person_name = parts[3]
            value = float(parts[4])
            response = aktien.get_more_money(person_name, value)
            await message.channel.send(response)
        except (IndexError, ValueError):
            await message.channel.send("Verwendung: !zeitungsjunge aktienwert ändern <Unternehmen> <Wert>")
            
    if message.content.lower().startswith("!zeitungsjunge tagesblatt"):
        try:
            parts = message.content.split(" ")
            date = parts[2]
            MAX_DISCORD_LENGTH = 2000

            response = events.bot_get_events_by_day(date)
            response_text = str(response)

            # In 2000 Zeichen lange Teile aufsplitten
            for i in range(0, len(response_text), MAX_DISCORD_LENGTH):
                await message.channel.send(response_text[i : i + MAX_DISCORD_LENGTH])
        except IndexError:
            await message.channel.send("Verwendung: !zeitungsjunge tagesblatt <Datum>")
    
    elif message.content.lower().startswith("!zeitungsjunge neues ereignis"):
        try:
            parts = message.content.split(" ")
            newspaper_event_id = parts[3]
            short_description = parts[4]
            newspaper_text = parts[5]
            activation_boolean = parts[6].lower() == "true"
            follow_newspaper_id = None if parts[7].lower() == "none" else parts[7]
            follow_newspaper_time_break = None if parts[8].lower() == "none" else int(parts[8])
            probability = float(parts[9])
            typ = parts[10]
            spezial_date = parts[11]
            response = events.bot_add_event(newspaper_event_id, short_description, newspaper_text, activation_boolean, follow_newspaper_id, follow_newspaper_time_break, probability, typ, spezial_date)
            await message.channel.send(response)
        except (IndexError, ValueError):
            await message.channel.send("Verwendung: !zeitungsjunge neues ereignis <ID> <Kurzbeschreibung> <Text> <Aktivierung (True/False)> <Follow-Up-ID oder None> <Follow-Up-Zeit oder None> <Wahrscheinlichkeit> <Typ> <Datum>")
            
    elif message.content.lower() == "!zeitungsjunge help":
        help_text = (
            "Hier sind alle verfügbaren Befehle:\n"
            "!zeitungsjunge - Begrüßung\n"
            "!zeitungsjunge welcher tag ist heute? - Zeigt das aktuelle Datum\n"
            "!zeitungsjunge wie wird das wetter? - Zeigt die Wettervorhersage\n"
            "!zeitungsjunge setzte zeit auf: <Tag Monat Jahr> - Setzt die fiktive Zeit\n"
            "!zeitungsjunge wettervorhersage - Zeigt die Wettervorhersage\n"
            "!zeitungsjunge wie steht die aktie <Unternehmen> - Zeigt den aktuellen Aktienkurs\n"
            "!zeitungsjunge zeig mein depot - Zeigt das Depot des Nutzers\n"
            "!zeitungsjunge kaufe <Aktie> <Menge> - Kauft Aktien für den Nutzer\n"
            "!zeitungsjunge verkaufe <Aktie> <Menge> - Verkauft Aktien aus dem Depot\n"
            "!zeitungsjunge portfolio wert - Zeigt den Wert des Depots\n"
            "!zeitungsjunge starte dein depot - Startet ein neues Depot\n"
            "!zeitungsjunge dividenden auszahlen - Zahlt Dividenden an alle Depots aus\n"
            "!zeitungsjunge nimm diesen groschen - Gibt dem Nutzer einen Groschen\n"
            "!zeitungsjunge aktien simulieren - Simuliert die Aktienkurse\n"
            "!zeitungsjunge marktereignisse anwenden - Wendet Marktereignisse an\n"
            "!zeitungsjunge aktienwert ändern <Unternehmen> <Wert> - Ändert den Wert einer Aktie\n"
            "!zeitungsjunge unternehmen info <Unternehmen> - Zeigt Informationen über ein Unternehmen\n"
            "!zeitungsjunge portfolio info - Zeigt Informationen über das Depot des Nutzers\n"
            "!zeitungsjunge guthaben erhöhen <Person> <Betrag> - Erhöht das Guthaben eines Nutzers\n"
            "!zeitungsjunge tagesblatt <Datum> - Zeigt eine Zeitung für ein bestimmtes Datum\n"
            "!zeitungsjunge neues ereignis <ID> <Kurzbeschreibung> <Text> <Aktivierung> <Follow-Up-ID> <Follow-Up-Zeit> <Wahrscheinlichkeit> <Typ> <Datum> - Fügt ein neues Ereignis hinzu\n"
            "!zeitungsjunge zeitung"
        )
        await message.channel.send(help_text)
        
        
    # Neue Methode für Tagesauskunft
    elif message.content.lower() == "!zeitungsjunge zeitung":
        today_date = wetter.fiktive_zeit  # Holen des aktuellen Datums
        today_date = today_date.strftime("%d.%m")
        events_response = events.bot_get_events_by_day(today_date) 

        # Wetterbericht erstellen
        if wetter.wettervorhersage["temperatur_vormittags"] is not None and wetter.wettervorhersage["zustand_vormittags"] is not None:
            wetter_text = (
                f"Wetterbericht für heute:\n"
                f"Vormittags: {wetter.wettervorhersage['temperatur_vormittags']}°C, {wetter.wettervorhersage['zustand_vormittags']}\n"
                f"Nachmittags: {wetter.wettervorhersage['temperatur_nachmittags']}°C, {wetter.wettervorhersage['zustand_nachmittags']}\n"
                f"Nachts: {wetter.wettervorhersage['temperatur_nachts']}°C, {wetter.wettervorhersage['zustand_nachts']}"
            )
        else:
            wetter_text = "Die Wettervorhersage ist aktuell nicht verfügbar."

        # Depot des Nutzers abfragen
        aktien.load_persons_data()
        person_name = message.author.name
        if person_name not in aktien.persons:
            depot_text = "Du hast noch kein Depot. Bitte registriere dich mit !zeitungsjunge starte dein depot."
        else:
            capital_var = aktien.persons[person_name]["capital"]
            portfolio = aktien.persons[person_name]["portfolio"]
            depot_text = f"Dein Kapital: {capital_var}\n"
            if not portfolio:
                depot_text += "Dein Depot ist leer."
            else:
                depot_text += "\n".join([f"{company}: {quantity} Aktien" for company, quantity in portfolio.items()])

        # Tageszeitung+
        events_text = str(events_response)

        # Antwort senden
        response_text = (
            f"Tagesauskunft für {today_date}:\n\n"
            f"Wetterbericht:\n{wetter_text}\n\n"
            f"Depotübersicht:\n{depot_text}\n\n"
            f"Tageszeitung:\n{events_text}"
        )
        MAX_DISCORD_LENGTH = 2000
        for i in range(0, len(response_text), MAX_DISCORD_LENGTH):
            await message.channel.send("```YAML\nThe London Chronicle\n```\n" + response_text[i:i + MAX_DISCORD_LENGTH])
    


# Bot starten
if __name__ == '__main__':
    print("Bot wird gestartet...")
    aktien.load_persons_data()  # Personen-Daten beim Start laden
    wetter.load_weather_data()  # Daten beim Start laden
    events = newspaper.NewspaperEvents("discord_bot/newspaper.csv")
    client.run(TOKEN)

