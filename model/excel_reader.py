import pandas as pd
import os

#ervoor zorgen dat het pad van het scrpit opgehaald wordt
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
#afdwingen dat dit script en het bronbestand in dezelfde folder moeten staan
EXCEL_BESTAND = os.path.join(SCRIPT_DIR, "Magazijn.xlsx")

#Lees een volledige sheet uit het Excel-bestand en retourneer een pandas DataFrame
def read_excel_sheet(sheet_name=None):
    try:
        df = pd.read_excel(EXCEL_BESTAND, sheet_name=sheet_name).fillna("")
        return df
    except Exception as e:
        print(f"Fout bij het openen van Excel: {e}")
        return None
    
