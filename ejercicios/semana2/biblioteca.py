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
HarryP = LibroB("")