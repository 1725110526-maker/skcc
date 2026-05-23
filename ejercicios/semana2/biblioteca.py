class LibroB:
    def __init__(self,nombre,lomo,formato,volumen,paginas,
                 indice,genero,voz,cubierta,paratextos):
        self.nombre = nombre
        self.lomo = lomo
        self.formato = formato
        self.volumen = volumen
        self.paginas = paginas
        self.indice = indice
        self.genero = genero
        self.voz = voz
        self.cubierta = cubierta
        self.paratextos = paratextos
        print(f"Nombre{self.nombre}")
        print(f"Lomo{self.lomo}")
        print(f"Formato{self.formato}")
        print(f"Volumen{self.volumen}")
        print(f"Paginas{self.paginas}")
        print(f"Indice{self.indice}")
        print(f"Genero{self.genero}")
        print(f"Voz{self.voz}")
        print(f"Cubierta{self.cubierta}")
        print(f"Paratextos{self.paratextos}")

    def acomodo_libros(self):
        print("Se acomodan los libros que desacomodas")
    def inventario(self):
        print("Llevan un invenrtario de los libros que tienen")
    def prestamos(self):
        ("Si quieres un libro te lo presta")
    def inscripciones(self):
        print("Te tienes que inscribir para porder llevarte un libro")
    def clasificacion(self):
        print("Clasifican los libros por genero")

HarryP = LibroB("harry potter", "rigido","fisico","4","672",
                "sin indice","ficcion","sin voz","sin cubierta","dedicatoria")