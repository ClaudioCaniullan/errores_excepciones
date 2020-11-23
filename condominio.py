

# Utilizar encapsulamiento
# Discutir en grupo sobre el uso de variables de esta forma
# Que es name mangling 
# ¿Es   posible   acceder   un   atributo   definido como:
#                           self.__nombre_atributo  desde   una subclase o desde el programaprincipal? 
#                           Experimente y muestre ejemplos


''' Crear 2 instancias de edificios y 2 de condominios horizaontales y demuestre la utilizacion de atributos y metodos '''

class Condominio:
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



class Guardia:
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



class UnidadHabitacional:
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



class CuentaCorriente:
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


class Terreno:
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




# Crear dos clases con herencia multiple de las clases Terreno y Comunidad, que se llamen CondominioVertical y CondominioHorizontal

class Comunidad:

    buena_convivencia = 'Respeta las reglas de convivencia'

    def __init__(self, nombre_comunidad):
        self.nombre_comunidad = nombre_comunidad

    def ComiteMascotas(self):
        print('Ven a participar del comite de mascotas')

    def JuegosPasatiempos(self):
        self.mensaje = 'Puedes visitar las áreas de esparcimiento'
        self.naci_aqui2 = 'Este es un mensaje que viene de la clase Comunidad'
        return self.mensaje


# Crear 5 atributos y 6 metodos propios que diferencien a cada una de estas subclases . Demostrar 2 casos de polimorfismo en metodos.
class CondominioVertical(Terreno, Comunidad):

    # 5 atributos
    tipo_condominio_vertical = 'Edificios habitacionales'
    terreno_km2 = 48524
    areas_verdes = 1425
    riego_automatico = True
    seguridad = True

    def __init__(self, nombre_condominio_vertical):
        self.nombre_condominio_vertical = nombre_condominio_vertical
        super().factibilidad_agua_potable()

    # llamamos a métodos de la clase Terreno
    def met_terr(self):
        super().factibilidad_agua_potable()
        super().factibilidad_electricidad()

    def polimorfeame1(self):
        super().factiilidad_servicios_digitales()
        self.message = 'Antes decia lo siguiente: 100 por ciento de factibilidad de electricidad'
        return self.message, self.naci_aqui

    # llamamos a métodos de la clase Comunidad
    def met_com(self):
        super().ComiteMascotas()

    def polimorfeame2(self):
        super().JuegosPasatiempos()
        self.mensaje = 'Antes decia lo siguiente: Puedes visitar las áreas de esparcimiento'
        return self.mensaje, self.naci_aqui2

    # métodos propios de la clase CondominioVertical
    def Ascensor(self):
        print("En estos momentos el servicio de ascensor se encuentra en mantenimiento, disculpe las molestias")

    def Terraza(self):
        print("Hermosas terrezas, únicas en Chile")

    def Quincho(self):
        print("Los mejores asados en tu quincho 3.0 'Lo último en tecnología'")

    def Piscina(self):
        print("Descubra las nuevas piscinas sin agua 'Antiahogos'")

    def Gym(self):
        print("Gym el Primo. Sin dolor no hay gloria")

class CondominioHorizontal(Terreno, Comunidad): # Se asignan 5 atributos
    # 5 atributos
    tipo_condominio_horizontal = 'Conjunto privado de casas'
    color = "Amarillo"
    juegos = True
    balcones = False
    m2 = 1000

    def __init__(self, nombre_condominio_h): # Inicializamos el nombre del condominio
        self.nombre_condominio_h = nombre_condominio_h

    # llamamoa a métodos de la clase Terreno
    def terrenox(self):
        super().factibilidad_agua_potable()
        super().factibilidad_electricidad()
        super().factiilidad_servicios_digitales()

    #polimorfismo_1
    def factibilidad_agua_potable(self):
        super().factibilidad_agua_potable()
        self.mensaje = "Ya no tiene agua potable"
        return self.mensaje

    #polimorfismo_2

    def consulta_hta(self):
        super().consulta_hta()
        self.mensaje = "Ahora las hectareas edificales consisten en 20 hectareas"
        return self.mensaje

    # llamamos a métodos de la clase Comunidad
    def condominiox(self):
        super().ComiteMascotas()
        super().JuegosPasatiempos()

    # métodos propios de la clase CondomioHorizontal

    def cine(self):
        print("Contamos con una sala de cina en la junta vecinal")

    def multicancha(self):
        print("Multicanchas de futbol y tenis")

    def estacionamietos(self):
        print("Estacionamientos de visita sin limite de tiempo")

    def ciclovia(self):
        print("Tiene ciclovia")

    def minimarket(self):
        print("Contamos con nuestros propios MiniMarket's dentro del condominio")



if __name__ == "__main__":
    
    # Pruebas de la clase Condominio
    print("\n***** Aquí comienzan las pruebas en clase Condominio")
    condominio1 = Condominio() # Creo instancia de condominio
    print(condominio1.get_direccion()) # muestra direccion
    condominio1.set_direccion("Esta es la nueva direccion") # cambio direccion
    print(condominio1.get_direccion()) # imprimo direccion nueva
    condominio1.set_administrador("Inserte aquí un administrador") # Agrego administrador
    print(condominio1.get_administrador()) # imprimo nombre del administrador agregado
    condominio1.add_guardia("Inserte aquí un guardia") # Agrego guardia a lista
    print(condominio1.get_guardias()) # Imprimo lista de guardias
    condominio1.add_guardia("Guardia a eliminar") # crear guardia para ser eliminado
    print(condominio1.get_guardias()) # Imprimo lista de guardias, para verificacion
    condominio1.del_guardia("Guardia a eliminar") # elimino guarida de lista
    print(condominio1.get_guardias()) # Imprimo lista de guardias, para verificacion
    
    # Pruebas en clase CondominioVertical
    print("\n***** Aquí comienzan las pruebas en clase CondominioVertical")
    edificio1 = CondominioVertical('Soy el edificio 1')
    edificio2 = CondominioVertical('Soy el edificio 2')
    print("Estos son los dos edificios creados:", edificio1.nombre_condominio_vertical, "y", edificio2.nombre_condominio_vertical)
    print("Aca tenemos un mensaje usando polimorfismo: \n", edificio1.polimorfeame1())
    print("Este es la segunda prueba de uso de polimorfismo: \n", edificio2.polimorfeame2())

    # Pruebas CondominioHorizontal
    print("### CONDOMINIO HORIZONTAL ###")
    condominio_horizonal = CondominioHorizontal("LOS PERALES")
    condominio_horizonal2 = CondominioHorizontal("GUARDIA VIEJA")
    print("El nombre del condominio es:", condominio_horizonal.nombre_condominio_h, "&", condominio_horizonal2.nombre_condominio_h) 
    print("#### APLICANDO POLIMORFISMO ####", condominio_horizonal.factibilidad_agua_potable())
    print("#### APLICANDO POLIMORFISMO ####", condominio_horizonal.consulta_hta())
    condominio_horizonal.cine()
    condominio_horizonal.multicancha()
    condominio_horizonal.estacionamietos()
    condominio_horizonal.ciclovia()
    condominio_horizonal.minimarket()

