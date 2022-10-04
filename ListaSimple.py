#Clase/Lista para manejar empresas

from Empresa import Empresa


class ListaSimple():
    def __init__(self):
        self.inicio=None
        self.fin=None   


    def añadirEmpresa(self,id,nombre,abreviatura):
        nuevo=Empresa(id,nombre,abreviatura)
        if self.inicio is None:
            self.inicio=nuevo
        else:
            tmp=self.inicio
            while tmp.siguiente is not None:
                tmp=tmp.siguiente
            tmp.siguiente=nuevo

    def imprimirEmpresas(self):
        print("------------------")
        print(" La lista de empresas es:")
        print("------------------")
        tmp=self.inicio
        while tmp is not None:
            print("id: ",tmp.id,' Nombre: ',tmp.nombre,' Abreviatura: ',tmp.abreviatura)
            tmp=tmp.siguiente

    def eliminarEmpresa(self,nombre):
        tmp=self.inicio
        while tmp is not None:
            if tmp.nombre==nombre:
                self.inicio=tmp.siguiente
                tmp.siguiente=None
                print('Empresa ',tmp.nombre,' fue eliminado')
                break
            elif tmp.siguiente is not None:
                if tmp.siguiente.nombre==nombre:
                    nodo_a_borrar=tmp.siguiente
                    tmp.siguiente=nodo_a_borrar.siguiente
                    nodo_a_borrar.siguiente=None
                    print('Empresa ',nombre,' fue eliminado')
                    break
            tmp=tmp.siguiente

    def getEmpresa(self,nombre):
        tmp=self.inicio
        while tmp is not None:
            if tmp.nombre==nombre:
                return tmp
            tmp=tmp.siguiente
        return None