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

    def ServidioJardineria(self):
        print('Servicio de jardinerai gratis para propietarios')



    # FALTA 1xStopIteration
    # 1xValueError
    def Emergencia(self):

    		numero = int(input('Marque 911:'))

    		try:
    			if numero == 911:
    				print('bien hecho')
    			
    		except ValueError:
    			print('No marcaste correctamente')


    def iteracion(self):
    	cantidad = int(input('ingrese la cantidad de elementos que desea revisar:'))
    





condominio1 = Condominio('piraña')
condominio1.Emergencia()

input()