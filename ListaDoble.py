from mimetypes import init
from PuntoAtencion import PuntoAtencion

class ListaDoble():
    def __init__(self):
        self.inicio=None
    
    def insertarPuntoAtencion(self,id,nombre,direccion):
        nuevo=PuntoAtencion(id,nombre,direccion)
        if self.inicio is None:
            self.inicio=nuevo
        else:
            tmp=self.inicio
            while tmp.siguiente is not None:
                tmp=tmp.siguiente
            tmp.siguiente=nuevo
            nuevo.anterior=tmp

    def mostrarPuntoAtencion(self):
        tmp=self.inicio
        while tmp is not None:
            print('id: ',tmp.id,' Nombre: ',tmp.nombre,' Direccion: ',tmp.direccion)
            tmp=tmp.siguiente

    def getPuntoAtencion(self,id):
        tmp=self.inicio
        while tmp is not None:
            if tmp.id==id:
                return tmp
            tmp=tmp.siguiente
        return None