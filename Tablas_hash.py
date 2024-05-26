import csv
from os import system

class Nodo:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.siguiente = None

class TablaHash:
    def __init__(self, tamaño=10):
        self.tabla = [None] * tamaño
        self.tamaño = tamaño

    def funcion_hash(self, clave):
        return hash(clave) % self.tamaño

    def insertar(self, clave, valor):
        indice = self.funcion_hash(clave)
        nuevo_nodo = Nodo(clave, valor)
        if self.tabla[indice] is None:
            self.tabla[indice] = nuevo_nodo
        else:
            actual = self.tabla[indice]
            while actual:
                if actual.clave == clave:
                    actual.valor = valor  # Actualizar valor existente
                    return
                if actual.siguiente is None:
                    break
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo  # Añadir nuevo nodo si no se encontró la clave

    def buscar_por_clave(self, clave):
        system("cls")
        indice = self.funcion_hash(clave)
        actual = self.tabla[indice]
        while actual:
            if actual.clave == clave:
                return f"{actual.valor}-{hash(actual.clave)}"
            actual = actual.siguiente
        return None

    def buscar_por_valor(self, valor):
        system("cls")
        for indice in range(self.tamaño):
            actual = self.tabla[indice]
            while actual:
                if actual.valor == valor:
                    return f"{actual.clave}-{hash(actual.clave)}"
                actual = actual.siguiente
        return None

    def mostrar_tabla(self):
        system("cls")
        for i, nodo in enumerate(self.tabla):
            actual = nodo
            print(f"Índice {i}: ", end="")
            while actual:
                print(f"({actual.clave}, {actual.valor}) -> ", end="")
                actual = actual.siguiente
            print("None")
        system("pause")
        system("cls")

    def cargar_desde_csv(self, archivo_csv):
        with open(archivo_csv, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for fila in reader:
                clave, valor = fila
                self.insertar(clave, valor)

def menu():#creo un proceso menu, para modificar facilmente el menu y como se imprime enconsola
    print("__________________Menu__________________")
    print("1. Insertar valores manualmente")
    print("2. Insertar valores del archivo .csv")
    print("3. Visualizar tabla")
    print("4. Buscar por clave")
    print("5. Buscar por valor")
    print("6. Salir.")

# Ejemplo de uso
tabla = TablaHash()
while True:
    menu()
    try:
        opc = int(input("Ingrese una opcion: "))
        system("cls")
    except ValueError as e:
        print("Error: Porfavor ingrese un valor valido: ")#imprimo que hubo un error 
        print(f"Error: {e}")#imprimo el error
    if(opc == 1):# Insertar datos manualmente
        datos = int(input("Ingrese el numero de datos que desea agregar a la tabla: "))
        for i in range(datos):
            clave = input("Ingrese la clave: ")
            valor = input("Ingrese el valor: ")
            tabla.insertar(clave, valor)
    elif(opc == 2):# Cargar datos desde un archivo CSV
        try:
            archivo_csv = input("Ingrese el nombre del archivo ej(archivo.csv): ")  # Asegúrate de tener un archivo CSV llamado 'datos.csv' con datos clave,valor
            tabla.cargar_desde_csv(archivo_csv)
        except FileExistsError as e:
            print(f"Error: {e}")
    elif(opc == 3):# Mostrar tabla hash
        print("Tabla Hash: ")
        tabla.mostrar_tabla()
    elif(opc == 4):# Buscar por clave
        clave = input("Introduce la clave que deseas buscar: ")
        print(tabla.buscar_por_clave(clave))  # Salida: valor2
    elif(opc == 5):# Buscar por valor
        valor = input("Introduce el valor que deseas buscar: ")
        print(tabla.buscar_por_valor(valor))  # Salida: clave3
    elif(opc == 6):
        break;
    else:#uso este else, sino introduce ningun valor anterior mencionado entonces
        system("cls")#limpio la consola para comenzar a pedir el valor a ingresar
        print("Opcion invalida, porfavor ingrese una opcion del menu")#imprimo un mensaje de opcion invalida, introdusca un valor valido
