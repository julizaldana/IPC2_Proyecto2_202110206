class Transaccion:
    def __init__(self,id,nombre,tiempoAtencion):
        self.id=id
        self.nombre=nombre
        self.tiempoAtencion=tiempoAtencion
        self.anterior=None
        self.siguiente=None
