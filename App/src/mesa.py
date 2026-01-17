import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import pygame # type: ignore
from recursos import recurso


class Mesa:
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
        pygame.mixer.music.load(recurso("Alarma.mp3"))
        self.extras_mesa1 = []
        self.tiempo_var = tk.IntVar()
        #self.tiempo_var.set(1)
        

        self.frame = tk.Frame(frame, bd=2, relief="ridge", padx=10, pady=5, bg="#181817")
        self.frame.config(width=900, height=75)
        #self.frame.grid_propagate(False)
        self.label_mesa1 = tk.Label(
            self.frame,
            text=f"Mesa {self.numero}", width = 20, anchor="w",
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#181817"
        )

        self.label_mesa1.grid(row=0, column=0, sticky="w") 

        self.boton_inicio = tk.Button(
            self.frame,
            command=self.boton_iniciar,
            text="Iniciar",
            font=("Arial", 10, "bold"),
            width=7,
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
            font=("Arial", 10, "bold"),
            width=7,
            height=1,
            bg="blue",
            fg="white",
            
        )
        self.boton_pausa.grid(row=0, column=2, padx=5)

        # --- Botón Stop ---
        self.boton_stop = tk.Button(
            self.frame,
            text="Detener",
            font=("Arial", 10, "bold"),
            width=7,
            height=1,
            bg="red",
            fg="white",
            command=self.boton_parar
        )
        self.boton_stop.grid(row=0, column=3, padx=5)  # espacio a la derecha del botón Inicio
        # label tiempo
        self.label_tiempo = tk.Label(self.frame,text="00:00:00",font=("Arial", 18, "bold"),fg="white",
            bg="#181817")
        
        self.label_tiempo.grid(row=0, column=4, padx=(18,10))

        # label precio
        self.label_precio = tk.Label(self.frame,text="0.0 BS.", width= 7,font=("Arial", 18, "bold"),fg="white",
            bg="#181817")
        self.label_precio.grid(row=0, column=5)

        #botones con frame eliminar y agregar

        frame_botones = tk.Frame(self.frame)  # Frame interno
        frame_botones.grid(row=0, column=6)   # Una sola celda de la grilla

        boton_agregar = tk.Button(frame_botones, text=" + ", font=("Arial", 10, "bold"),width=3,
    height=1, command=self.agregar_extra)
        boton_agregar.pack()  # Se apilan automáticamente

        boton_eliminar = tk.Button(frame_botones, text=" - ", font=("Arial", 10, "bold"),width=3,
    height=1, command=self.eliminar_extra)
        boton_eliminar.pack()

        #####
        self.lista_extras = tk.Listbox(self.frame, width=18, height=3, font=("Arial", 10))
        self.lista_extras.grid(row=0,column=7, padx=8)

        self.boton_eliminar_mesa = tk.Button(self.frame, text="X", bg="red", fg="white",command=self.eliminar_mesa)
        self.boton_eliminar_mesa.grid(row=0, column=8, padx=10)
        
    def actualizar_tiempo(self):
        if self.contando:
            self.segundos+=1
            horas = self.minutos//60
            minutos = self.segundos//60 
            segundos = self.segundos%60
            precio = round(minutos*0.234,2)
            if self.tiempo_limite <= minutos and self.tiempo_habilitado==True:
                self.label_tiempo.config(text=f"{horas:02d}:{minutos:02d}:{segundos:02d}")
                self.label_precio.config(text=f"{precio} BS.")
                self.label_tiempo.config(fg="red")
                if not self.tono:
                    self.tiempo_habilitado==False
                    self.tono=True
                    pygame.mixer.music.set_volume(1.0)
                    pygame.mixer.music.play()

            else:
                self.label_tiempo.config(text=f"{horas:02d}:{minutos:02d}:{segundos:02d}")
                self.label_precio.config(text=f"{precio} BS.")    

            self.frame.after(1000,self.actualizar_tiempo)  


    #funcion inicio
    def boton_iniciar(self):
        if not self.contando:
            self.contando = True
            self.boton_stop.config(text="Detener")
            self.boton_inicio.config(text="Iniciar")
            self.actualizar_tiempo()
            


    def boton_parar(self):
        if self.contando: 
            self.contando= False
            self.boton_stop.config(text="Borrar")
            self.boton_inicio.config(text="Seguir")
        else:
            self.boton_stop.config(text="Detener")
            self.boton_inicio.config(text="Iniciar")
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
        
        '''minutos = simpledialog.askinteger("Tiempo límite", "Ingrese el tiempo en minutos:", minvalue=1)
        if minutos:
            self.tiempo_limite = minutos
            self.tiempo_habilitado=True
            self.tono=False
            self.label_tiempo.config(fg="white")'''
        
        ventana = tk.Toplevel(self.frame)
        ventana.title("Tiempo de Mesa")
        ventana.resizable(False, False)

        tk.Radiobutton(
            ventana, text="1 hora", variable=self.tiempo_var, value=1
        ).pack(anchor="w")

        tk.Radiobutton(
        ventana, text="1 hora y media", variable=self.tiempo_var, value=2
        ).pack(anchor="w")

        tk.Radiobutton(
        ventana, text="2 horas", variable=self.tiempo_var, value=3
        ).pack(anchor="w")

        tk.Button(
        ventana, text="Aceptar", command=ventana.destroy
        ).pack(pady=10)

        
        ventana.wait_window()
        minutos=self.tiempo_var.get()
        
        
        
        if minutos > 0:
            print(minutos)
            self.tiempo_limite = minutos
            self.tiempo_habilitado=True
            self.tono=False
            self.label_tiempo.config(fg="white")
            self.tiempo_var.set(0)
        

    def agregar_extra(self):
        extra = simpledialog.askstring("Agregar Extra", "Descripción y monto (ej: Refresco 15):")
        if extra:
            self.extras_mesa1.append(extra)
            self.lista_extras.insert(tk.END, extra)

    def eliminar_extra(self):
            seleccion = self.lista_extras.curselection()
        
            if seleccion:
                index = seleccion[0]
                self.extras_mesa1.pop(index)
                self.lista_extras.delete(index)
            else:
                if self.extras_mesa1:
                    index = len(self.extras_mesa1) - 1
                    self.extras_mesa1.pop(index)
                    self.lista_extras.delete(index)
                
    
    def eliminar_mesa(self):
        respuesta = messagebox.askyesno("Confirmar", f"¿Estás seguro de eliminar la Mesa {self.numero}?")
    
        if respuesta:
            self.frame.destroy()
        