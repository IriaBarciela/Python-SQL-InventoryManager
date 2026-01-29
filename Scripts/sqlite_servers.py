import sqlite3
from servers_json import cargar_servidores

DB = "servidores.db"

def crear_db(nombre_db=DB):
    with sqlite3.connect(nombre_db) as conexion:
        conexion.execute("DROP TABLE IF EXISTS Servidores")
        conexion.execute("""
            CREATE TABLE Servidores (
                nombre text PRIMARY KEY,
                ip text,
                sistema text,
                ubicacion text,
                responsable text
            )
        """)

def insertar_servidores():
    lista = cargar_servidores()
    with sqlite3.connect(DB) as conexion:
        for servidor in lista:
            conexion.execute(
                "INSERT OR REPLACE INTO Servidores VALUES (?, ?, ?, ?, ?)",
                (servidor["nombre"], servidor["ip"], servidor["sistema"],
                 servidor["ubicacion"], servidor["responsable"])
            )

def gestionar_servidores():
    while True:
        print("1 Crear BDD | 2 Inserir Datos | 3 Consultar servidores | 4 Saír")
        opcion = input("Opción: ")
        
        if opcion == "1":
            crear_db()

        elif opcion == "2":
            insertar_servidores()

        elif opcion == "3":
            nombre = input("Nombre del servidor: ")
            with sqlite3.connect(DB) as conexion:
                resultado = conexion.execute(
                    "SELECT * FROM Servidores WHERE nombre=?", (nombre,)
                ).fetchone()

                if resultado is not None:
                    print(resultado)
                else:
                    print("Servidor no encontrado")
        
        elif opcion == "4":
            break
        
        else:
            print("Opcion no válida")

if __name__ == "__main__":
    gestionar_servidores()
