

class Condominio: # Claudio  ## 1xStopIteration, 1xValueError
    __direccion = "Las blancas palomas 1457, Buin"
    lista_administrador = []
    lista_guardias = []
    num_unidades_habitacionales = 0
    lista_unidades = []
    cuenta_corriente = ""
   
    # lista de atributos
    lista_atributos = ['areas verdes', 'sistema riego', 'tipo cableado', 'camino publico']

    # agregue este constructor
    def __init__(self, nombre):
        self.nombre = nombre

    def get_direccion(self):
        return self.__direccion

    def set_direccion(self, new_adress):
        self.__direccion = new_adress

    def set_administrador(self, admin):
        self.lista_administrador = admin

    def get_administrador(self):
        return self.lista_administrador

    def add_guardia(self, new_guard):
        self.lista_guardias.append(new_guard)

    def del_guardia(self, del_guard):
        if del_guard in self.lista_guardias:
            self.lista_guardias.remove(del_guard)
        else:
            print("No se puede eliminar, guardia no existe en registros")

    def get_guardias(self):
        return self.lista_guardias

    def get_unidades(self):
        return self.num_unidades_habitacionales

    # Agregar 4 metodos adicionales Servicios 

    def ServicioBasura(self):
        print('Recolección de basura servicios operativo')

    def ServicioGasfiter(self):
        print('Servicio de Gasfiter gratis para propietarios')

    def ServicioPlomeria(self):
        print('Servicio de plomeria gratis para propietarios')


    # 1xStopIteration
    def ServidioJardineria(self):

        try:
            print('Servicio de jardinerai gratis para propietarios')
            g = (i for i in 'OK')
            l =next(g)
            print(l)
            m= next(g)
            print(m)
            # Generador de StopIteration
            n = next(g)

        except StopIteration as e:
            print(e)


    # 1xValueError
    def Emergencia(self):

    		try:
                numero = int(input('Marque 911:'))
    			if numero == 911:
    				print('bien hecho')
    		# Si no se ingresa el int 911 Genera ValueError
    		except ValueError:
    			print('No marcaste correctamente')


## Verificación de errores
#1xValueError
condominio1 = Condominio('piraña')
condominio1.Emergencia()
#1xStopIteration
condominio1.ServidioJardineria()






class Guardia: # Seba #  1xArithmeticError # 2xTypeError #Exception
    # 3 atributos y 4 metodos OK

    empresa_contratista = 'Tus guardias'
    tipo_contrato = 'Contrato de plata'
    sueldo_bruto = '800.000 mil pesos'

    
    def __init__(self, nombre, rut, sexo):
        self.nombre = nombre
        self.rut = rut
        self.sexo = sexo

    def desayunar(self):
        print("8:00 am hora de desayunar en el casino")

    def almuerzo(self):
        print('13:00 pm hora de almorzar en el casino')

    def fin_jornada(self):
        print('17:00 pm hora de fin de jornada')



class UnidadHabitacional: # Valentina # 1xAttributeError # 1xLookupError
    # 3 atributos y 4 metodos OK

    tipo = 'Material sólido'
    cantidad_habitaciones = 6
    extras = 'calefaccion central y aire acondicionado'

    def __init__(self, numero):
        self.numero = numero 

    def abrir_puerta(self):
        print('Se abre la puerta del hogar numero', self.numero)

    def cerrar_puerta(self):
        print('Se cierra la puerta del hogar numero', self.numero)

    def prender_luces(self):
        print('Prender luces')



class CuentaCorriente: # Walter # 1xImportError # NameError 
    # 3 atributos y 4 metodos OK

    banco = 'Banco Terra'
    tipo = 'Cuenta Corriente'
    beneficios = 'No se cobra comision en ninguna operación'
    
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo =saldo

    def girar(self, giro):
        self.saldo -= giro
        print('Se ha efectuado un giro por el monto de', giro)

    def abono(self, abono):
        self.saldo += abono
        print('Se ha abonado la cantidad de', abono)

    def consulta_saldo(self):
        print('El saldo actual es', self.saldo)


class Terreno: # Miguel #ZeroDivisionError #­­ GeneratorExit
    
    # 6 atributos y 6 metodos OK

    nombre_dueño_terreno = 'Metropolis'
    seguros = 'terreno con seguros comprometidos'
    tipo = 'terreno privado'
    sector = 'urbano'
    finalidad = 'Habitacional'
    extensiones = 'Para fines de contruccion horizontal y vertical'
    
    def __init__(self, nombre_terreno):
        self.nombre_terreno = nombre_terreno

    def consulta_hta(self):
        print('Las hectareas edificafles consisten en 10 hectareas')

    def factibilidad_agua_potable(self):
        print('100 por ciento de factibilidad de agua potable')

    def factibilidad_electricidad(self):
        print('100 por ciento de factibilidad de electricidad')
        

    def factiilidad_servicios_digitales(self):
        self.message = '100 por ciento de factibilidad de servicios digitales'
        self.naci_aqui = 'Soy un mensaje que viene de la clase Terreno'
        return self.message, self.naci_aqui

    def seguridad_terreno(self):
        print('El terreno cuenta con todas las normas de seguridad para construir')




input()