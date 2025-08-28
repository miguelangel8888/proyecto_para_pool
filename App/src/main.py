import tkinter as tk
import time

class BillarApp(tk.Tk):
    def __init__(self):
        super().__init__()
        # --- Ventana principal ---
        self.title("GOSTHPOOL 🎱")
        self.geometry("900x600")  # Dimensión estática
        self.resizable(False, False)  # No se puede cambiar el tamaño
        self.configure(bg="#181817")

        # --- Variables del cronómetro ---
        self.start_time = None
        self.running = False

        # --- Label "Mesa 1" ---
        self.label_mesa1 = tk.Label(
            self,
            text="Mesa 1",
            font=("Arial", 24, "bold"),
            fg="white",
            bg="#181817"
        )
        self.label_mesa1.pack(pady=20)

        # --- Label Cronómetro ---
        self.label_timer = tk.Label(
            self,
            text="00:00:00",
            font=("Arial", 30, "bold"),
            fg="cyan",
            bg="#181817"
        )
        self.label_timer.pack(pady=20)

        # --- Botón Inicio ---
        self.btn_inicio = tk.Button(
            self,
            text="Inicio",
            font=("Arial", 14, "bold"),
            fg="white",
            bg="#28a745",   # verde
            width=10,
            command=self.inicio
        )
        self.btn_inicio.pack(pady=10)

        # --- Botón Fin ---
        self.btn_fin = tk.Button(
            self,
            text="Fin",
            font=("Arial", 14, "bold"),
            fg="white",
            bg="#dc3545",   # rojo
            width=10,
            command=self.fin
        )
        self.btn_fin.pack(pady=10)

    # --- Funciones del cronómetro ---
    def update_timer(self):
        if self.running:
            elapsed = time.time() - self.start_time
            mins, secs = divmod(int(elapsed), 60)
            hours, mins = divmod(mins, 60)
            self.label_timer.config(text=f"{hours:02}:{mins:02}:{secs:02}")
            self.after(1000, self.update_timer)  # Actualiza cada segundo

    def inicio(self):
        if not self.running:
            self.start_time = time.time()
            self.running = True
            self.update_timer()
            print("La mesa 1 ha iniciado ⏱️")

    def fin(self):
        if self.running:
            self.running = False
            print("La mesa 1 ha finalizado 🛑")
            print("Tiempo final:", self.label_timer.cget("text"))

if __name__ == "__main__":
    app = BillarApp()
    app.mainloop()
