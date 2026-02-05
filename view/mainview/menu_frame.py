<<<<<<< HEAD
#IMPORTS
import tkinter as tk

#FUNCTIES START FRAME
def create_menu_frame(parent,start_config_callback):
    menu_frame = tk.Frame(parent, bg="lightgrey", height=50)

    config_knop = tk.Button(menu_frame,width=5,text="config",command=start_config_callback)
    config_knop.pack(anchor="e",padx=10,pady=10)

=======
#IMPORTS
import tkinter as tk

#FUNCTIES START FRAME
def create_menu_frame(parent,start_config_callback):
    menu_frame = tk.Frame(parent, bg="lightgrey", height=50)

    config_knop = tk.Button(menu_frame,width=5,text="config",command=start_config_callback)
    config_knop.pack(anchor="e",padx=10,pady=10)

>>>>>>> 4ea80e0 (Initial Version)
    return menu_frame