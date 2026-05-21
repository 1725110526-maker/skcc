class NombreClase:
    def __init__(self):
        print("Constructor")

    def metodoUno(self):
        print("Metodo Uno")
    
    def metodoDos(self, numero_uno:int, numero_dos:int)->int:
        """
        Este metodo realiza la suma de dos numeros enteros y regresa
        el resultado

        Args:
            numero_uno:int - Primero numero para la suma
            numero_dos:int - Segundo numero para la suma

        Returns:
            resultado:int - Variable con el resultado de la suma
        """
        resultado = numero_uno + numero_dos
        return resultado

    def metodoTres(self, numero_uno, numero_dos):
        resultado = numero_uno + numero_dos
        return resultado
    
    def metodoCuatro(self, numero_uno, numero_dos):
        resultado =  numero_uno + numero_dos
        print(f"La suma es {resultado}")



nombre_objeto = NombreClase()
