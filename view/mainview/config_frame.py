import tkinter as tk

def create_config_frame(parent,sluit_config_callback):
    config_frame = tk.Frame(parent)

    home_knop = tk.Button(config_frame,text="sluit config",width=15,command=sluit_config_callback)
    home_knop.pack(padx=10,pady=10)

    return config_frame