from interfaz import grupos
from interfaz import modulos
from interfaz import estudiantes
from interfaz import docentes
from interfaz import Asignación_de_Estudiantes
from usuario import cambio_usuario
from usuario import clear 
 
def menu():
        print("        _______________________________________________________")
        print("        |        **BIENVENIDO A LA APLICACION **               |")
        print("        |   1. Registro de grupos                              |")
        print("        |   2. Registro de módulos                             |")
        print("        |   3. Registro de estudiantes                         |")
        print("        |   4. Asignación de Estudiantes a Grupos y Módulos    |")
        print("        |   5. Registro de docentes                            |")
        print("        |   6. Registro de asistencia                          |")
        print("        |   7. Consultas de información                        |")
        print("        |   8. Cambio de contraseña                            |")
        print("        |   9 . Salida del sistema                             |")
        print("        --------------------------------------------------------                                      ")
def inicio():
   sw = True
   while sw:
        cambio_usuario()
        clear()
        sw = False 
        while True:
         menu()
         opccion = input("Selecciona una opcion\n")
         match opccion:
            case "1":
               clear()
               grupos()
            case "2":
               clear()
               modulos() 
            case "3":
               clear()
               estudiantes()
            case "4":
               clear()
               Asignación_de_Estudiantes()
            case "5":
               clear()
               docentes()  
            case "6":
                pass
                           
       #else:
         #print("Usuario o contraseña son incorrectos")
inicio()
                      