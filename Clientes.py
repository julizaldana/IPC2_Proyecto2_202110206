class Cliente:
    def __init__(self,dpi,nombre,transacciones):
        self.dpi = dpi
        self.nombre = nombre
        self.transacciones = transacciones
        self.siguiente=None
