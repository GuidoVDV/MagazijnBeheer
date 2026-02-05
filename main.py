# IMPORT
import tkinter as tk
from view.startview.start_frame import create_start_frame
from view.mainview.menu_frame import create_menu_frame
from view.mainview.right_frame import create_right_frame
from view.mainview.left_frame import create_left_frame
from view.mainview.config_frame import create_config_frame
#FUNCTIES
#Functies om frames te tonen/verbergen
def show_frame(frame:tk.Frame, side_option:str="top", fill_option:str="both", expand_option:bool=False, hide=False):
    if hide:
        frame.pack_forget()
    else:
        frame.pack(side=side_option, fill=fill_option, expand=expand_option)

#functie om van start -> hoofdscherm te gaan
def start_app():
    menu_frame.pack(side="top", fill="x")
    show_frame(start_frame, hide=True)
    content_container.pack(fill="both",expand=True)
    show_frame(left_frame, side_option="left",fill_option="y", expand_option=False)
    show_frame(right_frame, side_option="left",fill_option="both", expand_option=True)

#Funcite om naar config scherm te gaan.
#PRE start_frame, left_frame, right_frame en config_frame bestaan.
def start_config():
    show_frame(start_frame, hide=True)
    content_container.pack(fill ="both", expand=True)
    show_frame(config_frame)
    show_frame(left_frame, hide=True)
    show_frame(right_frame, hide=True)

#Funcite om van config scherm terug te keren naar het hoofdscherl.
#PRE start_frame, left_frame, right_frame en config_frame bestaan.
def sluit_config():
    show_frame(start_frame, hide=True)
    content_container.pack(fill ="both", expand=True)
    show_frame(config_frame,hide=True)
    show_frame(left_frame, side_option="left", fill_option="y", expand_option=False)
    show_frame(right_frame, side_option="left", fill_option="both", expand_option=True)

#MAIN
if __name__ == "__main__":

    root = tk.Tk()
    root.title("Magazijnbeheer")
    root.geometry("900x600")

    #main container
    main_container = tk.Frame(root)
    main_container.pack(fill="both", expand=True)

    #FRAMES aanmaken in main container
    start_frame = create_start_frame(main_container, start_app)
    menu_frame = create_menu_frame(main_container, start_config)
    #start_frame.pack()
    menu_frame = create_menu_frame(main_container, start_config)
   


    #content container als sub container voor linker/rechter frame
    content_container = tk.Frame(main_container)
    right_frame = create_right_frame(content_container)
    left_frame = create_left_frame(content_container, on_leerling_selected=right_frame.toon_leerling, right_frame=right_frame)
    
    config_frame = create_config_frame(content_container,sluit_config)

    #STARTEN MET START_FRAME
    show_frame(start_frame,"top", "both")

    root.mainloop()