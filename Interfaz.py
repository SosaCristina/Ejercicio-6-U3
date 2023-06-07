from zope.interface import Interface

class IColeccion(Interface):
    def InsertarVehiculo(posicion,elemento):
        pass
    def AgregarVehiculo(elemento):
        pass
    def MostrarVehiculo(posicion):
        pass