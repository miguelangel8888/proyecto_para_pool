import tkinter as tk
from tkinter import simpledialog
import pygame


class mesa:
    def __init__(self, frame, numero):
        self.numero=numero
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

        self.frame = tk.Frame(frame, bd=4, relief="ridge", padx=10, pady=10, bg="#181817")
        self.frame.config(width=950, height=100)
        #self.frame.grid_propagate(False)
        self.label_mesa1 = tk.Label(
            self.frame,
            text=f"Mesa {self.numero}",
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#181817"
        )

        self.label_mesa1.grid(row=0, column=0, sticky="w") 

        self.boton_inicio = tk.Button(
            self.frame,
            command=self.boton_iniciar,
            text="Inicio",
            font=("Arial", 12, "bold"),
            width=8,
            height=1,
            bg="green",
            fg="white",
            
        )
        self.boton_inicio.grid(row=0, column=1, padx=2) 

        # --- Botón Pausar ---
        self.boton_pausa = tk.Button(
            self.frame,
            command=self.boton_pausar,
            text="Tiempo",
            font=("Arial", 12, "bold"),
            width=8,
            height=1,
            bg="blue",
            fg="white",
            
        )
        self.boton_pausa.grid(row=0, column=2, padx=5)

        # --- Botón Stop ---
        self.boton_stop = tk.Button(
            self.frame,
            text="Detener",
            font=("Arial", 12, "bold"),
            width=8,
            height=1,
            bg="red",
            fg="white",
            command=self.boton_parar
        )
        self.boton_stop.grid(row=0, column=3, padx=5)  # espacio a la derecha del botón Inicio
        # label tiempo
        self.label_tiempo = tk.Label(self.frame,text="00:00:00",font=("Arial", 20, "bold"),fg="white",
            bg="#181817")
        
        self.label_tiempo.grid(row=0, column=4)

        # label precio
        self.label_precio = tk.Label(self.frame,text="0.0 BS.",font=("Arial", 20, "bold"),fg="white",
            bg="#181817")
        self.label_precio.grid(row=0, column=5)

        # Boton agregar extra

        self.boton_agregar_extra = tk.Button(self.frame, text="Agregar",font=("Arial", 12, "bold"), command=self.agregar_extra )
        self.boton_agregar_extra.grid(row=0, column=6)

        self.lista_extras = tk.Listbox(self.frame, width=15, height=3, font=("Arial", 12))
        self.lista_extras.grid(row=0,column=7)

        self.boton_eliminar_mesa = tk.Button(self.frame, text="Eliminar", bg="red", fg="white",command=self.eliminar_mesa)
        self.boton_eliminar_mesa.grid(row=0, column=8)
        
    def actualizar_tiempo(self):
        if self.contando:
            self.segundos+=1
            horas = self.minutos//60
            minutos = self.segundos//60 
            segundos = self.segundos%60
            precio = round(minutos*0.217,2)
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

            self.frame.after(1000,self.actualizar_tiempo)  


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

    def eliminar_mesa(self):
        self.frame.destroy()
        