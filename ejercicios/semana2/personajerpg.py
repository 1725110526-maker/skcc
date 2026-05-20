class Personaje_rpg:
    def __init__(self,fuerza,agilidad,punteria,resistencia,salud,
                 intuicion,percepcion,altura,peso,equipo):
        self.fuerza = fuerza
        self.agilidad = agilidad
        self.punteria = punteria
        self.resistencia = resistencia 
        self.salud = salud
        self.intuicion = intuicion
        self.percepcion = percepcion
        self.altura = altura
        self.peso = peso
        self.equipo = equipo
        print(f"Fuerza {self.fuerza}")
        print(f"Agilidad {self.agilidad}")
        print(f"Punteria {self.punteria}")
        print(f"Resistencia {self.resistencia}")
        print(f"Salud {self.salud}")
        print(f"Intuicion {self.intuicion}")
        print(f"Percepcion {self.percepcion}")
        print(f"Altura {self.altura}")
        print(f"Peso {self.peso}")
        print(f"Equipo {self.equipo}")
ghost= Personaje_rpg("Sobresaliente", "Alta", "Maestro", "Extrema", "Robusto",
                     "Aguda", "Excepcional", "1.89cm", "90-100kg", "Mascara de calabera")


