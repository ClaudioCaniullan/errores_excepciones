

# Utilizar encapsulamiento
# Discutir en grupo sobre el uso de variables de esta forma
# Que es name mangling 
# ¿Es   posible   acceder   un   atributo   definido como:
#                           self.__nombre_atributo  desde   una subclase o desde el programaprincipal? 
#                           Experimente y muestre ejemplos


''' Crear 2 instancias de edificios y 2 de condominios horizaontales y demuestre la utilizacion de atributos y metodos '''

class Condominio: # Claudio  ## 1xStopIteration, 3xValueError
    __direccion = "Las blancas palomas 1457, Buin"
    lista_administrador = []
    lista_guardias = []
    num_unidades_habitacionales = 0
    lista_unidades = []
    cuenta_corriente = ""
    
    # atributos adicionales
    áreas_verdes = 'Plaza principal'
    sistema_riego = 'automatico'
    tipo_cableado = 'bajo tierra'
    camino_publico = 'cemento alta resistencia'


    def __init__(self):
        pass

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

    # Agregar 4 metodos adicionales Servicios REVISAR

    def ServicioBasura(self):
        print('Recolección de basura servicios operativo')

    def ServicioGasfiter(self):
        print('Servicio de Gasfiter gratis para propietarios')

    def ServicioPlomeria(self):
        print('Servicio de plomeria gratis para propietarios')

    def ServidioJardineria(self):
        print('Servicio de jardinerai gratis para propietarios')



class Guardia: # Seba #  1xArithmeticError # 2xTypeError
    # 3 atributos y 4 metodos OK

    empresa_contratista = 'Tus guardias'
    tipo_contrato = 'Contrato de plata'
    sueldo_bruto = '800.000 mil pesos'

    def __init__(self, nombre, rut, sexo):
        self.nombre = nombre
        self.rut = rut
        self.sexo = sexo

    def marcar_desayuno(self):
      while True:
        try:
          desayunar = int(input("Ingrese hora marcación: "))
          if desayunar == 8:
            print("8:00 am hora de desayunar en el casino")
            break
          elif desayunar != 8:
            print("El desayuno debe ser a las 8 A.M: ")
            continue
        except ValueError as ve:
            print( type(ve).__name__ , ": No se puede comparar un string con un int" )
        finally:
            print("Secuencia completada")
 
    def remuneraciones_guardia(self):
      while True:
        try:
            sueldo_base = int(input("Ingrese su sueldo base: "))
            horas_extras = str(input("Ingrese las horas extras realizadas: "))
            if sueldo_base > 0 and horas_extras > 0:
                total_sueldo = horas_extras + sueldo_base
                print(total_sueldo)
                break
        except TypeError as e:
            print( type(e).__name__ , ": No se puede sumar un entero con un string" )
            break
        except ValueError as v:
            print( type(v).__name__ , ": No se puede comparar un string con un int" )
        finally:
            print("Secuencia completada")

            
    def vacaciones_guardia(self):
        try:
            vacaciones_totales = 0
            dias_pedir = int(input("Ingrese días pedir: "))
            total = dias_pedir/vacaciones_totales
            print(total)
        except ArithmeticError:
            print("ArithmeticError: La operación no puede retornar un valor infinito")
        except Exception as e:
            print( type(e).__name__ , ": No se puede comparar un string con un int" )
        finally:
            print("Secuencia completa")

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


## Pruebas clase Guardia
guardia_1 = Guardia("Sebastian", "17920757-5","M") #Se crea instancia Guardia
guardia_1.remuneraciones_guardia() # datos solicitados por pantalla , se genera error 
guardia_1.marcar_desayuno() #datos solicitados por pantalla 
guardia_1.vacaciones_guardia() #error aritmetico