#NOMBRE: Julio Alejandro Zaldaña Ríos
#CARNET: 202110206
#IPC 2
#PROYECTO 2
#-------------------------------------

from xml.dom import minidom
from xml.dom import minidom
from ListaDoble import ListaDoble
from ListaDobleEscritorios import ListaEscritorio
from ListaSimple import ListaSimple
from ClaseCola import Cola
import xml.etree.ElementTree as ET
import xml.etree.ElementTree as ET
from ListaSimple import ListaSimple

Lista_Empresas=ListaSimple()
Lista_PuntosAtencion=ListaDoble()
Lista_Escritorios=ListaEscritorio()
cola=Cola()

    #def cargar_archivo(ruta):
        #tree=ET.parse(ruta)
        #root=tree.getroot()
        #for elemento in root.findall('empresa'):
            #nombre= elemento.find('nombre').text
            #abreviatura = elemento.find('abreviatura').text
            #print('Nombre:' + nombre, 'Abreviatura:' + abreviatura)

    

        #for elemento in root.findall('empresa'):
            #empresas.crearEmpresa(elemento.attrib['id'],)
           # print('Empresa', elemento.attrib['id'],' ha sido insertado')
            #for subelemento in elemento.iter('pelicula'):
                #empresa=empresas.getEmpresa(elemento.attrib['id'])
                #empresa.lista_puntoAtencion.insertarEmpresa(subelemento.attrib['id'],subelemento.attrib['nombre'],subelemento.attrib['direccion'],subelemento.text)
                #print('El punto de atención ',subelemento.attrib['id'],' es de la empresa ',empresa.id)




def menuprincipal():
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
        return lambda:menu()

        '''print()
        print("                                             ")
        print("---------------------------------------------")
        print("       CONFIGURACION DE EMPRESAS             ")
        print("1. Cargar archivo de configuracion de sistema")
        print("2. Crear una nueva empresa")
        print("3. Cargar archivo con configuracion inicial")
        print("4. Regresar al menu principal")
        print("5. Ver empresas")
        print("---------------------------------------------")
        respempresa = input("Ingrese una opcion:  ")'''

        #if respempresa =='1':
            

            #Filename=input('Ingrese nombre de archivo: ')
            #file='C:/Users/juliz/OneDrive/Escritorio/Proyecto2/IPC2_Proyecto2_202110206/ConfigSys.xml'
            #cargar_archivo(file)
            #return menuprincipal()

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
       # elif respempresa == '2':
           # c=input('Ingrese un id para una empresa: ')
            #n=input('Ingrese un nombre para la empresa: ')
           # o=input('Ingrese una abreviatura para la empresa: ')
            #Lista_Empresas.añadirEmpresa(c,n,o)


        #elif respempresa == '3':
            #file2='C:/Users/juliz/OneDrive/Escritorio/Proyecto2/IPC2_Proyecto2_202110206/ConfigInit.xml'
            #cargar_archivo(file2)



        
        #elif respempresa =='4':
            #return menuprincipal()


        #elif respempresa=='5':
            #Lista_Empresas.imprimirEmpresas()




    elif respuesta == '2':
        return menuprincipal()

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
        print('')
        return menuprincipal()



    elif respuesta == '4':
        print("NOMBRE: Julio Alejandro Zaldaña Ríos")
        print("CARNET: 202110206")
        return menuprincipal()

    elif respuesta == '5':
        exit()


menuprincipal()


def cargar_archivo(ruta,empresas,sucursales):
    tree=ET.parse(ruta)
    root=tree.getroot()

    for empresa in root.findall('empresa'):
        id = empresa.get('id')
        nombre = empresa.find('nombre').text
        abreviatura = empresa.find('abreviatura').text
        empresas.añadirEmpresa(id,nombre,abreviatura)
        print('Se añadió correctamente',id,nombre,abreviatura)
    
        for puntosatenc in empresa.iter('puntoAtencion'):
            puntoAt=empresas.getEmpresa(id)
            idpunto = puntosatenc.get('id')
            nombrepunto = puntosatenc.find('nombre').text
            direccion = puntosatenc.find('direccion').text
            puntoAt.lista_puntoAtencion.insertarPuntoAtencion(idpunto,nombrepunto,direccion)
            print('Se añade correctamente',idpunto,nombrepunto,direccion)
        
            for escritorio in puntosatenc.iter('escritorio'):
                empresa=empresas.getEmpresa(id)
                if empresa is None:
                    print('> id incorrecto o no registrado')
                else:
                    sucursal = sucursales.getPuntoAtencion(idpunto)
                    if sucursal is None:
                        print('No existe esa sucursal para la empresa')
                    else:
                        idescritorio = escritorio.get('id')
                        identificacionesc = escritorio.find('identificacion').text
                        encargadoesc = escritorio.find('encargado').text
                        sucursal.lista_escritorios.insertarEscritorio(idescritorio,identificacionesc,encargadoesc)
                        print('Se añade correctamente',idescritorio,identificacionesc,encargadoesc)


                  
def cargar_archivoini(ruta2,clientes):
    tree=ET.parse(ruta2)
    root=tree.getroot()

    for cliente in root.iter('cliente'):
        dpi = cliente.get('dpi')
        nombrecliente = cliente.find('nombre').text
        datos = ('dpi:' + dpi + 'nombre: ' + nombrecliente)
        clientes.encolar(datos)
        print('Se añadió el cliente', datos)


def menu():
    opcion=''
    while opcion!='10':
        print("---------------------------------------------")
        print("MENU - SOLUCIONES GUATEMALTECAS S.A")
        print('1. Ingresar Empresa')
        print('2. Selección de Empresas')
        print('3. Eliminar Empresa')
        print('4. Crear Puntos de Atención')
        print('5. Ver puntos de atención por Empresas')
        print('6. Crear escritorios')
        print('7. Ver escritorios en sucursal de Empresa')
        print('8. Crear una transaccion para una empresa ')
        print('9. Mostrar transacciones para empresas ')
        print('10. Cargar Archivo Configuracion Sistema')
        print('11. Crear Clientes')
        print('12. Ver Clientes')
        print('13. Cargar Archivo Configuracion Inicial')
        print('14. Regresar a menu principal')
        print("---------------------------------------------")
        opcion=input('Ingrese una opcion: ')
        print(opcion)

        if opcion=='1':
            c=input('Ingrese un id para una empresa: ')
            n=input('Ingrese un nombre para la empresa: ')
            o=input('Ingrese una abreviatura para la empresa: ')
            Lista_Empresas.añadirEmpresa(c,n,o)

        elif opcion=='2':
            Lista_Empresas.imprimirEmpresas()

        elif opcion=='3':
            x=input('Ingresar nombre de la empresa que se requiere eliminar')
            Lista_Empresas.eliminarEmpresa(x)
        elif opcion=='4':
            id=input('Ingresar id de empresa: ')
            empresa=Lista_Empresas.getEmpresa(id)
            if empresa is None:
                print('> id incorrecto o no registrado')
            else:
                idPA=input('Ingrese id del punto de atencion: ')
                nombrePA=input('Ingrese nombre del punto de atencion: ')
                direccionPA=input('Ingrese direccion del punto de atencion: ')
                empresa.lista_puntoAtencion.insertarPuntoAtencion(idPA,nombrePA,direccionPA)
        elif opcion=='5':
            y=input('Ingresar id de la empresa: ' )
            empresa=Lista_Empresas.getEmpresa(y)
            if empresa is None:
                print('> id incorrecto o no registrado')
            else:
                print('Empresa: ',empresa.nombre)
                print('----------Sucursales para',empresa.nombre,'------')
                empresa.lista_puntoAtencion.mostrarPuntoAtencion()


        elif opcion=='6':
            z=input('Ingrese id de la empresa: ')
            empresa=Lista_Empresas.getEmpresa(z)
            if empresa is None:
                print('> id incorrecto o no registrado')
            else:
                w=input('Ingrese id de una sucursal para la empresa')
                sucursal = empresa.lista_puntoAtencion.getPuntoAtencion(w)
                
                if sucursal is None:
                    print('No existe esa sucursal para la empresa')
                else:
                    idEscritorio=input('Ingrese un id para el escritorio: ')
                    identificacionEsc=input('Ingrese un numero de identificación para el escritorio: ')
                    encargadoEsc=input('Ingrese el nombre del encargado del escritorio: ')
                    empresa.lista_escritorios.insertarEscritorio(idEscritorio,identificacionEsc,encargadoEsc)  

        elif opcion=='7':
            z=input('Ingrese id de la empresa: ')
            empresa=Lista_Empresas.getEmpresa(z)
            if empresa is None:
                print('> id incorrecto o no registrado')
            else:
                w=input('Ingrese id de una sucursal para la empresa')
                sucursal = empresa.lista_puntoAtencion.getPuntoAtencion(w)
                
                if sucursal is None:
                    print('No existe esa sucursal para la empresa')
                else:
                    print('Los escritorios para la empresa: ',empresa.nombre, 'en', sucursal.nombre)
                    print('----------Escritorios disponibles para ',empresa.nombre,'en',sucursal.nombre,'------')
                    empresa.lista_escritorios.mostrarEscritorio()

        elif opcion =='8':
            id=input('Ingresar id de empresa: ')
            empresa=Lista_Empresas.getEmpresa(id)
            if empresa is None:
                print('> id incorrecto o no registrado')
            else:
                idTransaccion=input('Ingresar id de la transaccion: ')
                nombreTransaccion=input('Ingrese nombre de la transaccion: ')
                tiempoTransaccion=input('Ingrese el tiempo de atencion para la transaccion (minutos): ')
                empresa.lista_transacciones.insertarTransaccion(idTransaccion,nombreTransaccion,tiempoTransaccion)            

        elif opcion =='9':
            n=input('Ingresar id de la empresa: ' )
            empresa=Lista_Empresas.getEmpresa(n)
            if empresa is None:
                print('> id incorrecto o no registrado')
            else:
                print('Empresa: ',empresa.nombre)
                print('----------Transacciones disponibles para ',empresa.nombre,':-------')
                empresa.lista_transacciones.mostrarTransacciones()

        elif opcion =='10':
            Filename=input('Ingresar nombre de archivo: ')
            file='./'+Filename
            cargar_archivo(file, Lista_Empresas, Lista_PuntosAtencion)
            return menu()
        


        elif opcion=='11':
            dpi=input('Ingrese el dpi del cliente: ')
            nombrecliente=input('Ingrese el nombre del cliente: ')
            cola.encolar('dpi: ' +  dpi + '   nombre: ' + nombrecliente)
            return menu()

        elif opcion =='12':
            cola.imprimirCola()
            return menu()



        elif opcion=='13':
            Filename=input('Ingresar nombre de archivo: ')
            file='./'+Filename
            cargar_archivoini(file,cola)
            return menu()


        elif opcion=='14': 
            exit()  

        else:
            break

menu()

