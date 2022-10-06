#NOMBRE: Julio Alejandro Zaldaña Ríos
#CARNET: 202110206
#IPC 2
#PROYECTO 2
#-------------------------------------

from cgitb import text
from xml.dom import minidom
from ListaDoble import ListaDoble
from ListaDobleEscritorios import ListaEscritorio
from ListaSimple import ListaSimple
from ClaseCola import Cola
from ListaEscritoriosActivos import ListaEscritorioActivo
from ColaClientes import ColaCliente
import xml.etree.ElementTree as ET
from colorama import Fore, Back, Style

Lista_Empresas=ListaSimple()
Lista_PuntosAtencion=ListaDoble()
Lista_Escritorios=ListaEscritorio()
Lista_EscritoriosActivos=ListaEscritorioActivo()
colacliente=ColaCliente()
cola=Cola()


#FUNCION PARA CARGAR ARCHIVO DE SISTEMA DE CONFIGURACION DE EMPRESAS

def cargar_archivo(ruta,empresas):
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
                sucursal = puntoAt.lista_puntoAtencion.getPuntoAtencion(idpunto)
                idescritorio = escritorio.get('id')
                identificacionesc = escritorio.find('identificacion').text
                encargadoesc = escritorio.find('encargado').text
                sucursal.lista_escritorios.insertarEscritorio(idescritorio,identificacionesc,encargadoesc)
                print('Se añade correctamente',idescritorio,identificacionesc,encargadoesc)

                for transaccion in empresa.iter('transaccion'):
                    transacc = empresas.getEmpresa(id)
                    idtransaccion = transaccion.get('id')
                    nombretransaccion = transaccion.find('nombre').text
                    tiempotransaccion = transaccion.find('tiempoAtencion').text
                    transacc.lista_transacciones.insertarTransaccion(idtransaccion,nombretransaccion,tiempotransaccion)

            
#FUNCION PARA CARGAR ARCHIVO DE SISTEMA PARA INICIALIZACION DE CLIENTES


                 
def cargar_archivoini(ruta2,clientes,empresas,sucursal):
    tree=ET.parse(ruta2)
    root=tree.getroot()


    for config in root.findall('configInicial'):
        id = config.get('idEmpresa')
        idpunto = config.get('idPunto')
        puntoAt = empresas.getEmpresa(id)
        sucursal = puntoAt.lista_puntoAtencion.getPuntoAtencion(idpunto)

        for escritoriosactivos in config.iter('escritorio'):
            idEscritorioActivo = escritoriosactivos.get('idEscritorio')
            sucursal.lista_escritoriosactivos.insertarEscritorioActivo(idEscritorioActivo)
            print('Se añade correctamente',idEscritorioActivo)

    for cliente in root.iter('cliente'):
        dpi = cliente.get('dpi')
        nombrecliente = cliente.find('nombre').text
    
        for transaccioncl in cliente.iter('transaccion'):
            transacciones = transaccioncl.get('idTransaccion')
            datos = ('dpi: ' + dpi + '      ' + 'nombre:  ' + nombrecliente + '      ' + 'transacciones: ' + transacciones + '||')
            clientes.encolar(datos)
            print('Se añadió el cliente ', datos)







def menu():
    opcion=''
    while opcion!='19':
        print("---------------------------------------------")
        print("     MENU - SOLUCIONES GUATEMALTECAS S.A     ")
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
        print('---------------------------------------------')
        print('11. Crear Cliente')
        print('12. Ver Cola de Clientes')
        print('13. Cargar Archivo Configuracion Inicial')
        print('14. Activar Escritorio')
        print('15. Desactivar Escritorio')
        print('16. Mostrar Escritorios Activos')
        print('17. Atender Cliente en Escritorio')
        print('18. Salir ')
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
            x=input(Fore.BLUE+'Ingresar nombre de la empresa que se requiere eliminar')
            Lista_Empresas.eliminarEmpresa(x)
        elif opcion=='4':
            id=input(Fore.GREEN+'Ingresar id de empresa: ')
            empresa=Lista_Empresas.getEmpresa(id)
            if empresa is None:
                print('> id incorrecto o no registrado')
            else:
                idPA=input('Ingrese id del punto de atencion: ')
                nombrePA=input('Ingrese nombre del punto de atencion: ')
                direccionPA=input('Ingrese direccion del punto de atencion: ')
                empresa.lista_puntoAtencion.insertarPuntoAtencion(idPA,nombrePA,direccionPA)
        elif opcion=='5':
            y=input(Fore.BLUE+'Ingresar id de la empresa: ' )
            empresa=Lista_Empresas.getEmpresa(y)
            if empresa is None:
                print(Fore.RED+'> id incorrecto o no registrado')
            else:
                print(Fore.GREEN+'Empresa: ',empresa.nombre)
                print(Fore.GREEN+'----------Sucursales para',empresa.nombre,'------')
                empresa.lista_puntoAtencion.mostrarPuntoAtencion()


        elif opcion=='6':
            z=input('Ingrese id de la empresa: ')
            empresa=Lista_Empresas.getEmpresa(z)
            if empresa is None:
                print(Fore.RED+'> id incorrecto o no registrado')
            else:
                w=input('Ingrese id de una sucursal para la empresa')
                sucursal = empresa.lista_puntoAtencion.getPuntoAtencion(w)
                
                if sucursal is None:
                    print('No existe esa sucursal para la empresa: ')
                else:
                    idEscritorio=input('Ingrese un id para el escritorio: ')
                    identificacionEsc=input('Ingrese un numero de identificación para el escritorio: ')
                    encargadoEsc=input('Ingrese el nombre del encargado del escritorio: ')
                    sucursal.lista_escritorios.insertarEscritorio(idEscritorio,identificacionEsc,encargadoEsc)  

        elif opcion=='7':
            z=input('Ingrese id de la empresa: ')
            empresa=Lista_Empresas.getEmpresa(z)
            if empresa is None:
                print(Fore.RED+'> id incorrecto o no registrado')
            else:
                w=input('Ingrese id de una sucursal para la empresa: ')
                sucursal = empresa.lista_puntoAtencion.getPuntoAtencion(w)
                
                if sucursal is None:
                    print('No existe esa sucursal para la empresa')
                else:
                    print(Fore.GREEN+'Los escritorios para la empresa: ',empresa.nombre, 'en', sucursal.nombre)
                    print(Fore.GREEN+'----------Escritorios disponibles para ',empresa.nombre,'en',sucursal.nombre,'------')
                    sucursal.lista_escritorios.mostrarEscritorio()




        elif opcion =='8':
            id=input(Fore.GREEN+'Ingresar id de empresa: ')
            empresa=Lista_Empresas.getEmpresa(id)
            if empresa is None:
                print('> id incorrecto o no registrado')
            else:
                idTransaccion=input('Ingresar id de la transaccion: ')
                nombreTransaccion=input('Ingrese nombre de la transaccion: ')
                tiempoTransaccion=input('Ingrese el tiempo de atencion para la transaccion (minutos): ')
                empresa.lista_transacciones.insertarTransaccion(idTransaccion,nombreTransaccion,tiempoTransaccion)            

        elif opcion =='9':
            n=input(Fore.BLUE+'Ingresar id de la empresa: ' )
            empresa=Lista_Empresas.getEmpresa(n)
            if empresa is None:
                print(Fore.RED+'> id incorrecto o no registrado')
            else:
                print(Fore.GREEN+'Empresa: ',empresa.nombre)
                print(Fore.GREEN+'----------Transacciones disponibles para ',empresa.nombre,':-------')
                empresa.lista_transacciones.mostrarTransacciones()


        elif opcion =='10':
            Filename=input('Ingresar nombre de archivo: ')
            file='./'+Filename
            cargar_archivo(file, Lista_Empresas)
            return menu()
        

# ------------------------------- MANEJO ARCHIVO CLIENTES -------------------------------


        elif opcion=='11':
            dpi=input('Ingrese el dpi del cliente: ')
            nombrecliente=input('Ingrese el nombre del cliente: ')
            transaccionarealizar=input('Ingrese una transacción a realizar por el cliente: ')
            nuevocliente=('dpi: ' + dpi + '      ' + 'nombre:  ' + nombrecliente + '      ' + 'transacciones: ' + transaccionarealizar + '||')
            cola.encolar(nuevocliente)
            return menu()

        elif opcion =='12':
            cola.imprimirCola()
            return menu()

        elif opcion=='13':
            Filename=input('Ingresar nombre de archivo: ')
            file='./'+Filename
            cargar_archivoini(file,cola,Lista_Empresas,Lista_EscritoriosActivos)
            return menu()


        elif opcion=='14':
            print('-----------------------------')
            print('    ACTIVAR ESCRITORIO       ')
            l=input('Ingrese id de la empresa: ')
            empresa=Lista_Empresas.getEmpresa(l)
            if empresa is None:
                print(Fore.RED+'> id incorrecto o no registrado')
            else:
                v=input('Ingrese id de una sucursal para la empresa: ')
                sucursal = empresa.lista_puntoAtencion.getPuntoAtencion(v)
                
                if sucursal is None:
                    print('No existe esa sucursal para la empresa: ')
                else:
                    print(Fore.GREEN+'Los escritorios para la empresa: ',empresa.nombre, 'en', sucursal.nombre)
                    print(Fore.GREEN+'----------Escritorios disponibles para ',empresa.nombre,'en',sucursal.nombre,'------')
                    sucursal.lista_escritorios.mostrarEscritorio()
                    r=input('Ingrese id del escritorio a activar: ')
                    escritorio = sucursal.lista_escritorios.getEscritorio(r)

                    if escritorio is None:
                        print('No escribió correctamente el escritorio. ')
                    else:
                        print('Escritorio ',escritorio.id, 'ha sido activado')
                        idescactivo=escritorio.id
                        sucursal.lista_escritoriosactivos.insertarEscritorioActivo(idescactivo)


        elif opcion=='15':
            print('-----------------------------')
            print('    DESACTIVAR ESCRITORIO       ')
            l=input('Ingrese id de la empresa: ')
            empresa=Lista_Empresas.getEmpresa(l)
            if empresa is None:
                print(Fore.RED+'> id incorrecto o no registrado')
            else:
                v=input('Ingrese id de una sucursal para la empresa: ')
                sucursal = empresa.lista_puntoAtencion.getPuntoAtencion(v)
                
                if sucursal is None:
                    print('No existe esa sucursal para la empresa: ')
                else:
                    print(Fore.GREEN+'----------Los escritorios activos para la empresa: ',empresa.nombre, 'en', sucursal.nombre,'------------')
                    sucursal.lista_escritoriosactivos.mostrarEscritorioActivo()
                    r=input('Ingrese id del escritorio a desactivar: ')
                    escritorio = sucursal.lista_escritoriosactivos.getEscritorioActivo(r)

                    if escritorio is None:
                        print('No escribió correctamente el escritorio activo. ')
                    else:
                        print('Escritorio ',escritorio.id, 'ha sido desactivado')
                        iddesactivado=escritorio.id
                        sucursal.lista_escritoriosactivos.eliminarEscritorioActivo(iddesactivado)



        elif opcion=='16':
            print('-----------------------------')
            print('    ESCRITORIOS ACTIVOS      ')
            l=input('Ingrese id de la empresa: ')
            empresa=Lista_Empresas.getEmpresa(l)
            if empresa is None:
                print(Fore.RED+'> id incorrecto o no registrado')
            else:
                v=input('Ingrese id de una sucursal para la empresa: ')
                sucursal = empresa.lista_puntoAtencion.getPuntoAtencion(v)
                
                if sucursal is None:
                    print('No existe esa sucursal para la empresa: ')
                else:
                    print(Fore.GREEN+'----------Los escritorios activos para la empresa: ',empresa.nombre, 'en', sucursal.nombre,'------------')
                    sucursal.lista_escritoriosactivos.mostrarEscritorioActivo()




        elif opcion =='17':
            print('------------------------------------------------')
            print('    MANEJO DE CLIENTES EN ESCRITORIOS ACTIVOS  ')
            l=input('Ingrese id de la empresa: ')
            empresa=Lista_Empresas.getEmpresa(l)
            if empresa is None:
                print(Fore.RED+'> id incorrecto o no registrado')
            else:
                v=input('Ingrese id de una sucursal para la empresa: ')
                sucursal = empresa.lista_puntoAtencion.getPuntoAtencion(v)
                
                if sucursal is None:
                    print('No existe esa sucursal para la empresa: ')
                else:
                    print(Fore.GREEN+'----------Los escritorios activos para la empresa: ',empresa.nombre, 'en', sucursal.nombre,'------------')
                    sucursal.lista_escritoriosactivos.mostrarEscritorioActivo()
                    r=input('Ingrese id del escritorio para atender cliente de la cola: ')
                    escritorio = sucursal.lista_escritoriosactivos.getEscritorioActivo(r)

                    if escritorio is None:
                        print('No escribió correctamente el escritorio activo. ')
                    else:
                        clienteatendido = cola.desencolar()
                        print('Se atenderá en el escritorio ',escritorio.id, 'al cliente con datos: ' ,clienteatendido)
                        ask=input('¿Terminar de atender al cliente? S/N: ')
                        
                        if ask =='S':
                            print(clienteatendido, 'fue atendido correctamente!')
                            return menu()
                        else:
                            return menu()



        elif opcion=='18': 
            exit()  

        else:
            break

    return menu()
menu()
