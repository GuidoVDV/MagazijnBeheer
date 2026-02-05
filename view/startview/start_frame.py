<<<<<<< HEAD
#IMPORTS
import tkinter as tk

#FUNCTIES START FRAME
def create_start_frame(parent, start_app_callback):
    start_frame = tk.Frame(parent)

    label = tk.Label(start_frame, text="Hello World")
    label.pack(padx=10, pady=10)

    start_button = tk.Button(start_frame, text="Start Applicatie", command=start_app_callback)
    start_button.pack(pady=20)
    
=======
#IMPORTS
import tkinter as tk

#FUNCTIES START FRAME
def create_start_frame(parent, start_app_callback):
    start_frame = tk.Frame(parent)

    label = tk.Label(start_frame, text="Hello World")
    label.pack(padx=10, pady=10)

    start_button = tk.Button(start_frame, text="Start Applicatie", command=start_app_callback)
    start_button.pack(pady=20)
    
>>>>>>> 4ea80e0 (Initial Version)
    return start_frame