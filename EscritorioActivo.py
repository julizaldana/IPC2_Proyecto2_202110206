class EscritorioActivo:
    def __init__(self,id):
        self.id=id
        self.estado = False
        self.ocupado = False
        self.anterior=None
        self.siguiente=None
