

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
        from . import config

    def consulta_saldo(self):
        print('El saldo actual es', self.saldo)



cuenta1 = CuentaCorriente("jose perez", 300000)


try:
    cuenta1.girar(int(input("introdusca el el monto a girar: ")))

except NameError:
    print("los valores ingresados no son validos")

except ValueError:
    print("los valores ingresados no son validos")


try:
    from . import config

except ImportError:
    print("modulo no importado correctamente")

try: 
    cuenta1.abono(int(input("introduce el monto abonar: ")))

    from . import config

except ValueError:
    print("los valores ingresados no son validos")

except ImportError:
    print("modulo no importado correctamente")

cuenta1.consulta_saldo()

try:
    from . import config

except ImportError:
    print("modulo no importado correctamente")

cuenta1.consulta_saldo()

print("Ejecucion de la transaccion finalizada")


class Terreno: # Miguel ZeroDivisionError, GeneratorExit

    
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

    def factibilidad_agua_potable(self): # SyntaxError
        try:
           print("Estoy generando un error de sintaxis por mala identacion")  # <---- Identado 3 espacios
        except SyntaxError:
            print("Eror de sintaxis, producido por mal identación")
        finally:
            print('100 por ciento de factibilidad de agua potable')

    def factibilidad_electricidad(self): # SyntaxError

        self.casa_id = input("Ingrese su ID para conocer el estado electrico de su domicilio\n>> ")
        
        self.listas_casas_elec_ok  = ["Casa1", "Casa2", "Casa3"]
        try:   
            if self.casa_id in self.listas_casas_elec_ok:
                print("Tiene factibilidad")
            else:
                print("Sin factibilidad por el momento")    
        except SyntaxError:
            print("Error de sintaxis")
        finally:
            print('Disfrute electricidad limpia sin efectos secundarios')
        

    def factiilidad_servicios_digitales(self):
        self.message = '100 por ciento de factibilidad de servicios digitales'
        self.naci_aqui = 'Soy un mensaje que viene de la clase Terreno'
        return self.message, self.naci_aqui

    def seguridad_terreno(self):
        print('El terreno cuenta con todas las normas de seguridad para construir')

    def divisor_terreno(self): # ZeroDivisionError
         #Indica en cuantas partes iguales puede dividir su terreno, ingresando parametro por usuario 

        print("Todos los terrenos cuenta con mil m² y tienes la posibilidad de calcular cuantos metros por terreno quedan luego de dividirlos")
        self.divisor = int(input("Ingrese el numero de partes igual que desea para su terreno de mil m²\n>>> "))

        try:
            self.resultado = 1000 // self.divisor
            print('si divides tu terreno por', self.divisor, 'cada uno de ellos tendra', self.resultado, 'm²')
        except ZeroDivisionError:
            print("Realizaste una division por 0, espero disfrutes tu terreno de mil metros 'SOLO'")
        finally:
            print("Gracias por usar la superCalculadora todo terreno")

######################## Trabajo realizado en clase Terreno -Inicio- ########################
if __name__ == "__main__":
    # ZeroDivisionError
    # terrenito.divisor_terreno()
    
    # SyntaxError
    terrenito = Terreno("test")
    terrenito.factibilidad_agua_potable() # Error 1
    # terrenito.factibilidad_electricidad() # Error 2


######################## Trabajo realizado en clase Terreno -Fin- ########################
