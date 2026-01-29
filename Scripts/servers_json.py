import json
from inventario import procesar_inventario


JSON_FILE = "lista_servidores.json"


def guardar_servidores(fichero="inventario.txt"):
    servidores, errores = procesar_inventario(fichero)

    with open(JSON_FILE, "w", encoding="utf-8") as j:

        json.dump(servidores, j)
    return servidores


def leer_servidores():
    with open(JSON_FILE, "r", encoding="utf-8") as j:
        return json.load(j)


def cargar_servidores(fichero="inventario.txt"):
    guardar_servidores(fichero)
    return leer_servidores()


#PRUEBA
if __name__ == '__main__':
    servidores = cargar_servidores("inventario.txt")
    
    print("Servidores:")
    for servidor in servidores:
        print(servidor)

