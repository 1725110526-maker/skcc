class Alumno:
    def __init__(self,nombre,edad,fecha_nacimiento,altura,
                 peso,color_ojos,complexion,talla_pie,alergias,no_pie):
        self.nombre =nombre
        self.edad =edad
        self.fecha_nacimiento =fecha_nacimiento
        self.altura =altura
        self.peso =peso
        self.color_ojos =color_ojos
        self.complexion =complexion
        self.talla_pie =talla_pie
        self.alergias =alergias
        self.no_pie =no_pie
        print(f"Nombre {self.nombre}")
        print(f"Edad{self.edad}")
        print(f"Fecha_nacimiento{self.fecha_nacimiento}")
        print(f"altura{self.altura}")
        print(f"Peso{self.peso}")
        print(f"color_ojos{self.color_ojos}")
        print(f"Complexion{self.complexion}")
        print(f"Talla_pie{self.talla_pie}")
        print(f"Alergias{self.alergias}")
        print(f"No_pie{self.no_pie}")

    def estudiar(self):
        print("Esta estudiando")
    def tomar_cafe(self):
        print("Toma cafe para poder estudiar")
    def caminar(self):
        ("Camina para poder llegar a la univerisad")
    def hacer_tarea(self):
        print("Realiza su tarea para poder tener buena nota")
    def rendir_examen(self):
        print("realizo bien su examen")

carlos= Alumno("Carlos","19 años","11 de diciembre 2006","1.70","58kg",
               "cafe oscuro","delgada,","6","penicilina","2 pies")