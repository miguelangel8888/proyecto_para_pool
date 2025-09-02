import tkinter as tk
#from tkinter import ttk
from tkinter import simpledialog
import pygame
from PIL import Image, ImageTk
#from src.utils.cronometro import actualizar_tiempo

class BillarApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GHOSTPOOL")
        self.geometry("1000x600")
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


        # --- Frame principal ---
        self.mi_frame = tk.Frame(self, bg="#000000", padx=20, pady=20)
        #self.mi_frame.pack(fill="x")
        self.mi_frame.pack(fill="both", expand=True)

        #crear fondo
        imagen = Image.open("GhostPoolOficial.png")
        imagen = imagen.resize((1000, 600))  # ajustar al tamaño del frame
        self.foto_fondo = ImageTk.PhotoImage(imagen)

        self.label_fondo = tk.Label(self.mi_frame, image=self.foto_fondo)
        self.label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

        #titulo

        self.label_titulo = tk.Label(self.mi_frame,text="GhostPool",font=("Arial", 24, "bold"),fg="white",
            bg="#181817")
        
        self.label_titulo.grid(row=0, column=0, sticky="w")

        #titulo Precio

        self.label_titulo_precio = tk.Label(self.mi_frame,text="Precio",font=("Arial", 24, "bold"),fg="white",
            bg="#181817")
        
        self.label_titulo_precio.grid(row=0, column=5)

        # --- Label Mesa 1 ---
        self.label_mesa1 = tk.Label(
            self.mi_frame,
            text="Mesa 1",
            font=("Arial", 20, "bold"),
            fg="white",
            bg="#181817"
        )
        self.label_mesa1.grid(row=1, column=0, sticky="w")  # izquierda

        

        # --- Botón Inicio ---
        self.boton_inicio = tk.Button(
            self.mi_frame,
            command=self.boton_iniciar,
            text="Inicio",
            font=("Arial", 14, "bold"),
            width=8,
            height=1,
            bg="green",
            fg="white",
            
        )
        self.boton_inicio.grid(row=1, column=1, padx=2)  # espacio a la derecha del label

        # --- Botón Pausar ---
        self.boton_pausa = tk.Button(
            self.mi_frame,
            command=self.boton_pausar,
            text="Tiempo",
            font=("Arial", 14, "bold"),
            width=8,
            height=1,
            bg="blue",
            fg="white",
            
        )
        self.boton_pausa.grid(row=1, column=2, padx=5)

        # --- Botón Stop ---
        self.boton_stop = tk.Button(
            self.mi_frame,
            text="Stop",
            font=("Arial", 14, "bold"),
            width=8,
            height=1,
            bg="red",
            fg="white",
            command=self.boton_parar
        )
        self.boton_stop.grid(row=1, column=3, padx=10)  # espacio a la derecha del botón Inicio
        # label tiempo
        self.label_tiempo = tk.Label(self.mi_frame,text="00:00:00",font=("Arial", 20, "bold"),fg="white",
            bg="#181817")
        
        self.label_tiempo.grid(row=1, column=4)

        # label precio
        self.label_precio = tk.Label(self.mi_frame,text="0.0 BS.",font=("Arial", 20, "bold"),fg="white",
            bg="#181817")
        self.label_precio.grid(row=1, column=5)

        # Boton agregar extra

        self.boton_agregar_extra = tk.Button(self.mi_frame, text="Agregar",font=("Arial", 14, "bold"), command=self.agregar_extra )
        self.boton_agregar_extra.grid(row=1, column=6)

        self.lista_extras = tk.Listbox(self.mi_frame, width=15, height=3, font=("Arial", 14))
        self.lista_extras.grid(row=1,column=7)

        # --- Ajustar columnas para que no se compriman ---
        for c in range(3):
            self.mi_frame.grid_columnconfigure(c, weight=1)

    def actualizar_tiempo(self):
        if self.contando:
            self.segundos+=1
            horas = self.minutos//60
            minutos = self.segundos//60 
            segundos = self.segundos%60
            precio = round(minutos*0.2,2)
            if self.tiempo_limite <= minutos and self.tiempo_habilitado==True:
                self.label_tiempo.config(text=f"{horas:02d}:{minutos:02d}:{segundos:02d}")
                self.label_precio.config(text=f"{precio} BS.")
                self.label_tiempo.config(fg="red")
                if not self.tono:
                    self.tono=True
                    pygame.mixer.music.play()
            else:
                self.label_tiempo.config(text=f"{horas:02d}:{minutos:02d}:{segundos:02d}")
                self.label_precio.config(text=f"{precio} BS.")    

            self.after(1000,self.actualizar_tiempo)  


    #funcion inicio
    def boton_iniciar(self):
        if not self.contando:
            self.contando = True
            self.boton_stop.config(text="Stop")
            self.boton_inicio.config(text="Inicio")
            self.actualizar_tiempo()
            


    def boton_parar(self):
        if self.contando: 
            self.contando= False
            self.boton_stop.config(text="Borrar")
            self.boton_inicio.config(text="Seguir")
        else:
            self.boton_stop.config(text="Stop")
            self.boton_inicio.config(text="Inicio")
            self.minutos=0
            self.segundos=0
            self.precio=0
            self.tiempo_limite=0
            self.tono=False
            self.tiempo_habilitado=False
            self.label_tiempo.config(fg="white")
            self.label_tiempo.config(text="00:00:00")
            self.label_precio.config(text="0.0 BS.")
            self.lista_extras.delete(0, tk.END)
            self.extras_mesa1.clear()

        
    def boton_pausar(self):
        
        minutos = simpledialog.askinteger("Tiempo límite", "Ingrese el tiempo en minutos:", minvalue=1)
        if minutos:
            self.tiempo_limite = minutos
            self.tiempo_habilitado=True

    def agregar_extra(self):
        extra = simpledialog.askstring("Agregar Extra", "Descripción y monto (ej: Refresco 15):")
        if extra:
            self.extras_mesa1.append(extra)
            self.lista_extras.insert(tk.END, extra)

if __name__ == "__main__":
    app = BillarApp()
    app.mainloop()