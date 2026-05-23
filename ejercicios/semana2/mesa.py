class Mesa:
    def __init__(self,material,ancho,disenio,tamanio,tipo,
                 altura,color,portabilidad,soporte,no_patas):
        self.material = material
        self.ancho = ancho
        self.disenio = disenio
        self.tamanio = tamanio
        self.tipo = tipo
        self.altura = altura
        self.color = color
        self.portabilidad = portabilidad
        self.soporte = soporte
        self.no_patas = no_patas
        print(f"Material {self.material}")
        print(f"Ancho{self.ancho}")
        print(f"Diseño {self.disenio}")
        print(f"Tamaño {self.tamanio}")
        print(f"Tipo {self.tipo}")
        print(f"Altura {self.altura}")
        print(f"Color {self.color}")
        print(f"Portabilidad {self.portabilidad}")
        print(f"Soporte {self.soporte}")
        print(f"No. Patas {self.no_patas}")

    def comer(self):
        print("Por si no tienes escritorio usas la mesa")
    def comer(self):
        print("Para que no comas en el piso usas la mesa")
    def hacer_comer(self):
        ("Para que piques la verdura")
    def platicar(self):
        print("Por si no tienes una sala, usas la mesa para platicar")
    def poner_bebida(self):
        print("Para que pongas las bebidas al final de curso")
mesa_vidrio = Mesa("Fierro", "1.5m", "Moderno", "Pequeño", "Sala de estar", 
                   "0.75m", "Negro", "No portable", "Fuerte", "2")        