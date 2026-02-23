import pandas as pd

def write_list_to_excel(data, file_path, sheet_name="Sheet1"):
    """
    Schrijft een lijst of een lijst‑van‑lijsten naar een Excel‑spreadsheet.

    Parameters
    ----------
    data : list of list | list
        • Als `data` een lijst van lijsten is, wordt elke sub‑lijst als één rij
          in de spreadsheet geplaatst.
        • Als `data` een eenvoudige lijst is, wordt deze als één kolom weggeschreven.
    file_path : str
        Volledig pad (incl. .xlsx extensie) waar het bestand moet worden opgeslagen.
    sheet_name : str, optional
        Naam van het werkblad in het Excel‑bestand (standaard “Sheet1”).

    Returns
    -------
    None
        De functie schrijft het bestand naar schijf en geeft niets terug.
    """

    # Normaliseer de invoer zodat pandas er een DataFrame van kan maken
    if isinstance(data, list) and all(isinstance(row, list) for row in data):
        # Lijst van lijsten → elke sub‑lijst = één rij
        df = pd.DataFrame(data)
    else:
        # Enkele lijst → één kolom
        df = pd.DataFrame(data, columns=["Value"])

    # Schrijf naar Excel (engine=openpyxl wordt automatisch gekozen)
    df.to_excel(file_path, sheet_name=sheet_name, index=False)

# ----------------------------------------------------------------------
# Voorbeeldgebruik
if __name__ == "__main__":
    # Voorbeeld 1: eenvoudige lijst
    simple_list = ["Apple", "Banana", "Cherry"]
    write_list_to_excel(simple_list, "fruit_simple.xlsx")

    # Voorbeeld 2: lijst van lijsten (tabelvorm)
    table_data = [
        ["Naam", "Leeftijd", "Stad"],
        ["Alice", 30, "Amsterdam"],
        ["Bob",   25, "Rotterdam"],
        ["Cathy", 28, "Utrecht"]
    ]
    write_list_to_excel(table_data, "personen.xlsx")