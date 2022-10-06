from EscritorioActivo import EscritorioActivo
from ListaDobleEscritorios import ListaEscritorio

Lista_Escritorios = ListaEscritorio()

class ListaEscritorioActivo():
    def __init__(self):
        self.inicio=None
    
    def insertarEscritorioActivo(self,id):
        nuevo=EscritorioActivo(id)
        if self.inicio is None:
            self.inicio=nuevo
        else:
            tmp=self.inicio
            while tmp.siguiente is not None:
                tmp=tmp.siguiente
            tmp.siguiente=nuevo
            nuevo.anterior=tmp

    def mostrarEscritorioActivo(self):
        tmp=self.inicio
        while tmp is not None:
            print('id Escritorio Activo: ',tmp.id)
            tmp=tmp.siguiente

    def eliminarEscritorioActivo(self,id):
        tmp=self.inicio
        while tmp is not None:
            if tmp.id==id:
                self.inicio=tmp.siguiente
                tmp.siguiente=None
                print('Escritorio ',tmp.id,' fue desactivado')
                break
            elif tmp.siguiente is not None:
                if tmp.siguiente.id==id:
                    nodo_a_borrar=tmp.siguiente
                    tmp.siguiente=nodo_a_borrar.siguiente
                    nodo_a_borrar.siguiente=None
                    print('Escritorio ',tmp.id,' fue desactivado')
                    break
            tmp=tmp.siguiente



    def getEscritorioActivo(self, id):
        tmp=self.inicio
        while tmp is not None:
            if tmp.id==id:
                return tmp
            tmp=tmp.siguiente
        return None

