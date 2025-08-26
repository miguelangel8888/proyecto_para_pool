import tkinter as tk
#from tkinter import ttk

class BillarApp(tk.Tk):
    def __init__(self):
        super().__init__()
        # --- Ventana principal ---
        self.title("GOSTHPOOL 🎱")
        self.geometry("900x600") # Dimensión estática
        self.resizable(False, False) # No se puede cambiar el tamaño
        self.configure(bg="#181817")

        self.mi_frame=tk.Frame(self)
        self.mi_frame.pack()
        # --- Label "Mesa 1" ---
        self.label_mesa1 = tk.Label(
            self.mi_frame,
            text="Mesa 1",
            font=("Arial", 24, "bold"),
            fg="white",
            bg="#181817"
        )
        self.label_mesa1.pack(pady=50) # mejorar 

        self.boton_inicio=tk.Button(self.mi_frame, text="Inicio",font=("Arial", 16, "bold"))
        self.boton_inicio.place(x=50, y=50)


if __name__ == "__main__":
    app = BillarApp()
    app.mainloop()