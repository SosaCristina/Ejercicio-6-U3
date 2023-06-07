from ClaseMenu import Menu
from ClaseUsado import Usado
from ClaseNuevo import Nuevo
from ClaseDecodificador import ObjectEnconder
from ClaseLista import ListaVehiculo
import os

if __name__ == "__main__":
    vehiculos=ListaVehiculo()
    Json=ObjectEnconder()
    Diccionario=Json.LeerArchivo('C:/Users/Alumno/Desktop/POO/unidad 3 poo/ejemplo/vehiculos.json')
    vehiculos=Json.DecodificarDiccionario(Diccionario)
    menu=Menu()
    ban=False
    while not ban:
        os.system('cls')
        print("1. Insertar vehiculo")
        print("2. Agregar vehiculo")
        print("3. Mostrar tipo de objeto")
        print("4. Modificar precio base")
        print("5. Mostrar datos de vehiculo mas economico")
        print("6. Mostrar datos de todos los vehiculos")
        print("7. Guardar archivo")
        print("0. Salir")
        op=int(input("Ingrese su opcion."))
        menu.opcion(op,vehiculos)
        ban= op == 0