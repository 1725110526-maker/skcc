class Smartphone:
    def __init__(self, marca, modelo, color, ram, memoria,
                 serie,pantalla,procesador,bateria,conectividad):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.ram = ram
        self.memoria = memoria
        self.serie = serie
        self.pantalla = pantalla
        self.procesador = procesador
        self.bateria = bateria
        self.conectividad = conectividad
        print(f"Marca {self.marca}")
        print(f"Modelo {self.modelo}")
        print(f"Color {self.color}")
        print(f"Ram {self.ram}")
        print(f"Memoria {self.memoria}")
        print(f"Serie {self.serie}")
        print(f"Pantalla {self.pantalla}")
        print(f"Procesador {self.procesador}")
        print(f"Bateria {self.bateria}")
        print(f"Conectividad {self.conectividad}")

    def fotos(self):
        print("Te permite tomarte fotos con filtro")
    def comunicacion(self):
        print("Te permite estar comunicado para saber el chisme")
    def captura(self):
        ("Le tomas captura a un chisme para poder pasarlo a alguien mas")
    def linterna(self):
        print("Enciendes la linterna por que no encuntras el celular")
    def sonido(self):
        print("Te avisa cuando ya te llego la actualizacion al chisme") 

samsung= Smartphone("Samsung","Galaxy S25 Ultra","Lila","12GB","256GB",
                    "Serie S","6.9 pulgadas","Snapdragon 8 Elite","5000mAh","5G, Wi-Fi")