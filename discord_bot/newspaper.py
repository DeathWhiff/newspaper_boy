import pandas as pd
import numpy as np
from datetime import timedelta

class NewspaperEvents:
    def __init__(self, file_path: str):
        """Initialisiert die Klasse mit den Zeitungsereignissen."""
        self.file_path = file_path
        self.df = self.read_data()
    
    def read_data(self) -> pd.DataFrame:
        """Liest die Zeitungsereignisse aus einer CSV-Datei."""
        try:
            df = pd.read_csv(self.file_path)
            return df
        except FileNotFoundError:
            print(f"Datei {self.file_path} nicht gefunden.")
            return pd.DataFrame()
    

    
    def add_event(self, newspaper_event_id, short_description, newspaper_text, activation_boolean, follow_newspaper_id, follow_newspaper_time_break, probability, typ, spezial_date):
        """Fügt eine neue Ereigniszeile in den DataFrame ein."""
        new_row = {
            "newspaper_event_id": newspaper_event_id,
            "short_description": short_description,
            "newspaper_text": newspaper_text,
            "activation_boolean": activation_boolean,
            "follow_newspaper_id": follow_newspaper_id,
            "follow_newspaper_time_break": follow_newspaper_time_break,
            "probability": probability,
            "typ": typ,
            "spezial_date": spezial_date
        }
        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)
        self.save_data()
    
    def get_events_by_day(self, date: str) -> pd.DataFrame:
        """Gibt alle Ereignisse eines bestimmten Tages zurück."""
        self.df['spezial_date'] = self.df['spezial_date'].astype(str)
        return self.df[self.df['spezial_date'] == date]

    
    def bot_get_events_by_day(self, date: str) -> str:
        """Gibt alle Ereignisse eines bestimmten Tages als schön formatierte Zeitung aus."""
        events = self.get_events_by_day(date)
        if events.empty:
            return f"Keine Ereignisse für den {date} gefunden."
        
        formatted_events = []
        for _, row in events.iterrows():
            formatted_events.append(
                f"### {row['typ']} ###\n"
                f"**{row['short_description']}**\n"
                f"{row['newspaper_text']}\n"
                f"------------------------------"
            )
        
        return f"Ereignisse am {date}:\n" + "\n".join(formatted_events)
    
    def bot_add_event(self, newspaper_event_id, short_description, newspaper_text, activation_boolean, follow_newspaper_id, follow_newspaper_time_break, probability, typ, spezial_date) -> str:
        """Fügt ein Ereignis hinzu und gibt eine Bestätigung zurück."""
        self.add_event(newspaper_event_id, short_description, newspaper_text, activation_boolean, follow_newspaper_id, follow_newspaper_time_break, probability, typ, spezial_date)
        return f"Ereignis '{short_description}' wurde hinzugefügt."
    
    def save_data(self):
        """Speichert den DataFrame in die CSV-Datei zurück."""
        self.df.to_csv(self.file_path, index=False)

