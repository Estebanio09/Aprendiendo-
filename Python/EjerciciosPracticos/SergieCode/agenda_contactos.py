
def menu():
    print("Agenda de contactos:\n")
    print("1 - Agregar contacto")
    print("2 - Listar contactos")
    print("3 - Buscar contacto")
    print("4 - Eliminar contacto")
    print("5 - Editar contacto")
    print("6 - Salir de la agenda")
    print("\n")


def agregar_contacto(agenda):
    print("\n")
    nombre = input("Introduzca el nombre del contacto: ")
    nombre = nombre.strip(" ")
    telefono = input("Introduzca el teléfono del contacto: ")
    correo = input("Introduzca el correo del contacto: ")
    agenda[nombre] = {'telefono': telefono, 'correo': correo}
    print("El contacto se creo exitosamente")
    print("\n")
   
    
def mostrar_agenda(agenda):
    print("\n")
    if agenda:
        for nombre,info in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"Telefono: {info["telefono"]}")
            print(f"Correo: {info["correo"]}")
            print("-"*20)
    else:
        print("¡La agenda esta vacía!")
        print("\n")
    print("\n")
       
        
def buscar_contacto(agenda):
    print("\n")
    contacto = input("Ingresa el nombre del contacto: ")
    contacto = contacto.strip(" ")
    if contacto in agenda:
        print("\n")
        print(f"Nombre: {contacto}")
        print(F"Telefono: {agenda[contacto]['telefono']}")
        print(F"Correo: {agenda[contacto]['correo']}")
    else:
        print("\n")
        print("El contacto no existe")
    print("\n")
    
    
def eliminar_contacto (agenda):
    contacto = input("Ingresa el nombre del contacto a eliminar: ")
    contacto = contacto.strip(" ")
    if contacto in agenda:
        del agenda[contacto]
        print('Contacto eliminado exitosamente')
    else:
        print("No se encontró el contacto a eliminar")
        
def menu_editar():
    print("\n")
    print("1 - Salir")
    print("2 - Editar nombre")
    print("3 - Editar número")
    print("4 - Editar correo")
    
    print("\n")
    
def editar_nombre (agenda, contacto):
    print("\n")
    nuevo_nombre = input("Ingresa el nuevo nombre: ")
    agenda[nuevo_nombre] = agenda.pop(contacto)
    contacto = nuevo_nombre
    print("Nombre editado correctamente")
    
def editar_numero (agenda, contacto):
    nuevo_telefono = input("Ingresa el nuevo número de telefono: ")
    agenda[contacto]["telefono"] = nuevo_telefono
    print("Telefono editado correctamente")
    
def editar_correo (agenda, contacto):
    nuevo_correo = input("Ingresa el nuevo correo: ")
    agenda[contacto]["correo"] = nuevo_correo
    
def editar_contacto(agenda):
    print("\n")
    contacto = input("Ingresa el contacto a editar: ")
    contacto = contacto.strip(" ")
    while True:
        if contacto in agenda: 
                menu_editar()
                opcion = input("Ingresa la opción que de deseas editar: ")
                if opcion == "1":
                    break
                elif opcion == "2":
                    editar_nombre(agenda, contacto)
                elif opcion == "3":
                    editar_numero(agenda, contacto)
                elif opcion == "4":
                    editar_correo(agenda, contacto)
                else:
                    print("Selecciona una opción valida")
        else: 
            print("El contacto no existe")

def agenda():
    agenda = {}
    
    while True:
        menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            mostrar_agenda(agenda)
        elif opcion == "3": 
            buscar_contacto(agenda)
        elif opcion == "4":
            eliminar_contacto(agenda)
        elif opcion == "5":
            editar_contacto(agenda)
        elif opcion == "6":
            break
        else:
            print("\n")
            print("¡Seleccione una opcion valida!")


agenda()


