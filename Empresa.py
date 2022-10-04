from ListaDoble import ListaDoble
from ListaDobleEscritorios import ListaEscritorio
from ListaTransacciones import ListaTransacciones

class Empresa:
    
    def __init__(self, id, nombre, abreviatura):
        self.id=id
        self.nombre=nombre
        self.abreviatura=abreviatura
        self.lista_puntoAtencion=ListaDoble()
        self.lista_escritorios=ListaEscritorio()
        self.lista_transacciones=ListaTransacciones()
        self.siguiente=None
    
    def getPuntoAtencion(self):
        return self.lista_puntoAtencion
