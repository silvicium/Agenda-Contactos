"""
EJERCICIO:
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
"""

import contactos, os , platform

def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
        #print("\n" * 10000000000000000000000000)  # Imprime 100 líneas en blanco para simular el efecto de limpieza
    else:
        os.system("clear") #clear para Linux y MacOS
        #print("\n" * 10000000000000000000000000)  # Imprime 100 líneas en blanco para simular el efecto de limpieza
        #Esta en comentario la linia 27 y 24 porque al final si funciona el clear de cada plataforma. En un primer intento no funcionaba pero un reincio del entorno y solucionado :)

while True:
    clear_console()
    print()
    print("Agenda de contactos:\n1. Insertar contacto\n2. Buscar contacto\n3. Actualizar contacto\n4. Eliminar contacto\n5. Mostrar todos los contactos\n6. Exit")

    opcion = "2" #input("Elige una opción: ")
    print()

    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    #Ponemos primero el 6 por si la persona quiere salir no ejecutar por detras otras cosas
    if opcion == "6" or opcion.lower() == "exit": #Dos condiciones con las que poder salir con el 6 o con el valor exit y añadido de que si esta escrito asi "EXIT" o "ExiT" el .lower() lo pone en minusculas
        print("Saliendo del programa...")
        clear_console()
        break

    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    elif opcion == "1":
        while True:
            # Solicitar el nombre y el número de teléfono en un solo input, separados por una coma
            entrada = input("Introduce el nombre y el número separados por una coma (o 'exit' para salir): ") #Ejemplo de como tiene que estar Alex,64266

            # Si el usuario escribe 'exit', rompemos el bucle
            if entrada.lower() == "exit":
                print("Volviendo al menu principal")
                break
            
            # Dividimos la entrada en nombre y número usando una coma
            if ',' in entrada:
                try:
                    nombre, numero = entrada.split(',') #Rompe el unico input para definirlo en dos valores dentro de una cadena EJ: ["Juan", "123456789"] 

                    # Elimina los posibles espacios en blanco alrededor del nombre y el número
                    nombre = nombre.strip()
                    numero = numero.strip()

                    # Comprobamos que el número este entre un rango de numeros para que no se introduzca por error un numero corto o largo
                    if len(numero) > 4 and len(numero) < 11:
                        long_numero = True

                        # Comprobamos que el numero sea valido
                        if numero.isdigit() and long_numero == True:
                            contactos.agenda[nombre] = numero  # Guardamos el contacto en la agenda
                            print(f"Contacto {nombre} agregado correctamente.")
                            print()
                            
                        else:
                            print("Número de teléfono no válido. Debe ser numérico y tener máximo 11 dígitos.")
                            clear_console()

                except ValueError:
                    print("Error: Asegúrate de separar el nombre y el número con una coma.")
            else:
                print("Formato incorrecto. Usa una coma para separar el nombre y el número.")

    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    elif opcion == "2":
        while True:
            buscador = input("Introduce el nombre o exit: ")
            
            if buscador.lower == "exit": 
                print("Volviendo al menu inicial")
                break

            for nombre, numero in contactos.agenda.items(): #El atributo .items() proporciona todo lo que hay en el diccionario tanto key como elemento, el .key() solo la key y el .values() solo el valor. Por eso en el for asignamos dos variables.
                nombre = nombre.lower()#Convierte todo el nombre en minusculas para que al buscar si o si encuentre a la persona independientemente de si a puesto la mayuscula en el orden que toca
                
                if nombre.startswith(buscador.lower()):
                   
                    agenda2 = {}
                    agenda2[nombre] = numero 
                    
                    y = 1
                    for x in range(len(agenda2)):
                        print(f"{y}.{nombre.title()}: {numero}") #.capitalize Convierte todas las primeras letras en mayusculas y title todo las primera letra de cada palabra
                        y += 1 

                
            
            salir = input("¿Exit? ")
            if salir.lower == "exit" or salir.lower() == "yes": #Recordar que si el atributo lower esta sin parentesis es condicion y con parentesis es un metodo
                print()
                print("Volviendo al menu inicial")
                break                
                


    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    elif opcion == "3":
        print("En construccion")

    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    elif opcion == "4":        
        print("En construccion")

    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    elif opcion == "5":        
        print(contactos.agenda)






























    else:
        print("¡Esto no tendria que haber pasado!")
