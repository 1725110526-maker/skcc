class Transporte:
    def __init__(self,modo,operador,capacidad,origen,destino,
                 horario,duracion,precio,frecuencia,ruta):
        self.modo = modo
        self.operador = operador
        self.capacidad = capacidad
        self.origen = origen
        self.destino = destino
        self.horario = horario
        self.duracion = duracion
        self.precio = precio
        self.frecuencia = frecuencia
        self.ruta = ruta

    def avance(self):
        print("Avanza para que llegues a tu destino")
    def frena(self):
        print("Para que no choque")
    def gira(self):
        ("Para irse por las curvas")
    def impacto(self):
        print("Ijoles ya choco")
    def control(self):
        print("Control del volante para que no vuelvan a chocar") 

        print(f"Modo {self.modo}")
        print(f"Operador {self.operador}")
        print(f"Capacidad {self.capacidad}")
        print(f"Origen {self.origen}")
        print(f"Destino {self.destino}")
        print(f"Horario {self.horario}")
        print(f"Duracion {self.duracion}")
        print(f"Precio {self.precio}")
        print(f"Frecuencia {self.frecuencia}")
        print(f"Ruta {self.ruta}")
autobus = Transporte("Autobus", "Free", "40 pasajeros", "Puebla", "Morelia",
                     "14:00-17:00","3 horas", "350 pesos", "cada 30 min", "Autopista")