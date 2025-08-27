import tkinter as tk
#from src.utils.cronometro import actualizar_tiempo

class BillarApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GHOSTPOOL 🎱")
        self.geometry("900x500")
        #self.resizable(False, False)
        self.configure(bg="#181817")
        self.minutos=0
        self.segundos=0
        self.contando=False
        self.precio=0

        # --- Frame principal ---
        self.mi_frame = tk.Frame(self, bg="#181817", padx=20, pady=20)
        self.mi_frame.pack(fill="x")

        #titulo

        self.label_titulo = tk.Label(self.mi_frame,text="GhostPool",font=("Arial", 24, "bold"),fg="white",
            bg="#181817")
        
        self.label_titulo.grid(row=0, column=0, sticky="w")

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
        self.boton_inicio.grid(row=1, column=1, padx=10)  # espacio a la derecha del label

        # --- Botón Pausar ---
        self.boton_pausa = tk.Button(
            self.mi_frame,
            command=self.boton_pausar,
            text="Pausa",
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

        # --- Ajustar columnas para que no se compriman ---
        for c in range(3):
            self.mi_frame.grid_columnconfigure(c, weight=1)

    def actualizar_tiempo(self):
        if self.contando:
            self.segundos+=1
            horas = self.minutos//60
            minutos = self.segundos//60 # manejar precio dividido 5
            segundos = self.segundos%60
            self.label_tiempo.config(text=f"{horas:02d}:{minutos:02d}:{segundos:02d}")
            self.after(1000,self.actualizar_tiempo)  


    #funcion inicio
    def boton_iniciar(self):
        if not self.contando:
            self.contando = True
            self.actualizar_tiempo()
            


    def boton_parar(self):
        self.contando = False
        
        
        
    def boton_pausar(self):
        if not self.contando:
            self.contando = True
            self.actualizar_tiempo()

if __name__ == "__main__":
    app = BillarApp()
    app.mainloop()