# Python-SQL-InventoryManager

Un sistema modular diseñado para la **limpieza, validación y migración de datos** de servidores, integrando archivos planos (TXT), estructuras de intercambio (JSON) y bases de datos relacionales (SQLite).

---

## Descripción del Proyecto
El objetivo principal es transformar un archivo de inventario "sucio" (`inventario.txt`) con formatos inconsistentes y errores manuales, en una base de datos SQL robusta y segura.



### El flujo de trabajo se divide en 3 fases:
1.  **Limpieza (Python):** Lectura del TXT y normalización de separadores, mayúsculas y espacios.
2.  **Validación:** Filtrado de líneas corruptas y validación técnica de formatos IPv4 y sistemas operativos permitidos.
3.  **Persistencia (SQL):** Exportación a JSON y carga masiva en SQLite utilizando sentencias preparadas para prevenir ataques de **SQL Injection**.

---

## Estructura del Repositorio
* `inventario.py`: Lógica principal de limpieza y validación (Módulo base).
* `servers_json.py`: Módulo de exportación e importación de formato JSON.
* `sqlite_servers.py`: Interfaz de usuario, gestión de base de datos y consultas SQL.
* `inventario.txt`: Archivo origen con los datos de los servidores.
