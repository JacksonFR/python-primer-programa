Alumnos = {}
def sistem():
    print("1.-Agregar Alumno")
    print("2.-Eliminar")
    print("3.-Modificaciones")
    print("4.-Mostrar arreglos")
    print("5.-Buscar Alumno")
    print("6.-Salir")
def agregar():

    x = input("Nombres de los alumnos: ")
    y = int(input("Calificacion del alumno: "))
    Alumnos[x]=y

def eliminar():
    #print("Eliminar: ")
    e = intput("Nombre del alumno: ")
    alumnos.pop(e)

def modificar():
    print("Modificar:")
    x = input("Nombres del alumno: ")
    y = int(input("Calificacion del alumno: "))
    Alumnos[x]=y
def mostrar():
    print(Alumnos)
def buscar():
    x = input("Nombres del alumno: ")
    if x in Alumnos:
        print(x,Alumnos[x])
    else:
        print("No existe")
def salir():
    exit()
def ejecutar(option):
    if (option == 1):
        agregar()
    if (option == 2):
        eliminar()
    if (option == 3):
        modificar()
    if (option == 4):
        mostrar()
    if (option == 5):
        buscar()
    if (option == 6):
        salir()
    sistem()
    a=int(input("Dame una opción"))
    ejecutar(a)

sistem()
a = int(input("Dame una opción"))
ejecutar(a)




