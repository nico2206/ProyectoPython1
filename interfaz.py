import json 
from pathlib import Path

def cargar (arch):
    arch = Path(arch)
    base = {"Grupos":{}, "Modulos":{}, "Estudiantes":{}, "Docentes":{}}
    if arch.is_file():
        try:
            if arch.stat().st_size == 0:
                print("El archivo está vacío, creando con datos vacíos.")
            else:
                with open(arch, "r") as fd:
                    base = json.load(fd)
        except json.JSONDecodeError:
            print("Error de formato. Creando con datos vacíos")
        except Exception as e:
            print("Error al abrir el archvio: ", e)
    else:
        print("El archivo no existe, creando uno nuevo...")
    with open (arch, "w")as fd:
      json.dump(base, fd, indent=4)
    return base 

def grupos():
    archivo = "base.json"
    funcion = cargar(archivo)
    sw = True
    while sw:
     codigo1 = (input("Ingrese el codigo del grupo con maximo 5 caracteres\n"))
     if codigo1 in funcion["Grupos"]:
         print("El codigo ya esta registrado")
         print("Registre un nuevo codigo")
     elif len(codigo1) > 1 and len(codigo1)<= 5:
        print("El codigo es valido")
        sw = False
     elif len(codigo1) > 6:
        print ("El codigo no es valido")
        print("Escribe de nuevo el codigo")
     else:
         print("El codigo es incorrecto") 
    nombre1 = (input("ingrese el nombre del grupo \n")).capitalize()
    sigla1 = input("ingrese las siglas del grupo \n")
    grupo = {"codigo": codigo1, "nombre":nombre1,"sigla":sigla1}
    funcion ["Grupos"][codigo1] = grupo
    with open("base.json", "w") as fd:
        json.dump(funcion, fd, indent=4)
    print("El grupo a sido registrado correctamente")

def modulos():
    archivo = "base.json"
    DATOS = cargar(archivo)
    sw = True
    while sw:
     modulo1 = (input("Ingrese el codigo del modulo con maximo 5 caracteres\n"))
     if modulo1 in DATOS["Modulos"]:
         print("El codigo ya esta registrado")
         print("Registre un nuevo codigo")
     elif len(modulo1) > 1 and len(modulo1)<= 5:
        print("El codigo es valido")
        sw = False
     elif len(modulo1) > 6:
        print ("El codigo no es valido")
        print("Escribe de nuevo el codigo")
     else:
         print("El codigo es incorrecto")
    nombre1 = input("Ingrese el nombre del modulo\n")
    tiempo1 = input("Ingrese duracion del modulo en semanas\n")
    modulos = {"Modulos":modulo1, "nombre": nombre1, "tiempo": tiempo1}
    DATOS ["Modulos"][modulo1]= modulos
    with open(archivo, "w") as fd:
        json.dump(DATOS, fd, indent=4)

def estudiantes():
    archivo = "base.json"
    DATOS = cargar(archivo)
    codigoEstuadiantes = input("Ingrese el codigo del estudiante \n")
    nombre2 = input("Ingrese el nombre del estudiante\n")
    sexo1 = input("Ingresa el sexo del estudiante\n")
    edad1 = input ("Ingrese la edad del estudiante\n")
    estudiantes = {"codigo":codigoEstuadiantes, "nombre": nombre2, "sexo": sexo1, "edad":edad1}
    DATOS ["Estudiantes"][codigoEstuadiantes]= estudiantes
    with open(archivo, "w") as fd:
        json.dump(DATOS, fd, indent=4)

def docentes ():
    archivo = "base.json"
    DATOS = cargar(archivo)
    cedula1 = input("Ingrese tu numero de cedula \n")
    nombre1 = input("Ingresa tu nombre\n")
    docentes = {"Cedula":cedula1, "nombre": nombre1}
    DATOS ["Docentes"]= docentes
    with open(archivo, "w") as fd:
        json.dump(DATOS, fd, indent=4)

def  Asignación_de_Estudiantes():
    archivo = "base.json"
    Datos= cargar(archivo)
    estudiante_registro = input("Ingrese el codigo del estudiante")
    if estudiante_registro not in Datos["Estudiantes"]:
        print ("vuelva a menu y registre el estudiante")
        return
    print("Estos son los grupos disponibles en el momento")
    for codigo1, nombre1 in Datos["Grupos"].items():
        print (f"{codigo1}:{nombre1}" )
    grupo_registro = input("ingrese el codigo del grupo al que quieres registrar al estudiante")
    if grupo_registro not in Datos["Grupos"]:
        print("vuelva a menu y cree el grupo")
        return
    print("Estos son los modulos disponibles en el momento")
    for modulo1, nombre1 in Datos["Modulos"].items():
        print (f"{modulo1}:{nombre1}" )
    modulos_asignar= []
    while len(modulos_asignar) <= 3:
        modulo = input("ingrese el modulo")
        if modulo in Datos["Modulos"]:
            modulos_asignar.append(modulo)
            if len(modulos_asignar) == 3:
                break
        else:
            print("No existe el modulo")
    Datos["Estudiantes"][estudiante_registro]["Grupos"] = grupo_registro
    Datos["Estudiantes"][estudiante_registro]["Modulos"]= modulos_asignar
    with open(archivo, "w") as fd:
        json.dump(Datos, fd, indent=4)
    
