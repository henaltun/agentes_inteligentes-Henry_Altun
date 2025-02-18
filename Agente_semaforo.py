import time
import random

class SemaforoInteligente:
    def __init__(self):
        self.estado = "rojo"  # Estado inicial
        self.duracion = {"verde": 5, "amarillo": 2, "rojo": 5}  # Tiempos base

    def detectar_trafico(self):
        """Simula la detección de vehículos (de 0 a 20)"""
        return random.randint(0, 20)

    def ajustar_tiempos(self, num_vehiculos):
        """Ajusta la duración de los estados según el tráfico"""
        if num_vehiculos > 15:
            self.duracion["verde"] = 8  # Más tráfico, luz verde más larga
            self.duracion["rojo"] = 6
        elif num_vehiculos > 5:
            self.duracion["verde"] = 6  # Tráfico moderado
            self.duracion["rojo"] = 5
        else:
            self.duracion["verde"] = 4  # Poca afluencia, ciclos más cortos
            self.duracion["rojo"] = 4
        self.duracion["amarillo"] = 2  # El amarillo mantiene su tiempo

    def cambiar_estado(self):
        """Cambia el estado del semáforo cíclicamente"""
        if self.estado == "rojo":
            self.estado = "verde"
        elif self.estado == "verde":
            self.estado = "amarillo"
        else:
            self.estado = "rojo"

    def iniciar(self):
        """Ejecuta el semáforo de forma continua"""
        while True:
            num_vehiculos = self.detectar_trafico()
            self.ajustar_tiempos(num_vehiculos)
            
            print(f"🚦 Estado: {self.estado.upper()} | Vehículos detectados: {num_vehiculos} | Duración: {self.duracion[self.estado]}s")
            time.sleep(self.duracion[self.estado])  # Espera según el estado actual
            
            self.cambiar_estado()

# Ejecutar el semáforo
if __name__ == "__main__":
    semaforo = SemaforoInteligente()
    semaforo.iniciar()
