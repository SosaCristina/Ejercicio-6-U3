from ClaseVehiculo import Vehiculo
class Nuevo(Vehiculo):
    marca="Fiat"
    __version=""

    def __init__(self, modelo, puertas, color, preciobase,version):
        super().__init__(modelo, puertas, color, preciobase)
        self.__version=version

    def getPuertas(self):
        return super().getPuertas()
    def getPrecioBase(self):
        return super().getPrecioBase()
    def getModelo(self):
        return super().getModelo()
    def getColor(self):
        return super().getColor()

    def CalcPrecioVenta(self):
        total=0
        gastos=0.10*self.getPrecioBase()
        if(self.__version.lower()=='full'):
            full=0.02*self.getPrecioBase()
            total=self.getPrecioBase()+gastos+full
        else:
            total=self.getPrecioBase()+gastos
        return total

    def toJson(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                modelo=self.getModelo(),
                puertas=self.getPuertas(),
                color=self.getColor(),
                preciobase=self.getPrecioBase(),
                version=self.__version
            )
        )
        return d
    
    def __str__(self):
        super().__str__()
        print('Version: {}'.format(self.__version))
        return ""