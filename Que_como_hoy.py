"""
I have created a program that helps you to know what to do for lunch.
For all those people who don't want to think about what to make for lunch, here it comes: 
What do I eat today?

The user will be able to:
    -Create/remove a list of meals.
    -Add/remove meals.
    -Choose to use a pre-made list.
    -Decide what to eat today randomly.
    -Create/remove users.

The program will choose a meal from the list and show it to the user.
#----------------------------------------------------------------------------------
He creado  un programa que ayuda a saber que hacer de comer.
Para todas esas personas que no quieren pensar en qué pueden hacer de comer, llega: 
¿Qué como hoy?

El usuario podrá:
    -Crear/eliminar una lista de comidas.
    -Añadir/eliminar comidas.
    -Optar por usar una lista prefabricada.
    -Decidir que comer hoy de forma aleatoria
    -Crear/eliminar usuarios.

El programa elegirá una comida de la lista y la mostrará al usuario.

"""

#--------------------
import random as rd
import os.path as path
from os import remove
#--------------------
def comidas():
    print()
    print("Debe introducir uno por uno los comidas que quiera añadir a la tu lista '{}', al terminar ponga '0'".format(nLista))

    comida=""
    while comida!="0":
        comida=input("Inserte una comida: ").upper()
        if comida=="0":
            break

        uLista.append(comida)
    print()
""""Esta función que recoge las comidas del usuario en una lista."""

def escritura():
    archivo=open("que_como_hoy_DB_{}".format(usuario),"w")
    archivo.write("{}\n".format(usuario))
    archivo.write("{}\n".format(nLista))
    for i in uLista:
        archivo.write("{},".format(i))
    archivo.close
"""Esta función reescribe un bloc de notas para usarlo como 'base de datos' para guardar el nombre del usuario y su lista."""

#--------------------
pLista0=["1","2","3"]
pLista1=["4","5","6"]
#--------------------
control=0


# ALREADY A USER
print()
existe=path.isfile("que_como_hoy_DB")

print("Bienvenido/a a ¿Que como hoy?")
if existe==True:
    control=-1
    while control==-1:
        archivo=open("que_como_hoy_DB")

        print("-------------------------------")
        print("---- Selección de usuarios ----")
        print("-------------------------------")

        for linea in archivo:
            print("-. {}".format(linea))
        print()

        usuario=input("Elija un usuario: ")
        archivo.close

        existe= path.exists("que_como_hoy_DB_{}".format(usuario))
        if existe==True:
            archivo=open("que_como_hoy_DB_{}".format(usuario))
            usuario=archivo.readline().rstrip("\n")
            nLista= archivo.readline().rstrip("\n")
            linea3= archivo.readline().rstrip("\n")
            linea3=linea3.split(",")
            uLista=linea3
            archivo.close

            uLista.pop() #Elimino el último elemento ya que al hacer el split por ',' se añade un elemento vacio.
            control=1
        
        else:
            print("No ha introducido un usuario válido. se volverá a la selección de usuario")

else:
    print("No existen datos. Se procede a la creación de usuario")
    usuario=""
    uLista=[]


# NEW USER
while usuario=="":
    archivo=open("que_como_hoy_DB","a")
    print()
    print()

    print("Vamos a crear su usuario, por favor, introduzca lo siguiente: ")
    print()

    usuario=input("Nombre de usuario: ").capitalize()
    archivo.write("{}\n".format(usuario))
    archivo.close
    print()
    print()

    while control==0:
        archivo=open("que_como_hoy_DB_{}".format(usuario),"a")
        archivo.write("{}\n".format(usuario))
        print("{}, Para empezar a usar '¿Que como hoy?' Debe tener una lista de comidas.".format(usuario))
        print("opciones: ")
        print("    1.- Crear una lista")
        print("    2.- Usar una lista prefabricada")
        print()

        opcion=int(input("¿Que prefiere hacer?: "))
        print()

        if opcion==1: #CREA UNA LISTA
            print()

            nLista=input("Hola {}, vamos a crear tu lista de comida ¿Como se va a llamar?: ".format(usuario))
            comidas()

            archivo.write("{}\n".format(nLista))
            for i in uLista:
                archivo.write("{},".format(i))
            archivo.close

            control=1


        elif opcion==2: #USA LISTA PREFABRICADA
            print()

            print("Le mostraremos nuestras listas: ")
            print("Lista_1: ",pLista0)
            print("Lista_2: ",pLista1)
            print()

            sN=input("¿Quiere usar alguna de estas listas? (s/n): ").upper()

            if sN=="S":
                qLista=input("¿Cual le gustaría usar?: ").upper()
                print()

                if qLista=="LISTA_1":
                    uLista=pLista0
                    nLista="Lista_1"

                    archivo.write("{}\n".format(nLista))
                    for i in uLista:
                        archivo.write("{},".format(i))
                    archivo.close
                    print()

                    control=1

                elif qLista=="LISTA_2":
                    uLista=pLista1
                    nLista="Lista_2"

                    archivo.write("{}\n".format(nLista))
                    for i in uLista:
                        archivo.write("{},".format(i))
                    archivo.close
                    print()

                    control=1
                else:
                    print("No ha introducido una lista válida.")
                    print("Se volverá al principio.")
                    print()
                    
            
            elif sN=="N":
                print("Se volverá al principio.")
                print()
                print()
            else:
                print("No ha introducido un caracter válido.")
                print("Se devolverá al principio.")
                print()
                print()
        else:
            print("No ha introducido una opción válida. Se volverá al principio.")
# MAIN
while control==1:
    print("------------------------")
    print("---- Menu principal ----")
    print("------------------------")
    print()
    print("Lista de {}: {} {}".format(usuario,nLista,uLista))
    print()

    print("     1.- Crear una nueva lista.")
    print("     2.- Editar comidas.")
    print("     3.- ¿Qué como hoy?")
    print("     4.- Edición de usuarios.")
    print("                                     5.- Salir.")
    print()

    opcion= int(input("¿Qué desea hacer?: "))
    print()

    if opcion==1: #Crea nueva lista
        print("-------------------------------------")
        print("---- Creación de una nueva lista ----")
        print("-------------------------------------")
        print()
        print("Al crear una nueva lista se eliminará la actual.")
        opcion=input("¿Quiere continuar? s/n: ").upper()
        print()

        if opcion=="S":
            uLista.clear()
            nLista=input("Hola {}, vamos a crear tu lista de comida ¿Como se va a llamar?: ".format(usuario))
            comidas()

            escritura()

        elif opcion=="N":
            print("Se volverá al menu principal.")
            print()
            print()

        else:
            print("No ha introducido un caracter válido.")
            print("Se devolverá al menu principal.")
            print()
            print()

    elif opcion==2: # Edición de comida
        print("----------------------------")
        print("---- Edición de comidas ----")
        print("----------------------------")
        print()
        print("1.- Añadir comida")
        print("2.- Eliminar comida")
        print("3.- Usar una lista pre-fabricada")
        print()

        opcion=int(input("¿Qué desea hacer?: "))
        print()

        if opcion==1: # Añadir comida
            comidas()
            
            escritura()
            print()

            print("Las comidas se han añadido correctamente.")
            print("Se volverá al menú principal.")
            print()
            print()
        
        elif opcion==2: # Eliminar comida
            print("Debe introducir una por una las comidas que desee eliminar. Al terminar, introduzca '0'.")
            print()

            comida=""
            while comida!="0":
                print(nLista,":",uLista)
                print()
                eliminar=input("¿Qué comida desea eliminar?: ").upper()
                if eliminar=="0":
                    break

                uLista.remove(eliminar)

                escritura()

                print("Se ha eliminado {} con éxito.".format(eliminar))
                print()
                print()

            escritura()
        
        elif opcion==3: # Usar lista pre-fabricada

            archivo=open("que_como_hoy_DB_{}".format(usuario),"w")
            archivo.write("{}\n".format(usuario))
            print()

            print("Le mostraremos nuestras listas: ")
            print("Lista_1: ",pLista0)
            print("Lista_2: ",pLista1)
            print()

            sN=input("¿Quiere usar alguna de estas listas? (s/n): ").upper()

            if sN=="S":
                qLista=input("¿Cual le gustaría usar?: ").upper()
                print()

                if qLista=="LISTA_1":
                    uLista=pLista0
                    nLista="Lista_1"

                    archivo.write("{}\n".format(nLista))
                    for i in uLista:
                        archivo.write("{},".format(i))
                    archivo.close
                    print()

                elif qLista=="LISTA_2":
                    uLista=pLista1
                    nLista="Lista_2"

                    archivo.write("{}\n".format(nLista))
                    for i in uLista:
                        archivo.write("{},".format(i))
                    archivo.close
                    print()

                else:
                    print("No ha introducido una lista válida.")
                    print("Se volverá al principio.")
                    print()
                
                escritura()
                    
            
            elif sN=="N":
                print("Se volverá al principio.")
                print()
                print()
            else:
                print("No ha introducido un caracter válido.")
                print("Se devolverá al principio.")
                print()
                print()
            

        else:
            print("No ha introducido una opción válida.")
            print("Se volverá al menú principal.")
            print()
            print()

    elif opcion==3: # ¿Qué como hoy?
        comida= rd.choice(uLista)
        print("Hoy se come: '{}'".format(comida))

        print("Que aproveche!")
        print()

        sN=input("Desea salir de la app? s/n: ").upper()

        if sN=="S":
            print("{},gracias por usar '¿Qué como hoy?' Esperamos verle pronto!".format(usuario))
            control=2
        
        elif sN=="N":
            print("Se volverá al menú principal.")
            print()
            print()
    

    elif opcion==4: # Edición de usuarios
        print("-----------------------------")
        print("---- Edición de usuarios ----")
        print("-----------------------------")
        print()
        print("1.- Crear nuevo usuario")
        print("2.- Eliminar usuario")
        print()

        opcion=int(input("¿Qué desea hacer?: "))
        print()

        if opcion==1: #Creación de usuarios
            archivo=open("que_como_hoy_DB","a")
            newUser=input("Nombre de usuario: ").capitalize()
            archivo.write("{}\n".format(newUser))
            archivo.close

            archivo=open("que_como_hoy_DB_{}".format(newUser),"w")
            archivo.write("{}\n".format(newUser))
            archivo.close

            print("Se ha creado al usuario '{}'".format(newUser))
            print("Podrá crear una lista cuando inicie sesión, en el menú 'Crear nueva lista' o 'Edición de comidas'.")
            print()
        
        elif opcion==2: #Eliminar usuario
            delUser=input("Inserte el usuario a eliminar: ").capitalize()
            sN=input("Se va a eliminar al usuario '{}' ¿Está seguro? s/n: ".format(delUser)).upper()

            if sN=="S":
                existe= path.exists("que_como_hoy_DB_{}".format(delUser))
                if existe==True:
                    remove("que_como_hoy_DB_{}".format(delUser))

                    #borrado del nombre en el fichero de 'usuarios'
                    archivo= open("que_como_hoy_DB")
                    lista=[]

                    for nombre in archivo:
                        nombre=nombre.rstrip("\n").capitalize()
                        lista.append(nombre)
                    archivo.close

                    lista.remove(delUser)
                    
                    archivo= open("que_como_hoy_DB","w")
                    for nombre in lista:
                        archivo.write("{}\n".format(nombre))
                    archivo.close
                    
                else:
                    print("No se ha introducido un usuario válido.")
                    print()

            elif sN=="N":
                print("Se volverá al menú principal.")
                print()
                print()
    
            

    elif opcion==5: # Salir
        print("{},gracias por usar '¿Qué como hoy?' Esperamos verle pronto!".format(usuario))
        control=2

    else:
        print("No ha introducido una opción válida.")
        print("Se volverá al menú principal.")
        print()
        print()
