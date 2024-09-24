from interfaz import grupos
from interfaz import modulos
from interfaz import estudiantes
from interfaz import docentes
 
def menu():
        print("** BIENVENIDO A LA APLICACION **")
        print("1. Registro de grupos ")
        print("2. Registro de módulos ")
        print("3. Registro de estudiantes ")
        print("4. Registro de docentes")
        print("5. Registro de asistencia ")
        print("6. Consultas de información")
        print("7. Generación de informes")
        print("8. Cambio de contraseña")
        print("9. Salida del sistema")
contraseña1 = ("SISGESA")
def inicio():
   sw = True
   while sw:
       usuario = input("Ingresa tu usuario ? \n")
    
       contraseña = input("ingresa tu contraseña \n")
       if contraseña == contraseña1:
        sw = False 
        while True:
         menu()
         opccion = input("selecciona una opcion\n")
         match opccion:
            case "1":
               grupos()
            case "2":
               modulos() 
            case "3":
               estudiantes()
            case "4":
               docentes()         
       else:
         print("Usuario o contraseña son incorrectos")
inicio()
                      