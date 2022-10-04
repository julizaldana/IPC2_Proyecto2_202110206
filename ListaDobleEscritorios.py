from Escritorio import Escritorio

class ListaEscritorio():
    def __init__(self):
        self.inicio=None
    
    def insertarEscritorio(self,id,identificacion,encargado):
        nuevo=Escritorio(id,identificacion,encargado)
        if self.inicio is None:
            self.inicio=nuevo
        else:
            tmp=self.inicio
            while tmp.siguiente is not None:
                tmp=tmp.siguiente
            tmp.siguiente=nuevo
            nuevo.anterior=tmp

    def mostrarEscritorio(self):
        tmp=self.inicio
        while tmp is not None:
            print('id: ',tmp.id,' Identificacion: ',tmp.identificacion,' Encargado: ',tmp.encargado)
            tmp=tmp.siguiente