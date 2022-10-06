from ListaDobleEscritorios import ListaEscritorio
from ListaEscritoriosActivos import ListaEscritorioActivo

class PuntoAtencion:
    def __init__(self,id,nombre,direccion):
        self.id=id
        self.nombre=nombre
        self.direccion=direccion
        self.lista_escritorios=ListaEscritorio()
        self.lista_escritoriosactivos=ListaEscritorioActivo()
        self.anterior=None
        self.siguiente=None




