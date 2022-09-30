#NOMBRE: Julio Alejandro Zaldaña Ríos
#CARNET: 202110206
#IPC 2
#PROYECTO 2
#-------------------------------------

from xml.dom import minidom

if __name__=='__main__':

    def menu():
        print("                                             ")
        print("---------------------------------------------")
        print("MENU - SOLUCIONES GUATEMALTECAS S.A")
        print("1. Configuracion de empresas")
        print("2. Seleccion de empresa y puntos de atencion")
        print("3. Manejo de puntos de atencion")
        print("4. Información Estudiante")
        print("5. Salir de aplicación")
        print("---------------------------------------------")
        respuesta = input("Ingrese una opcion: ")

        if respuesta == '1':
            print()
            print("                                             ")
            print("---------------------------------------------")
            print("       CONFIGURACION DE EMPRESAS             ")
            print("1. Cargar archivo de configuracion de sistema")
            print("2. Crear una nueva empresa")
            print("3. Cargar archivo con condiguracion inicial")
            print("4. Información Estudiante")
            print("5. Regresar al menu principal")
            print("---------------------------------------------")
            respempresa = input("Ingrese una opcion:  ")

            if respempresa =='1':
                Filename=input('Ingresar nombre de archivo: ')
                file='./'+Filename
                documentoxml = minidom.parse(file)
                empresas = documentoxml.getElementsByTagName("listaEmpresas")
                print("----------------------------------------------------------")
                print("            Lista de Empresas                 ")
                print("----------------------------------------------------------")
                for empresa in empresas:
                    id = empresa.getElementsByTagName("empresa id")[0]                    
                    nombre = empresa.getElementsByTagName("nombre")[0]
                    abreviatura = empresa.getElementsByTagName("abreviatura")[0]
                    print("id:" + str(id.firstChild.data) + "Nombre: " + str(nombre.firstChild.data) + "Abreviatura: " + str(abreviatura.firstChild.data))

            elif respempresa =='5':
                return menu()
        
        elif respuesta == '2':
            print("     ")
            print("---------------------------------")
            print("     SELECCIÓN DE EMPRESAS       ")
            print("---------------------------------")
            print("Selecciona una empresa:  ")
            inputempresa = input()

            if inputempresa == '1':
                print('Escoger punto de atención: ')
                print('Muestra cantidad de escritorios activos, cant. escritorios inactivos, clientes en espera de atención')
                escritorioactivado = input()

                if escritorioactivado =='activar':
                    print("Escritorio inactivo pasarlo a activo")

                if escritorioactivado == 'desactivar':
                    print("Escritorio activo pasarlo a inactivo")

                #Atender cliente -> El primer cliente que entra a la cola será atendido.
                #Solicitud de atención -> agregar un cliente que solicita atención, permitir transaccion que desee realiza
                #Simular actividad del punto de atención -> se atiende a todos en la cola.
                #Mostrar clientes atendidos.
                #Por cada escritorio, mostrar número de clientes atendidos

        elif respuesta =='3':
            print(" ")



        elif respuesta == '4':
            print("NOMBRE: Julio Alejandro Zaldaña Ríos")
            print("CARNET: 202110206")
            return menu()

        elif respuesta == '5':
            exit()


    menu()