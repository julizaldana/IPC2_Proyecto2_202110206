from ListaDoble import ListaDoble
class Empresa:
    def __init__(self, id, nombre, abreviatura):
        self.id=id
        self.nombre=nombre
        self.abreviatura=abreviatura
        self.lista_puntoAtencion=ListaDoble()
        self.siguiente=None
    
    def getPuntoAtencion(self):
        return self.lista_puntoAtencion
