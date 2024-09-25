import json 
from pathlib import Path
import hashlib
def cargar_usuario (arch):
    arch = Path(arch)
    usuario1 = {"Usuariocontra":{}}
    if arch.is_file():
        try:
            if arch.stat().st_size == 0:
                print("El archivo está vacío, creando con datos vacíos.")
            else:
                with open(arch, "r") as fd:
                    usuario1 = json.load(fd)
        except json.JSONDecodeError:
            print("Error de formato. Creando con datos vacíos")
        except Exception as e:
            print("Error al abrir el archvio: ", e)
    else:
        print("El archivo no existe, creando uno nuevo...")
    with open (arch, "w")as fd:
      json.dump(usuario1, fd, indent=4)
    return usuario1 
def encriptar_contraseña(contraseña):
    return hashlib.sha256(contraseña.encode()).hexdigest()
def cambio_usuario():
    archivo = "usuario1.json"
    datos = cargar_usuario(archivo)
    sw = True
    while sw:
      Usuario = input("        INGRESE UN USUSARIO \n")
      Contraseña_base = input("        INGRESE CONTRASEÑA \n ")
      contraseña_encriptada = encriptar_contraseña(Contraseña_base)
      if Contraseña_base=="SISGESA":
          sw= False
          inicio_sec = {"usuario_dig": Usuario, "contraseña_dig":contraseña_encriptada}
          datos["Usuariocontra"] =inicio_sec
      else:
          print("Digite nuevamente su usuario y contraseña")  
    with open(archivo, "w") as fd:
        json.dump(datos, fd, indent=4)

def clear():
    print("\n"*100)

    
