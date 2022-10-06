from Escritorio import Escritorio


#Lista para escritorios

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


    def getEscritorio(self, id):
        tmp=self.inicio
        while tmp is not None:
            if tmp.id==id:
                return tmp
            tmp=tmp.siguiente
        return None

