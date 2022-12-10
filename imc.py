print ("Este es mi Programa Principal")
#Le pedimos el nombre y lo guardamos en un input
# Definicion de Variables
#try:
nombre = input ("Su nombre por favor: ")
apellido = input ("Ingrese su Pallido: ")
if nombre =="" :
    print ("No puede ir el dato en blanco, debe de ingresar el nombre y el apellido")
    exit ()
#except:
 #   print ("solo Caracteres Alfanumericos")

print (nombre)
print ("Hola",nombre,"bienvenido al programa de calculo de IMC")
try:
#Se pide al edad que siempre es un entero por eso el int()
    edad = int(input("Su edad en años sin Fracciones por favor: "))
 #El peso es con Kilos y con fracciones,  hay que ponerle punto, es un flotante float()
    peso = float (input ("Introduce tu peso en Kilogramos: "))
 #La altura es en metros y con fracciones,  hay que ponerle punto, es un flotante foat()
    altura = float (input("Introduce tu altura: "))
except:
    print ("Error ingrese solo numeros, y no puede ir en blanco el dato")
    exit()
#Calculo del Indice corporal
imc = peso / altura **2
print (nombre, apellido,",","tu masa corporal es de",  imc)
#Nota
