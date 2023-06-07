from ClaseUsado import Usado
from ClaseNuevo import Nuevo
from ClaseDecodificador import ObjectEnconder
class Menu:
    __switcher = None
    def  __init__ ( self ): 
        self.__switcher  = { 
            1: self.opcion1 ,
            2: self. opcion2,
            3: self.opcion3,
            4: self.opcion4,
            5: self.opcion5,
            6: self.opcion6,
            7: self.opcion7,
            0: self.salir
        }
    def  getSwitcher ( self ):
        return self. __switcher
    def  opcion ( self , op , vehiculos ):
        func = self . __switcher . get ( op , lambda:print ( "Opción no válida" ))
        func ( vehiculos )
    def salir ( self,vehiculos):
        
        print ( 'Cerrando sistema...' )
        
    def opcion1(self,vehiculos):
        posicion=input("Ingrese la posicion a insertar: (Distinto de 0)")
        try:
            posicion=int(posicion)
            vehiculo=input("Usado(U) o Nuevo(N) --> ")
            if (vehiculo=='u'):
                modelo=input("Modelo: ")
                puertas=int(input("Cantidad de puertas. "))
                col=input("Color: ")
                base=int(input("Precio base: "))
                marca=input("Marca: ")
                pat=input("Patente: ")
                año=int(input("Año: "))
                km=int(input("Kilometraje: "))
                vehic=Usado(modelo,puertas,col,base,marca,pat,año,km)
                vehiculos.InsertarVehiculo(posicion-1,vehic)
            if (vehiculo=='n'):
                modelo=input("Modelo: ")
                puertas=int(input("Cantidad de puertas. "))
                col=input("Color: ")
                base=int(input("Precio base: "))
                version=input("Version: ")
                ve=Nuevo(modelo,puertas,col,base,version)
                vehiculos.InsertarVehiculo(posicion-1,ve)
        except ValueError:
            print("Debe ingresar un numero entero...")
            

    def opcion2(self, vehiculos):
       
        vehiculo=input("Usado(U) o Nuevo(N) --> ")
        if (vehiculo=='u'):
            modelo=input("Modelo: ")
            puertas=int(input("Cantidad de puertas. "))
            col=input("Color: ")
            base=int(input("Precio base: "))
            marca=input("Marca: ")
            pat=input("Patente: ")
            año=int(input("Año: "))
            km=int(input("Kilometraje: "))
            vehic=Usado(modelo,puertas,col,base,marca,pat,año,km)
            vehiculos.AgregarVehiculo(vehic)
        if (vehiculo=='n'):
            modelo=input("Modelo: ")
            puertas=int(input("Cantidad de puertas. "))
            col=input("Color: ")
            base=int(input("Precio base: "))
            version=input("Version: ")
            vehic=Nuevo(modelo,puertas,col,base,version)
            vehiculos.AgregarVehiculo(vehic)

    def opcion3(self,vehiculos):
        
        pos=input("Posicion: ")
        try:
            pos=int(pos)
            vehi=vehiculos.MostrarVehiculo(pos-1)
            if(vehi!=None):
                print("{}".format(vehi))
                
        except ValueError:
            print("Debe ingresar un numero entero...")
            

    def opcion4(self,vehiculos):
        
        pat=input('Patente ')
        vehic=vehiculos.ModificaBase(pat)
        if(vehic!=0):
            print('Precio Venta {}'.format(vehic.CalcPrecioVenta()))
            
        else:
            print('Patente incorrecta')
            

    def opcion5(self, vehiculos):
        
        ve=vehiculos.Minimo()
        print("Precio del vehiculo mas economico")
        print("$ {}".format(ve.CalcPrecioVenta()))
        print(ve)
        

    def opcion6(self, vehiculos):
        
        vehiculos.Mostrar()
        
    def opcion7(self,ve):
        
        Nuevo=ve.toJson()
        Json=ObjectEnconder()
        Json.GuardarArchivo(Nuevo,('vehiculos.json'))
        