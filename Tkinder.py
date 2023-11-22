#from tkinter import *
# import tkinter as tk

# def restaurante():
#     nombre= "Restaurante propio"







# def  saludar():
#    texto['text'] = "Hola amigo" 
# def  despedir(): 
#   texto['text'] = "Hasta la vista"
#  # Ventana principal
# principal = tk.Tk()
#  # Título de la ventana 
# principal.wm_title("Programilla") 
# # Texto que se muestra 
# texto = tk.Label(principal, text="Saluda") 
# # Botones
# boton_saluda = tk.Button(principal, text="Hola", command=saludar)
# boton_despide = tk.Button(principal, text="Adios", command=despedir) 
# texto.pack() 
# boton_saluda.pack() 
# boton_despide.pack()
# principal.mainloop()

import tkinter as tk


import tkinter as tk

class MyRestaurantApp:
    def __init__(self, master):
        self.master = master
        master.geometry("500x500")
        master.title("MY RESTAURANT")
        master.resizable(True, False)
        master.configure(bg="grey")

        self.create_widgets()

    def create_widgets(self):
        # Título del restaurante
        label_title = tk.Label(self.master, text="MY RESTAURANT", bg="green", font=("Helvetica", 16))
        label_title.pack(pady=10)

        # Descripción del restaurante
        label_description = tk.Label(self.master, text=
        """
        Our restaurant is a place where we offer 
        a variety of delicious dishes and culinary resources
        to the public to satisfy your culinary needs and make 
        you enjoy an exceptional dining experience.
        """, bg="orange")
        label_description.pack(pady=10)

        # Botón de CHECK IN
        button_checkin = tk.Button(self.master, text="CHECK IN", bg="yellow", width=15, height=2)
        button_checkin.pack(pady=5)

        # Botón de LOG IN
        button_login = tk.Button(self.master, text="LOG IN", bg="red", width=15, height=2)
        button_login.pack(pady=5)

if __name__ == "__main__":
    ventana = tk.Tk()
    app = MyRestaurantApp(ventana)
    ventana.mainloop()

