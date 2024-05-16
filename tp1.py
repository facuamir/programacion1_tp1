
def agregar_empleado(nombre, apellido, edad, puesto, dni, salario, fecha_ingreso, legajo):
    return {'Nombre': nombre, 'Apellido': apellido, 'Edad': edad, 'Puesto': puesto, 'Dni': dni, 'Salario': salario, 'Fecha de ingreso': fecha_ingreso, 'Legajo': legajo}

lista_empleados = []

def alta_empleados():
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    edad = int(input("Ingrese edad: "))
    puesto = input("Ingrese puesto: ")
    dni = int(input("Ingrese DNI: "))
    salario = float(input("Ingrese salario: "))
    fecha_ingreso = input("Ingrese fecha de ingreso: ")
    legajo = int(input("Ingrese legajo: "))

    empleado = agregar_empleado(nombre, apellido, edad, puesto, dni, salario, fecha_ingreso, legajo)
    lista_empleados.append(empleado)
    return lista_empleados

def baja_legajo():
    legajo = int(input("Ingrese el legajo del empleado a eliminar: "))
    
    empleado_encontrado = False
    for empleado in lista_empleados:
        if empleado["Legajo"] == legajo:
            lista_empleados.remove(empleado)
            empleado_encontrado = True
            print("Empleado eliminado.")
            break
    
    if not empleado_encontrado:
        print("No se encontró un empleado con ese legajo.")
        
def modificar_datos():
    dni = int(input("Ingrese el DNI del empleado a modificar: "))
    empleado_encontrado = False
    
    for empleado in lista_empleados:
        if empleado["Dni"] == dni:
            empleado_encontrado = True
            
            nombre = input("Ingrese el nuevo nombre del empleado: ")
            if nombre:
                empleado["Nombre"] = nombre
            
            apellido = input("Ingrese el nuevo apellido del empleado: ")
            if apellido:
                empleado["Apellido"] = apellido
            
            edad = input("Ingrese la nueva edad del empleado: ")
            if edad:
                empleado["Edad"] = int(edad)
            
            puesto = input("Ingrese el nuevo puesto del empleado: ")
            if puesto:
                empleado["Puesto"] = puesto
            
            print("Datos del empleado modificados.")
            break
    
    if not empleado_encontrado:
        print("No se encontró un empleado con ese DNI.")


def buscar_empleado():
    nombre = input("Ingrese el nombre del empleado a buscar: ")
    for empleado in lista_empleados:
        if empleado["Nombre"] == nombre:
            print(empleado)
            return
    print("No se encontró un empleado con ese nombre.")

def filtrar_edad():
    min_edad = int(input("Ingrese la edad mínima: "))
    max_edad = int(input("Ingrese la edad máxima: "))
    for empleado in lista_empleados:
        if min_edad <= empleado["Edad"] <= max_edad:
            print(empleado)
        

def filtrar_empleados_puesto():
    puesto = input("Ingrese el puesto para filtrar: ")
    for empleado in lista_empleados:
        if empleado["Puesto"] == puesto:
            print(empleado)

def obtener_nombre(empleado):
    return empleado["Nombre"]

def ordenar_empleados_nombre():
    lista_empleados.sort(key=obtener_nombre)
    for empleado in lista_empleados:
        print(empleado)

def contar_empleados_edad():
    min_edad = int(input("Ingrese la edad mínima: "))
    max_edad = int(input("Ingrese la edad máxima: "))
    contador = 0
    for empleado in lista_empleados:
        if min_edad <= empleado["Edad"] <= max_edad:
            contador += 1
    print(f"Hay {contador} empleados entre las edades de {min_edad} y {max_edad}.")

def promedio_edad_empleados():
    suma_edades = 0
    for empleado in lista_empleados:
        suma_edades += empleado["Edad"]
    promedio = suma_edades / len(lista_empleados)
    print(f"El promedio de edad de los empleados es {promedio}.")
    
def menu():
    while True:
        print("\n[1] Alta de empleado")
        print("[2] Baja de empleado")
        print("[3] Modificar datos de empleado")
        print("[4] Buscar empleado")
        print("[5] Filtro de Empleados por Edad")
        print("[6] Filtro de Empleados por Puesto")
        print("[7] Ordenar Empleados por Nombre")
        print("[8] Contar Empleados por Edad")
        print("[9] Calcular Promedio de Edad de los Empleados")
        print("[0] Salir")
        opcion = input("Elige una opción: ")
        match opcion:
            case '1':
                alta_empleados()
            case '2':
                baja_legajo()
            case '3':
                modificar_datos()
            case '4':
                buscar_empleado()
            case '5':
                filtrar_edad()
            case '6':
                filtrar_empleados_puesto()
            case '7':
                ordenar_empleados_nombre()
            case '8':
                contar_empleados_edad()
            case '9':
                promedio_edad_empleados()
            case '0':
                print("Saliendo ")
                return
            case _:
                print("invalida.")
menu()