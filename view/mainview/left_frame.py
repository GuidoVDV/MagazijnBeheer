#IMPORTS
import tkinter as tk
from tkinter import ttk
from controller.excel_controller import read_klassen
from controller.excel_controller import get_leerlingen


#FUNCTIES START FRAME
def create_left_frame(parent, on_leerling_selected, right_frame):
    left_frame = tk.Frame(parent, width=200, bg="grey")

    title = tk.Label(left_frame, text="Kies een klas:", bg="grey")
    title.pack(padx=10, pady=10)

    lijst_klassen = read_klassen()
    geselecteerde_klas = tk.StringVar() #deze variabele zal de gekozen waarde bijhouden.

    klassen_combobox = ttk.Combobox(left_frame, textvariable=geselecteerde_klas, values=lijst_klassen, state="readonly")
    klassen_combobox.pack(padx=10, pady=10, fill="x")

    #als er waarden in de lijst zijn, dan toon je direct de eerste waarde
    if lijst_klassen:
        klassen_combobox.current(0)
    
    # Container voor leerlingen 
    leerlingen_listbox = tk.Listbox(left_frame, selectmode=tk.SINGLE, bg="lightgrey", activestyle="none")
    leerlingen_listbox.pack(fill="both", expand=True, padx=5, pady=5)


    #geneste functie om leerlingen te updaten
    def update_leerlingen(lijst_leerlingen):
        leerlingen_listbox.delete(0, tk.END)
        for leerling in lijst_leerlingen:
            leerlingen_listbox.insert(tk.END, leerling)


    #geneste functie als callback functie zodat we een even kunnen binden aan de combobox
    def on_klassen_gekozen(event):
        
        right_frame.reset_leerling()

        print("Geselecteerde klasse:", geselecteerde_klas.get())

        klas = geselecteerde_klas.get()
        lijst_leerlingen = get_leerlingen(klas)
        update_leerlingen(lijst_leerlingen)
    
    def on_leerling_gekozen(event):
        selectie = leerlingen_listbox.curselection()
        if not selectie:
            return
        leerling = leerlingen_listbox.get(selectie[0])
        on_leerling_selected(leerling)

    #event binden aan combobox => on_klassen_gekozen functie wordt uitgevoer als de gebruiker een andere
    #optie kiest.
    klassen_combobox.bind("<<ComboboxSelected>>", on_klassen_gekozen)
    leerlingen_listbox.bind("<<ListboxSelect>>", on_leerling_gekozen)


    #initialiseer leerlingenlijst voor de eerste klas
    if lijst_klassen:
        update_leerlingen(get_leerlingen(geselecteerde_klas.get()))

    left_frame.pack_propagate(False)    #voorkomt krimpen van een frame
    return left_frame


