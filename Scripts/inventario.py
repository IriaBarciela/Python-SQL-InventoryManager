def leer_fichero(ruta_fichero):
    with open(ruta_fichero, "r", encoding='utf-8') as fich:
        lista_lineas = []
        linea = fich.readline()
        while(linea):
            lista_lineas.append(linea)
            linea = fich.readline()
    
    return lista_lineas

def normalizar_linea(linea: str):
    """Pasa cada fragmento  de la línea a un diccionario
    efectuando las normalizaciones necesarias sobre los datos (en enunciado)"""
    #Unificamos separadores, sustituyendo ; por ,
    linea = linea.replace(";", ",")
    #Rompemos en trozos usando el separador , ya unificado
    #Otro type hint: lista de strings
    lista_datos: list[str] = linea.split(",")
    #Elimino espacios sobrantes al principio o al final de cada dato
    lista_datos = [dato.strip() for dato in lista_datos]
    
    #Queremos 5 datos en cada línea. Si alguno no está, se sustituye por ""
    #Lo hago con "list comprehesion", pero se puede hacer con un for normal
    lista_datos = [lista_datos[i] if i < len(lista_datos) else '' for i in range(5)]
    
    #Creo el diccionario que voy a devolver
    dic_servidor = {
        'nombre': lista_datos[0],
        'ip': lista_datos[1],
        'sistema': lista_datos[2].lower(),
        'ubicacion': lista_datos[3],
        'responsable': lista_datos[4].capitalize()
    }
    
    return dic_servidor
    
def ip_valida(ip: str):
    lista_octetos = ip.split(".")
    
    if len(lista_octetos) != 4: 
        return False
    
    #Validamos que cada octeto esté en el rango [0,255]
    for octeto in lista_octetos:
        try: # protejo el casting a int(). No hay casos en el fichero de ejemplo
            valor = int(octeto)
        except ValueError:  
            return False
        if not 0 <= valor <= 255:
            return False
    
    return True



def ip_valida_v2(ip):
    """Versión usando el módulo ipaddress"""
    import ipaddress
    #El constructor IPV4Address(ip) genera una excepcion si la ip no es correcta
    try:
        ipaddress.IPv4Address(ip)
        return True
    except:
        return False

def validar_datos(dic_linea: dict[str,str]):
    if dic_linea['nombre'] == '':
        return False, "ERROR_NOMBRE_INVALIDO"
    if not ip_valida(dic_linea['ip']):
        return False, 'ERROR_IP_INVALIDA'
    if not dic_linea['sistema'] in ['linux','windows','macos']:
        return False, 'ERROR_SISTEMA_INVALIDO'
    
    dato_vacio = ['', '-']
    if dic_linea['ubicacion'] in dato_vacio:
        dic_linea['ubicacion'] = None
    if dic_linea['responsable']in dato_vacio:
        dic_linea['ubicacion'] = None
    
    return True, dic_linea
    


def obviar_linea(linea: str):
    """Función auxiliar
    Devuelve TRUE si la línea no tiene contenido a procesar.
    Es decir: si empieza por #, está vacía, o sólo contiene espacios"""
    return linea.startswith("#") or linea == "" or linea.isspace()
        
def escribir_informe(ruta_salida, lista_dic_servidores, lista_errores):
    with open(ruta_salida, "w", encoding='utf-8') as fich_informe:
        fich_informe.write(f"Número de servidores válidos: {len(lista_dic_servidores)}\n")
        fich_informe.write(f"Número de líneas descartadas (con errores): {len(lista_errores)}\n")
        
        #Formo un conjunto con las ips del diccionario. Usando set comprehesion (se puede hacer con un for normal)
        set_ips = {servidor['ip'] for servidor in lista_dic_servidores}
        fich_informe.write(f"Lista de IPs únicas: {', '.join(set_ips)}\n")
        
        #Hago lo propio con los responsables, para mostrar cuantos son
        set_responsables = {servidor['responsable'] for servidor in lista_dic_servidores}
        fich_informe.write(f"Responsables distintos: {len(set_responsables)}\n")
        

def procesar_inventario(ruta_fichero):
    lista_lineas = leer_fichero(ruta_fichero)
    
    

    
    #Creamos la lista que contendrá los diccionarios con datos válidos
    lista_dic_lineas = []
    #Creo la lista de errores
    lista_errores = []
    for linea in lista_lineas:
        #Obviamos las líneas de comentarios o vacías
        if not obviar_linea(linea):
            #Normalizamos, y si lo datos son válidos, los recogemos en la lista
            dic_linea = normalizar_linea(linea)
            #print("Linea ", dic_linea)
            valido, info = validar_datos(dic_linea)
            if valido:
                lista_dic_lineas.append(info)
            else:
                #En mi caso, veo la lista de errores como una lista de tuplas:  (línea errónea, mensaje de error)
                lista_errores.append((linea, info))
    
    escribir_informe("informe_servidores.txt", lista_dic_lineas, lista_errores)
    return lista_dic_lineas, lista_errores 

#PRUEBAS
if __name__ == '__main__':
    #hay que comprobar visualmente el fichero informe_servidores.txt
    lista_servers, lista_errores = procesar_inventario("inventario.txt")


    print("Lista de servidores")
    for servidor in lista_servers:
        print(servidor)

    print("\nLista Errores")
    for error in lista_errores:
        print(error)

            
            
