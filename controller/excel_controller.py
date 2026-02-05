from model.excel_reader import read_excel_sheet

#Deze functie leest de klassen uit van het tabblad met de naam "Klassen"
#De assumptie is dat deze klassen op rij 1 in dat tabblad staan.
def read_klassen():
    df = read_excel_sheet(sheet_name="Klassen")

    if df is None or df.empty:
        return []
    
    return list(df.columns)

#Met deze functie halen we de leerlingen op van de opgegeven klas
def get_leerlingen(klas_naam):
    df = read_excel_sheet(sheet_name="Klassen")

    if df is None or df.empty or klas_naam not in df.columns:
        return[]
    
    lijst_leerlingen = df[klas_naam].dropna().tolist()
    return lijst_leerlingen     

def get_kasten():
    df = read_excel_sheet(sheet_name="Kasten")

    if df is None or df.empty:
        return []
    
    lijst_kasten_id = df["kast_id"].dropna().tolist()
    lijst_kasten = df["naam"].dropna().tolist()
    lijst_bestandnamen = df["bestandsnaam"].dropna().tolist()

    return lijst_kasten_id, lijst_kasten, lijst_bestandnamen
 
def get_categorie(event):
    df = read_excel_sheet(sheet_name=event)
    if df is None or df.empty:
        return []
    
    materiaal_categorie = df["Categorie"].dropna().unique().tolist()

    return materiaal_categorie

    

