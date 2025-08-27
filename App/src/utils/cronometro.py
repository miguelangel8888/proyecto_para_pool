

def actualizar_tiempo(self):
            if self.contando:
                self.segundos+=1
                minutos= self.segundos//60
                segundos=self.segundos%60
                self.label_tiempo.config(text=f"{minutos:02d}:{segundos:02d}")
                self.after(1000,self.actualizar_tiempo)