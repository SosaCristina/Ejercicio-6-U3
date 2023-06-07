import json
from pathlib import Path
from ClaseVehiculo import Vehiculo

from ClaseUsado import Usado
from ClaseNuevo import Nuevo
from ClaseLista import ListaVehiculo

class ObjectEnconder(object):
 def GuardarArchivo(self,dic,archivo):
    with Path(archivo).open("w",encoding="UTF-8")as destino:
        json.dump(dic,destino,indent=4)
        destino.close()
 def LeerArchivo(self,archivo):
    with Path(archivo).open(encoding="UTF-8")as fuente:
        dic=json.load(fuente)
        fuente.close()
        return dic
 def DecodificarDiccionario(self,dic):
    if '__class__' not in dic:
        return dic
    else:
        class_name=dic['__class__']
        class_=eval(class_name)
        if(class_name=='ListaVehiculo'):
            vehiculos=dic['vehiculo']
            lista=class_()
            for i in range(len(vehiculos)):
                dVehiculo=vehiculos[i]
                class_name=dVehiculo.pop('__class__')
                class_=eval(class_name)
                atributos=dVehiculo['__atributos__']
                unVehiculo=class_(**atributos)
                lista.AgregarVehiculo(unVehiculo)
        return lista