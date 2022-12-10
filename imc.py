print ("Este es mi Programa Principal")
#Le pedimos el nombre y lo guardamos en un input
# Definicion de Variables
while True:
    try:
        nombre = input ("Su nombre por favor: ")
        nombre[0] 


        apellido = input ("Ingrese su Apellido: ")
        apellido[0] 
        #print ("no puede ir el apellido en Blanco")
        break
#if nombre =="" :
#   print ("No puede ir nungun dato en Blanco, debe de ingresar el nombre y el apellido")
#    exit () 
#if apellido =="" :
#    print ("No puede ir ningun  dato en blanco, debe de ingresar el nombre y el apellido")
#    exit () 

    except:
        
        print ("No puede ir nungun dato en Blanco, debe de ingresar el nombre y el apellido")
        #break
  
    print ("Hola",nombre,"bienvenido al programa de calculo de IMC")
while True:
    try:
#Se pide al edad que siempre es un entero por eso el int()
        edad = int(input("Su edad en años sin Fracciones por favor: "))
        #edad [0]
 #El peso es con Kilos y con fracciones,  hay que ponerle punto, es un flotante float()
        peso = float (input ("Introduce tu peso en Kilogramos: "))
        #peso [0]
 #La altura es en metros y con fracciones,  hay que ponerle punto, es un flotante foat()
        altura = float (input("Introduce tu altura en metros y centimetros: "))
        #altura [:1]
        break

    except:
        print ("Error ingrese solo numeros, y no puede ir en blanco el dato")

#Calculo del Indice corporal
imc = peso / altura **2
print (nombre,apellido,",","tu masa corporal es de",  imc)
