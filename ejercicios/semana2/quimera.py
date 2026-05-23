class Quimera:
    def __init__(self,color,peso,altura,tamanio,sexo,
                 temperamento,fuerza_de_mordedura,agilidad,grosor,pelaje):
        self.color = color
        self.peso = peso
        self.altura = altura
        self.tamanio = tamanio
        self.sexo = sexo
        self.temperamento = temperamento
        self.fuerza_de_mordedura = fuerza_de_mordedura
        self.agilidad = agilidad
        self.grosor = grosor
        self.pelaje = pelaje
        print(f"Color {self.color}")
        print(f"Peso {self.peso}")
        print(f"Altura {self.altura}")
        print(f"Tamanio {self.tamanio}")
        print(f"Sexo {self.sexo}")
        print(f"Temperamento {self.temperamento}")
        print(f"Fuerza de Mordedura {self.fuerza_de_mordedura}")
        print(f"Agilidad {self. agilidad}")
        print(f"Grosor {self.grosor}")
        print(f"Pelaje {self.pelaje}")

    def lanzar(self):
        print("Lanza aliento de fuego")
    def embestida(self):
        print("Ataca con rudeza")
    def morder(self):
        ("Activa el veneno de sus colmillos al morder")
    def cambiar(self):
        print("Cambia la forma de ataque")
    def soltar(self):
        print("Tiene complejo de canjuro") 

quimera1 = Quimera("Negro con rojo", "100kg", "1.5m", "Enorme", "Femenino",
                   "Feroz", "1000N", "100%", "15cm", "Suave")
