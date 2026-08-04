import random
import json
import os
ids = []
titulos = []
rutas = []
cantidad_claves = []
claves_json = []
fechas = []
estados = []
observaciones = []
#------------------------------------#
#--|menu_principal_analizador_json|--#
#------------------------------------#
while True:
    print("menu principal analizador json")
    print("1) crear análisis")
    print("2) editar análisis")
    print("3) eliminar análisis")
    print("4) buscar análisis")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #--------------------#
    #--|crear_analisis|--#
    #--------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_analisis = 1
        else:
            id_analisis = ids[-1] + 1
        titulo = input("título: ")
        ruta = input("ruta del archivo json: ")
        fecha = input("fecha: ")
        estado = input("estado (analizado o pendiente): ")
        observacion = input("observación: ")
        if os.path.exists(ruta):
            try:
                with open(ruta, "r", encoding="utf-8") as archivo:
                    datos = json.load(archivo)
                if isinstance(datos, dict):
                    claves = list(datos.keys())
                elif isinstance(datos, list):
                    claves = []
                    for elemento in datos:
                        if isinstance(elemento, dict):
                            for clave in elemento.keys():
                                if clave not in claves:
                                    claves.append(clave)
                else:
                    claves = []
                resultado = ""
                for clave in claves:
                    resultado += clave + " "
                ids.append(id_analisis)
                titulos.append(titulo)
                rutas.append(ruta)
                cantidad_claves.append(len(claves))
                claves_json.append(resultado)
                fechas.append(fecha)
                estados.append(estado)
                observaciones.append(observacion)
                print("archivo analizado correctamente.")
                print("id:", id_analisis)
            except:
                print("el archivo no contiene un json válido.")
        else:
            print("el archivo no existe.")
    #---------------------#
    #--|editar_analisis|--#
    #---------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("editar análisis")
            for i in range(len(ids)):
                print(f"{ids[i]} | {titulos[i]} | {cantidad_claves[i]} claves | {estados[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {titulos[posicion]} | {rutas[posicion]}")
                nuevo_titulo = input("nuevo título: ")
                nueva_ruta = input("nueva ruta del archivo json: ")
                nueva_fecha = input("nueva fecha: ")
                nuevo_estado = input("nuevo estado: ")
                nueva_observacion = input("nueva observación: ")
                if os.path.exists(nueva_ruta):
                    try:
                        with open(nueva_ruta, "r", encoding="utf-8") as archivo:
                            datos = json.load(archivo)
                        if isinstance(datos, dict):
                            claves = list(datos.keys())
                        elif isinstance(datos, list):
                            claves = []
                            for elemento in datos:
                                if isinstance(elemento, dict):
                                    for clave in elemento.keys():
                                        if clave not in claves:
                                            claves.append(clave)
                        else:
                            claves = []
                        resultado = ""
                        for clave in claves:
                            resultado += clave + " "
                        titulos[posicion] = nuevo_titulo
                        rutas[posicion] = nueva_ruta
                        cantidad_claves[posicion] = len(claves)
                        claves_json[posicion] = resultado
                        fechas[posicion] = nueva_fecha
                        estados[posicion] = nuevo_estado
                        observaciones[posicion] = nueva_observacion
                        print("registro actualizado correctamente.")
                    except:
                        print("el archivo no contiene un json válido.")
                else:
                    print("el archivo no existe.")
            else:
                print("id no encontrada.")
    #-----------------------#
    #--|eliminar_analisis|--#
    #-----------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("eliminar análisis")
            for i in range(len(ids)):
                print(f"{ids[i]} | {titulos[i]} | {cantidad_claves[i]} claves | {estados[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {titulos[posicion]} | {rutas[posicion]}")
                respuesta = input("¿desea eliminar este registro? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    titulos.pop(posicion)
                    rutas.pop(posicion)
                    cantidad_claves.pop(posicion)
                    claves_json.pop(posicion)
                    fechas.pop(posicion)
                    estados.pop(posicion)
                    observaciones.pop(posicion)
                    print("registro eliminado correctamente.")
                else:
                    print("el registro no fue eliminado.")
            else:
                print("id no encontrada.")
    #---------------------#
    #--|buscar_analisis|--#
    #---------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("buscar análisis")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("id:", ids[posicion])
                print("título:", titulos[posicion])
                print("ruta:", rutas[posicion])
                print("cantidad de claves:", cantidad_claves[posicion])
                print("claves encontradas:")
                print(claves_json[posicion])
                print("fecha:", fechas[posicion])
                print("estado:", estados[posicion])
                print("observación:", observaciones[posicion])
            else:
                print("id no encontrada.")
    #-----------------#
    #--|lista_datos|--#
    #-----------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            analizados = 0
            pendientes = 0
            total_claves = 0
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {titulos[i]} | {cantidad_claves[i]} claves | {estados[i]}")
                total_claves += cantidad_claves[i]
                if estados[i].lower() == "analizado":
                    analizados += 1
                elif estados[i].lower() == "pendiente":
                    pendientes += 1
            promedio = total_claves / len(ids)
            print("estadísticas analizador json")
            print("cantidad de archivos:", len(ids))
            print("archivos analizados:", analizados)
            print("archivos pendientes:", pendientes)
            print("total de claves analizadas:", total_claves)
            print("promedio de claves por archivo:", round(promedio, 2))
            posicion = random.randint(0, len(ids) - 1)
            print("archivo seleccionado")
            print("título:", titulos[posicion])
            print("ruta:", rutas[posicion])
            print("cantidad de claves:", cantidad_claves[posicion])
            print("claves:")
            print(claves_json[posicion])
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el analizador json.")
        break
    else:
        print("opción no válida.")