### finanzen.py ###
import json
import os
import pandas as pd
import random
import numpy as np

# Finanzdaten
companies_df = pd.read_csv("discord_bot/boerse.csv")
events = pd.read_csv("discord_bot/events.csv")
persons = {}

# Funktion zum Laden der Personendaten
def load_persons_data():
    if os.path.exists("personen_daten.csv"):
        df = pd.read_csv("personen_daten.csv")
        for _, row in df.iterrows():
            name = row["Name"]
            capital = row["capital"]
            portfolio = json.loads(row["Depot"])
            persons[name] = {"capital": capital, "portfolio": portfolio}

# Funktion zum Speichern der Personendaten
def save_persons_data():
    data = [{"Name": name, "capital": data["capital"], "Depot": json.dumps(data["portfolio"])} for name, data in persons.items()]
    df = pd.DataFrame(data)
    df.to_csv("personen_daten.csv", index=False)

# Aktienkurs abrufen
def get_stock_price(company_name):
    row = companies_df[companies_df["Unternehmen"] == company_name]
    return row.iloc[0]["Aktienwert"] if not row.empty else None

def buy_stock(person_name, company_name, quantity):
    if person_name not in persons:
        return "Person existiert nicht."

    stock_price = get_stock_price(company_name)
    if stock_price is None:
        return "Unternehmen nicht gefunden."

    total_price = stock_price * quantity
    if persons[person_name]["capital"] < total_price:
        return "Nicht genügend Kapital."

    # Kauf durchführen
    persons[person_name]["capital"] -= total_price
    if company_name in persons[person_name]["portfolio"]:
        persons[person_name]["portfolio"][company_name] += quantity
    else:
        persons[person_name]["portfolio"][company_name] = quantity

    save_persons_data()
    return f"{quantity} Aktien von {company_name} für {total_price} gekauft."

def sell_stock(person_name, company_name, quantity):
    if person_name not in persons:
        return "Person existiert nicht."

    if company_name not in persons[person_name]["portfolio"] or persons[person_name]["portfolio"][company_name] < quantity:
        return "Nicht genügend Aktien im Depot."

    stock_price = get_stock_price(company_name)
    if stock_price is None:
        return "Unternehmen nicht gefunden."

    total_price = stock_price * quantity

    # Verkauf durchführen
    persons[person_name]["portfolio"][company_name] -= quantity
    if persons[person_name]["portfolio"][company_name] == 0:
        del persons[person_name]["portfolio"][company_name]  # Falls alle verkauft wurden, entfernen

    persons[person_name]["capital"] += total_price
    save_persons_data()
    return f"{quantity} Aktien von {company_name} für {total_price} verkauft."

def calculate_portfolio_value(person_name):
    if person_name not in persons:
        return "Person existiert nicht."

    total_value = 0
    for company_name, quantity in persons[person_name]["portfolio"].items():
        stock_price = get_stock_price(company_name)
        if stock_price:
            total_value += stock_price * quantity
            
    capital = persons[person_name]["capital"]
    return total_value, capital

def distribute_dividends():
    total_payouts = {}

    # Gehe durch jede Person
    for person_name, data in persons.items():
        payout = 0
        # Gehe durch das Portfolio der Person (Unternehmen und ihre Anzahl an Aktien)
        for company_name, quantity in data["portfolio"].items():
            # Überprüfe, ob das Unternehmen Dividende zahlt
            company_data = companies_df[companies_df["Unternehmen"].str.lower() == company_name.lower()]
            if not company_data.empty:
                # Überprüfe, ob der Aktientyp "dividende" ist
                if company_data["Aktientyp"].values[0] == "dividende":
                    # Berechne den Dividendenbetrag (10 % des Aktienwerts * Anzahl der Aktien)
                    dividend = company_data["Aktienwert"].values[0] * 0.10 * quantity
                    payout += dividend
        
        # Update des Kapitals der Person
        persons[person_name]["capital"] += payout
        total_payouts[person_name] = payout

    save_persons_data()
    return total_payouts


def simulate_stock_prices():
    """
    Simuliert Aktienkurse basierend auf zufälligen Marktereignissen und Unternehmensspezifika.
    """
    market_trend = np.random.choice(["boom", "neutral", "crash"], p=[0.2, 0.6, 0.2])
    
    for index, row in companies_df.iterrows():
        change_factor = np.random.uniform(-0.05, 0.05)  # Standardmäßige Schwankung ±5%
        
        if market_trend == "boom":
            change_factor += np.random.uniform(0.02, 0.1)  # Positiver Boost
        elif market_trend == "crash":
            change_factor -= np.random.uniform(0.02, 0.1)  # Negativer Einbruch
        
        new_price = row['Aktienwert'] * (1 + change_factor)
        companies_df.at[index, 'Aktienwert'] = round(max(new_price, 0.1), 2)  # Mindestens 0.1
    
    companies_df.to_csv("discord_bot/boerse.csv", index=False)
    print("Markt Simulation.")
    return companies_df


def apply_market_events():
    """
    Wendet ein zufälliges Marktereignis auf die Aktienkurse an.
    """
    
    # Zufälliges Marktereignis auswählen
    event = events.sample(n=1).iloc[0]
    
    branche = event["branche"]
    impact = event["impact"]  # "positive" oder "negative"
    change = event["change"] / 100  # Umrechnung in Prozent
    description = event["description"]
    impact = event["impact"]
    
    companies_df.loc[companies_df['Branche'] == branche, 'Aktienwert'] = (
    companies_df.loc[companies_df['Branche'] == branche, 'Aktienwert'] * (1 + change)).apply(lambda x: round(max(x, 0.1), 2))

    
    companies_df.to_csv("discord_bot/boerse.csv", index=False)
    print("Marktevent angewendet.")
    return impact, description

def change_specific_company_value(company_name, value):
    """
    Ändert den Aktienwert eines spezifischen Unternehmens um einen bestimmten Wert.
    """
    if company_name not in companies_df["Unternehmen"].values:
        return "Unternehmen nicht gefunden."
    
    companies_df.loc[companies_df["Unternehmen"] == company_name, "Aktienwert"] = (
        companies_df.loc[companies_df["Unternehmen"] == company_name, "Aktienwert"] + value
    ).apply(lambda x: round(max(x, 0.1), 2))  # Mindestwert 0.1
    
    companies_df.to_csv("discord_bot/boerse.csv", index=False)
    return f"Aktienwert von {company_name} um {value} angepasst."


def get_all_information_about_a_company(company_name):
    """
    Ruft alle verfügbaren Informationen über ein Unternehmen ab.
    """
    row = companies_df[companies_df["Unternehmen"] == company_name]
    if row.empty:
        return "Unternehmen nicht gefunden."
    
    return row.to_dict(orient="records")[0]  # Gibt die Zeile als Wörterbuch zurück
def get_portfolio_information(person_name):
    """
    Ruft die Depotinformationen einer Person ab und ergänzt die Unternehmensinfos.
    """
    if person_name not in persons:
        return "Person existiert nicht."
    
    portfolio = persons[person_name]["portfolio"]
    capital = round(persons[person_name]["capital"], 2)
    
    portfolio_details = []
    total_value = 0
    for company, quantity in portfolio.items():
        stock_price = get_stock_price(company)
        company_info = get_all_information_about_a_company(company)
        if stock_price:
            value = round(stock_price * quantity, 2)
            total_value += value
            portfolio_details.append(f"\n**{company}**\n"
                                     f"  - Anzahl: {quantity}\n"
                                     f"  - Wert pro Aktie: {round(stock_price, 2)}\n"
                                     f"  - Gesamtwert: {value}\n"
                                     f"  - Branche: {company_info.get('Branche', 'N/A')}\n"
                                     f"  - Aktientyp: {company_info.get('Aktientyp', 'N/A')}\n"
                                     f"  - Kursbewegung: {company_info.get('Kursbewegung', 'N/A')}")

    total_value = round(total_value, 2)
    
    return (f"**Kapital:** {capital}\n"
            f"**Depotwert:** {total_value}\n"
            f"**Details:** {''.join(portfolio_details)}")

def get_more_money(person, amount):
    """
    Fügt einer Person mehr Kapital hinzu.
    """
    if person not in persons:
        return "Person existiert nicht."
    
    # Kapital erhöhen
    persons[person]["capital"] += amount
    save_persons_data()
    
    return f"{amount} wurde zu {person}'s Kapital hinzugefügt."
