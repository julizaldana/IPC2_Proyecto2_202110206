#NOMBRE: Julio Alejandro Zaldaña Ríos
#CARNET: 202110206
#IPC 2
#PROYECTO 2
#-------------------------------------

from xml.dom import minidom
import xml.etree.ElementTree as ET
from ListaSimple import ListaSimple

if __name__=='__main__':



    def cargar_archivo(ruta):
        tree=ET.parse(ruta)
        root=tree.getroot()
        for elemento in root.findall('empresa'):
            nombre= elemento.find('nombre').text
            abreviatura = elemento.find('abreviatura').text
            print('Nombre:' + nombre, 'Abreviatura:' + abreviatura)

        


        #for elemento in root.findall('empresa'):
            #empresas.crearEmpresa(elemento.attrib['id'],)
           # print('Empresa', elemento.attrib['id'],' ha sido insertado')
            #for subelemento in elemento.iter('pelicula'):
                #empresa=empresas.getEmpresa(elemento.attrib['id'])
                #empresa.lista_puntoAtencion.insertarEmpresa(subelemento.attrib['id'],subelemento.attrib['nombre'],subelemento.attrib['direccion'],subelemento.text)
                #print('El punto de atención ',subelemento.attrib['id'],' es de la empresa ',empresa.id)


    def menu():
        Lista_Empresas=ListaSimple()
        print("                                             ")
        print("---------------------------------------------")
        print("MENU - SOLUCIONES GUATEMALTECAS S.A")
        print("1. Configuracion de empresas")
        print("2. Crear Empresa")
        print("3. Seleccion de empresa y puntos de atencion")
        print("4. Manejo de puntos de atencion")
        print("5. Información Estudiante")
        print("6. Salir de aplicación")
        print("---------------------------------------------")
        respuesta = input("Ingrese una opcion: ")
        

        if respuesta == '1':
            print()
            print("                                             ")
            print("---------------------------------------------")
            print("       CONFIGURACION DE EMPRESAS             ")
            print("1. Cargar archivo de configuracion de sistema")
            print("2. Crear una nueva empresa")
            print("3. Cargar archivo con configuracion inicial")
            print("4. Regresar al menu principal")
            print("5. Ver empresas")
            print("---------------------------------------------")
            respempresa = input("Ingrese una opcion:  ")

            if respempresa =='1':
                #Filename=input('Ingrese nombre de archivo: ')
                file='C:/Users/juliz/OneDrive/Escritorio/Proyecto2/IPC2_Proyecto2_202110206/ConfigSys.xml'
                cargar_archivo(file)
                return menu()

                #Filename=input('Ingresar nombre de archivo: ')
                #file='./'+Filename
                #documentoxml = minidom.parse(file)
               # empresas = documentoxml.getElementsByTagName("listaEmpresas")
                #print("----------------------------------------------------------")
                #print("            Lista de Empresas                 ")
                #print("----------------------------------------------------------")
                #for empresa in empresas:
                    #id = empresa.getElementsByTagName("empresa id")[0]                    
                    #nombre = empresa.getElementsByTagName("nombre")[0]
                    ##print("id:" + str(id.firstChild.data) + "Nombre: " + str(nombre.firstChild.data) + "Abreviatura: " + str(abreviatura.firstChild.data))
            elif respempresa == '2':
                c=input('Ingrese un id para una empresa: ')
                n=input('Ingrese un nombre para la empresa: ')
                o=input('Ingrese una abreviatura para la empresa: ')
                Lista_Empresas.añadirEmpresa(c,n,o)


            elif respempresa == '3':
                file2='C:/Users/juliz/OneDrive/Escritorio/Proyecto2/IPC2_Proyecto2_202110206/ConfigInit.xml'
                cargar_archivo(file2)



            
            elif respempresa =='4':
                return menu()


            elif respempresa=='5':
                Lista_Empresas.imprimirEmpresas()




        elif respuesta == '2':
            c=input('Ingrese un id para una empresa: ')
            n=input('Ingrese un nombre para la empresa: ')
            o=input('Ingrese una abreviatura para la empresa: ')
            Lista_Empresas.añadirEmpresa(c,n,o)

            return menu()

            '''print("Selecciona una empresa:  ")
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
                #Por cada escritorio, mostrar número de clientes atendidos'''

        elif respuesta =='3':
            Lista_Empresas.imprimirEmpresas()
            return menu()



        elif respuesta == '5':
            print("NOMBRE: Julio Alejandro Zaldaña Ríos")
            print("CARNET: 202110206")
            return menu()

        elif respuesta == '6':
            exit()


    menu()