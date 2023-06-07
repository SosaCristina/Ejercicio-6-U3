from ClaseVehiculo import Vehiculo
import datetime

class Usado(Vehiculo):
    __marca=""
    __patente=""
    __año=""
    __kilometraje=0

    def __init__(self, modelo, puertas, color, preciobase,marca,patente,año,kilometraje):
        super().__init__(modelo, puertas, color, preciobase)
        self.__marca=marca
        self.__patente=patente
        self.__año=año
        self.__kilometraje=kilometraje
    def getPatente(self):
        return self.__patente

    def getPuertas(self):
        return super().getPuertas()
    def getPrecioBase(self):
        return super().getPrecioBase()
    def getModelo(self):
        return super().getModelo()
    def getColor(self):
        return super().getColor()

    def toJson(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                modelo=self.getModelo(),
                puertas=self.getPuertas(),
                color=self.getColor(),
                preciobase=self.getPrecioBase(),
                marca=self.__marca,
                patente=self.__patente,
                año=self.__año,
                kilometraje=self.__kilometraje
            )
        )
        return d

    def CalcPrecioVenta(self):
        km=0
        antig=int(datetime.date.today().year) - int(self.__año)
        porc=float((super().getPrecioBase() * 1)/100)
        if(int(self.__kilometraje)>100000):
            km=float((super().getPrecioBase() * 2)/100)
        total=float(super().getPrecioBase())-porc-antig-km
        return total
    def __str__(self):
        super().__str__()
        print('Marca: {}'.format(self.__marca))
        print('Patente: {}'.format(self.__patente))
        print('Año: {}'.format(self.__año))
        print('Kilometros: {}'.format(self.__kilometraje))
        return ""