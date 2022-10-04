from Transaccion import Transaccion

class ListaTransacciones():

    def __init__(self):
        self.inicio=None
    
    def insertarTransaccion(self,id,nombre,tiempoAtencion):
        nuevo=Transaccion(id,nombre,tiempoAtencion)
        if self.inicio is None:
            self.inicio=nuevo
        else:
            tmp=self.inicio
            while tmp.siguiente is not None:
                tmp=tmp.siguiente
            tmp.siguiente=nuevo
            nuevo.anterior=tmp

    def mostrarTransacciones(self):
        tmp=self.inicio
        while tmp is not None:
            print('id: ',tmp.id,' Nombre: ',tmp.nombre,' Tiempo de duración de atención: ',tmp.tiempoAtencion)
            tmp=tmp.siguiente