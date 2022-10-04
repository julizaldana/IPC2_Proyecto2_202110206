class PuntoAtencion:
    def __init__(self,id,nombre,direccion):
        self.id=id
        self.nombre=nombre
        self.direccion=direccion
        self.anterior=None
        self.siguiente=None
