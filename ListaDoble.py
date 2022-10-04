#Lista/Clase para manejar puntos de atencion

class puntoAtencion:
    def __init__(self,id,nombre,direccion):
        self.id=id
        self.nombre=nombre
        self.direccion=direccion
        self.anterior=None
        self.siguiente=None


class ListaDoble():
    def __init__(self):
        self.inicio=None
    
    def insertarPuntoAtencion(self,id,nombre,direccion):
        nuevo=puntoAtencion(id,nombre,direccion)
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
            print('id ',tmp.id,' Nombre ',tmp.nombre,' Direccion ',tmp.direccion)
            tmp=tmp.siguiente