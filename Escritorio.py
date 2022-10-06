class Escritorio:
    def __init__(self,id,identificacion,encargado):
        self.id=id
        self.identificacion=identificacion
        self.encargado=encargado
        self.estado = False
        self.ocupado = False
        self.anterior=None
        self.siguiente=None
