#Para clientes

class Node:
    
    def __init__(self, data=None, siguiente=None, anterior=None):
        self.data = data
        self.siguiente = siguiente
        self.anterior = anterior


class Cola:

    def __init__(self):
        self.cabeza = None
        self.ultimo = None

    #AGREGAR UN CLIENTE A LA COLA
    def encolar(self, data):
        node = Node(data)
        if self.cabeza == None:
            self.cabeza = node
            self.ultimo = self.cabeza
        else:
            self.ultimo.siguiente = node
            self.ultimo.siguiente.anterior = self.ultimo
            self.ultimo = self.ultimo.siguiente


    #QUITAR UN CLIENTE DE LA COLA (PRIMERA QUE SALE)
    def desencolar(self):
        if self.cabeza == None:
            return None
        else:
            temp = self.cabeza.data
            self.cabeza = self.cabeza.siguiente
            return temp


    #MOSTRAR  EL PRIMER CLIENTE EN LA COLA
    def primeroencola(self):
        if self.cabeza == None:
            print("No hay ningun cliente en la cola")
        else:
            return self.cabeza.data

    #VERIFICAR SI LA COLA ESTÁ VACÍA
    def ColaVacia(self):
        if self.cabeza == None:
            print("No hay ninguna cliente en la cola")
        else:
            return False


    #IMPRIMIR LA COLA DE CLIENTES
    def imprimirCola(self):
        print("----------------------------")
        print("Los clientes en la cola son:")
        print("----------------------------")
        temp=self.cabeza
        while temp != None:
            print(temp.data,end="   le sigue       ")
            temp=temp.siguiente

