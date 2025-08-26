import tkinter as tk

class BillarApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GHOSTPOOL 🎱")
        self.geometry("900x200")
        self.resizable(False, False)
        self.configure(bg="#181817")

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
            text="Inicio",
            font=("Arial", 14, "bold"),
            width=8,
            height=1,
            bg="green",
            fg="white"

        )
        self.boton_inicio.grid(row=1, column=1, padx=20)  # espacio a la derecha del label

        # --- Botón Stop ---
        self.boton_stop = tk.Button(
            self.mi_frame,
            text="Stop",
            font=("Arial", 14, "bold"),
            width=8,
            height=1,
            bg="red",
            fg="white"
        )
        self.boton_stop.grid(row=1, column=2, padx=20)  # espacio a la derecha del botón Inicio

        # --- Ajustar columnas para que no se compriman ---
        for c in range(3):
            self.mi_frame.grid_columnconfigure(c, weight=1)

if __name__ == "__main__":
    app = BillarApp()
    app.mainloop()