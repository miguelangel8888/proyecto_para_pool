import tkinter as tk
#from tkinter import ttk
from tkinter import simpledialog
import pygame # type: ignore
from PIL import Image, ImageTk # type: ignore
from mesa import mesa
#from src.utils.cronometro import actualizar_tiempo

class BillarApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GHOSTPOOL")
        self.geometry("980x700")
        self.resizable(False, False)
        self.configure(bg="#181817")
        self.minutos=0
        self.segundos=0
        self.contando=False
        self.tiempo_habilitado=False
        self.precio=0
        self.tiempo_limite=0
        self.tono=False
        pygame.mixer.init()
        pygame.mixer.music.load("Alarma.mp3")
        self.extras_mesa1 = []
        self.mesas = []
        self.contador_mesas = 0


        # --- Frame principal ---
        self.mi_frame = tk.Frame(self, bg="#000000", padx=20, pady=20)
        #self.mi_frame.pack(fill="x")
        self.mi_frame.pack(fill="both", expand=True)

        #crear fondo
        imagen = Image.open("GhostPoolOficial.png")
        imagen = imagen.resize((980, 700))  # ajustar al tamaño del frame
        self.foto_fondo = ImageTk.PhotoImage(imagen)

        self.label_fondo = tk.Label(self.mi_frame, image=self.foto_fondo)
        self.label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

        #titulo

        self.label_titulo = tk.Label(self.mi_frame,text="GhostPool",font=("Arial", 24, "bold"),fg="white",
            bg="#181817")
        
        self.label_titulo.grid(row=0, column=0, sticky="w")


        self.boton_nueva = tk.Button(self.mi_frame, text="Nueva Mesa", command=self.agregar_mesa)
        self.boton_nueva.grid(row=2, column=0)

    def agregar_mesa(self):
        self.contador_mesas = simpledialog.askstring("Nueva Mesa", "Ingrese el nombre o número de la mesa:")
        nueva = mesa(self.mi_frame, self.contador_mesas)
        fila_actual = len(self.mesas) + 4
        nueva.frame.grid(row=fila_actual, column=0, sticky="ew", padx=20, pady=5)
        self.mesas.append(nueva)

if __name__ == "__main__":
    app = BillarApp()
    app.mainloop()