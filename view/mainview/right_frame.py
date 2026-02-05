<<<<<<< HEAD
#IMPORTS
import tkinter as tk
import os
from controller.excel_controller import get_kasten
from controller.excel_controller import get_categorie

from PIL import Image, ImageTk

#CONSTANTEN
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) #bepaal de locatie van je script!
IMG_LOCATION = ".."  # ga naar de parent folder
IMG_LOCATION_NAME = "images" #folder naam die je wil openen => in ons voorbeeld de folder images

#FUNCTIES KAST
#def kast_on_click():
def kast_on_click(kast_id, kast_naam):
    print("kast geklikt", kast_id, kast_naam)
    print("categorieen : ",get_categorie(kast_naam))

#FUNCTIES START FRAME
def create_right_frame(parent):
    right_frame = tk.Frame(parent)
    
    #title = tk.Label(right_frame, text="right frame")
    #title.pack(padx=10, pady=10)

    leerling = tk.Label(right_frame, text="Geen leerling geselecteerd")
    #leerling.pack(padx=10, pady=10) => als we knoppen met grid willen positioneren, dan moet deze pack ook vervangen worden door een grid
    #maar 1 pack manager per bestand!
    leerling.grid(row=0, column=0, padx=10, pady=10)

    #je krijgt drie lijsten terug van de get_kasten methode!
    lijst_kasten_ids, lijst_kasten, lijst_bestandsnamen = get_kasten()
    #zorg ervoor dat de referenties naar de afbeeldingen bekend blijven in je frame, ook als de ophalen gedaan is
    #dit doe je bijvoorbeeld door deze op het frame zelf in een lijst bij te houden.
    right_frame.lijst_kast_images = []
    row_teller = 3  #3e rij omdat we boven de knoppen de naam van de leerling tonen op het scherm
    col_teller = 0 
    kast_index = 0
    if lijst_kasten:        
        while kast_index < len(lijst_kasten):
            #pad naar de afbeelding instellen
            icoon_pad = os.path.join(SCRIPT_DIR, IMG_LOCATION, IMG_LOCATION_NAME, lijst_bestandsnamen[kast_index])
            #print(f"DEBUG: Pad='{icoon_pad}' Bestaat={os.path.exists(icoon_pad)}")
            if os.path.exists(icoon_pad):
                kast_img = Image.open(icoon_pad).resize((200, 200))
                kast_img_tk = ImageTk.PhotoImage(kast_img)
                right_frame.lijst_kast_images.append(kast_img_tk) #referentie behouden
            else:
                kast_img_tk = ImageTk.PhotoImage(Image.new("RGB", (200, 200), color="gray"))
                right_frame.lijst_kast_images.append(kast_img_tk)

            kast_knop = tk.Button(
                right_frame,
                image=kast_img_tk,
                text=lijst_bestandsnamen[kast_index], 
                compound="top", 
                width=250,
                height=220,
                #command=kast_on_click
                #lambda = een anonieme (naamloze) functie in één regel waardoor je in staat bent om bijv waarden mee te geven aan het uit
                #te voeren commando bij het drukken op een knop.
                command=lambda kast_id=lijst_kasten_ids[kast_index], kast_naam=lijst_kasten[kast_index]: kast_on_click(kast_id, kast_naam)
                )
            kast_knop.image = kast_img_tk  #om de referentie naar de afbeelding te verzekeren
            #max 3 knoppen per rij instellen, dus pack manager voor dit frame omvormen naar grid
            kast_knop.grid(row=row_teller, column=col_teller, padx=3, pady=3)
            if col_teller == 2:
                col_teller = 0
                row_teller = row_teller + 1
            else:
                col_teller = col_teller + 1

            kast_index = kast_index + 1


    def toon_leerling(naam):
        leerling.config(text=f"Geselecteerde leerling: {naam}")

    def reset_leerling():
        leerling.config(text="Geen leerling geselecteerd")

    #Toegankelijk maken via right_frame
    right_frame.reset_leerling = reset_leerling
    right_frame.toon_leerling = toon_leerling

=======
#IMPORTS
import tkinter as tk
import os
from controller.excel_controller import get_kasten
from controller.excel_controller import get_categorie

from PIL import Image, ImageTk

#CONSTANTEN
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) #bepaal de locatie van je script!
IMG_LOCATION = ".."  # ga naar de parent folder
IMG_LOCATION_NAME = "images" #folder naam die je wil openen => in ons voorbeeld de folder images

#FUNCTIES KAST
#def kast_on_click():
def kast_on_click(kast_id, kast_naam):
    print("kast geklikt", kast_id, kast_naam)
    print("categorieen : ",get_categorie(kast_naam))

#FUNCTIES START FRAME
def create_right_frame(parent):
    right_frame = tk.Frame(parent)
    
    #title = tk.Label(right_frame, text="right frame")
    #title.pack(padx=10, pady=10)

    leerling = tk.Label(right_frame, text="Geen leerling geselecteerd")
    #leerling.pack(padx=10, pady=10) => als we knoppen met grid willen positioneren, dan moet deze pack ook vervangen worden door een grid
    #maar 1 pack manager per bestand!
    leerling.grid(row=0, column=0, padx=10, pady=10)

    #je krijgt drie lijsten terug van de get_kasten methode!
    lijst_kasten_ids, lijst_kasten, lijst_bestandsnamen = get_kasten()
    #zorg ervoor dat de referenties naar de afbeeldingen bekend blijven in je frame, ook als de ophalen gedaan is
    #dit doe je bijvoorbeeld door deze op het frame zelf in een lijst bij te houden.
    right_frame.lijst_kast_images = []
    row_teller = 3  #3e rij omdat we boven de knoppen de naam van de leerling tonen op het scherm
    col_teller = 0 
    kast_index = 0
    if lijst_kasten:        
        while kast_index < len(lijst_kasten):
            #pad naar de afbeelding instellen
            icoon_pad = os.path.join(SCRIPT_DIR, IMG_LOCATION, IMG_LOCATION_NAME, lijst_bestandsnamen[kast_index])
            #print(f"DEBUG: Pad='{icoon_pad}' Bestaat={os.path.exists(icoon_pad)}")
            if os.path.exists(icoon_pad):
                kast_img = Image.open(icoon_pad).resize((200, 200))
                kast_img_tk = ImageTk.PhotoImage(kast_img)
                right_frame.lijst_kast_images.append(kast_img_tk) #referentie behouden
            else:
                kast_img_tk = ImageTk.PhotoImage(Image.new("RGB", (200, 200), color="gray"))
                right_frame.lijst_kast_images.append(kast_img_tk)

            kast_knop = tk.Button(
                right_frame,
                image=kast_img_tk,
                text=lijst_bestandsnamen[kast_index], 
                compound="top", 
                width=250,
                height=220,
                #command=kast_on_click
                #lambda = een anonieme (naamloze) functie in één regel waardoor je in staat bent om bijv waarden mee te geven aan het uit
                #te voeren commando bij het drukken op een knop.
                command=lambda kast_id=lijst_kasten_ids[kast_index], kast_naam=lijst_kasten[kast_index]: kast_on_click(kast_id, kast_naam)
                )
            kast_knop.image = kast_img_tk  #om de referentie naar de afbeelding te verzekeren
            #max 3 knoppen per rij instellen, dus pack manager voor dit frame omvormen naar grid
            kast_knop.grid(row=row_teller, column=col_teller, padx=3, pady=3)
            if col_teller == 2:
                col_teller = 0
                row_teller = row_teller + 1
            else:
                col_teller = col_teller + 1

            kast_index = kast_index + 1


    def toon_leerling(naam):
        leerling.config(text=f"Geselecteerde leerling: {naam}")

    def reset_leerling():
        leerling.config(text="Geen leerling geselecteerd")

    #Toegankelijk maken via right_frame
    right_frame.reset_leerling = reset_leerling
    right_frame.toon_leerling = toon_leerling

>>>>>>> 4ea80e0 (Initial Version)
    return right_frame