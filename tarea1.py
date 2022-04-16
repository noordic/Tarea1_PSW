# Nicolás Oporto
# Rol: 201773107-9


# Manejo de logs
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s : %(levelname)s : %(message)s',
                    filename = 'tarea1.log',
                    filemode = 'w',)
# Programar pilas

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.superior = None

    def apilar(self, dato):
        print(f"Agregado {dato} en la cima de la pila")
        # Si no hay datos, se agrega valor como elemento superior y termina, primera iteración
        if self.superior == None:
            self.superior = Nodo(dato)
            return
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.superior
        self.superior = nuevo_nodo

    def desapilar(self):
        # Si no hay datos en el nodo superior, regresamos
        if self.superior == None:
            print("No hay ningún elemento en la pila para desapilar")
            return

        print(f"Desapilar {self.superior.dato}")
        aux= self.superior.dato # var auxiliar para almacenar el dato que se desapila
        self.superior = self.superior.siguiente # nuevo valor superior
        return aux

    def imprimir(self):
        secuencia=""
        #print("Imprimiendo pila:")
        # Recorrer la pila e imprimir valores
        nodo_temporal = self.superior
        while nodo_temporal != None:
            print(f"{nodo_temporal.dato}", end=",")
            secuencia= secuencia + nodo_temporal.dato
            nodo_temporal = nodo_temporal.siguiente
        print("")
        secuencia=secuencia.split(",")[0]
        return secuencia

# Ejecución del programa
                
pilas_llenas= False
while True:
    try:
        opcion = int(input('\nIngresar 1 para almacenar secuencia de caracteres en una pila\nIngresar 2 para comparar 2 cadenas almacenadas: \n'))  # entrada de entero
        if opcion == 1:
            # PILA 1
            pila1 = Pila() #creo la pila 1
            logging.info('Pila 1 creada')
            car1 = ""
            while car1 != "0":
                car1 = input('\nIngresa caracter a la pila 1:\nPara ver secuencia de caracteres actual ingresa 8\nPara desapilar ingresa 9\nPara terminar la secuencia de caracteres ingresa 0\n') #caracteres dentro de la pila 1
                if len(car1)> 1:
                    print("Solo se pueden ingresar caracteres, intenta nuevamente.")
                    continue
                if car1 != "0" and car1 != "8" and car1 != "9":
                    pila1.apilar(car1)
                    logging.info("Caracter "+ car1 + " agregado a Pila 1.")
                if car1 == "8":
                    pila1.imprimir()
                if car1 == "9":
                    logging.info("Desapilado " + pila1.desapilar()+ " de Pila 1.")
            print("\nLa secuencia de caracteres en la pila 1 es:")
            pila1.imprimir()
            # PILA 2
            pila2 = Pila() #creo la pila 2
            logging.info('Pila 2 creada')
            car2 = ""
            while car2 != "0":
                car2 = input('\nIngresa caracter a la pila 2:\nPara ver secuencia de caracteres actual ingresa 8\nPara desapilar ingresa 9\nPara terminar la secuencia de caracteres ingresa 0\n') #caracteres dentro de la pila 2
                if len(car2)> 1:
                    print("Solo se pueden ingresar caracteres, intenta nuevamente.")
                    continue
                if car2 != "0" and car2 != "8" and car2 != "9":
                    pila2.apilar(car2)
                    logging.info("Caracter "+ car2 + " agregado a Pila 2.")
                if car2 == "8":
                    
                    pila2.imprimir()
                if car2 == "9":
                    logging.info("Desapilado " + pila2.desapilar()+ " de Pila 2.")
                
            print("\nLa secuencia de caracteres en la pila 2 es:")
            pila2.imprimir()
            pilas_llenas= True
        elif opcion == 2:
            if pilas_llenas == False:
                print("No hay cadenas almacenadas en pilas.")
            else:
                if pila1.imprimir() == pila2.imprimir():
                    print("Las cadenas son iguales.")
                    logging.info('Comparadas ambas cadenas y son iguales.')
                else:
                    print("Las cadenas son diferentes.")
                    logging.info('Comparadas ambas cadenas y son diferentes.')

        else:
            print("Opcion invalida.")
    except ValueError:
        print("No se ha ingresado un numero, intenta nuevamente.")
        continue

                
            


