import os

from Clientes import Cliente


class ColaCliente:
    def __init__(self):
        self.primero = None
        self.contador = 0


       #VERIFICAR SI LA COLA ESTÁ VACÍA
    def estaVacia(self):
        if self.primero == None:
            return True
        else:
            return False


    #AGREGAR UN CLIENTE A LA COLA
    def encolar(self, dpi, nombre, transacciones):
        nuevo=Cliente(dpi,nombre,transacciones)
        if self.estaVacia():
            self.primero = nuevo
        else:
            temp = self.primero
            while(temp.siguiente != None):
                temp = temp.siguiente
            temp.siguiente = nuevo


    #QUITAR UN CLIENTE DE LA COLA (PRIMERA QUE SALE)
    def desencolar(self):
        if self.primero == None:
            return None
        else:
            temp = self.primero
            self.primero = self.primero.siguiente
            return temp
    

    #MOSTRAR  EL PRIMER CLIENTE EN LA COLA
    def primeroencola(self):
        if self.primero == None:
            print("No hay ningun cliente en la cola")
        else:
            return self.primero


    #IMPRIMIR LA COLA DE CLIENTES
    def imprimirCola(self):
        print("----------------------------------")
        print("     LA COLA DE CLIENTES ES          ")
        print("----------------------------------")
        tmp=self.primero
        while tmp is not None:
            print("dpi: ",tmp.dpi, '||' ,' Nombre: ',tmp.nombre, '||' ,' Transacciones a realizar por cliente: ', '||' ,tmp.transacciones)
            tmp=tmp.siguiente