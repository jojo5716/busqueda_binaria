# coding=utf-8
import time
import math

#Datos de Entrada:
print "=========================================="
print "|                                        |"
print "|       Juguemos a las adivinanzas       |"
print "|                                        |"
print "|            Elige un numero entero      |"
print "|             el cual tendre que         |"
print "|                  adivinar              |"
print "|                                        |"
print "|                                        |"
print "|                                        |"
print "=========================================="

opcion = input("Numero: ")

# Variables
intentos   =  math.log(opcion, 2)
n_intentos =  0
vector     =  sorted([n for n in xrange(opcion + 1)])
tam        =  len(vector)
centro     =  0
encontrado =  "N"
posicion   =  0
inf        =  0
sup        =  tam-1

print "Piensa en un numero del 0 al %s" % opcion
time.sleep(3)
print "Adivinare el numero en %s intentos." % int(intentos)
time.sleep(3)

while inf <= sup:
 centro = ((sup + inf) / 2)
 encontrado = raw_input("Tu numero es: %s ? [S/N]" % vector[centro])

 if encontrado.upper() == "N":
  es_menor = raw_input("%s es menor que el numero que pensaste? [S/N]" % vector[centro])
  n_intentos += 1
 else:
  encontrado = "S"
  posicion = vector[centro]
  break

 if es_menor.upper() == "N":
  sup = centro - 1
 else:
  inf = centro + 1

if encontrado == 'S':
 print 'El numero que habias pensado es %s y lo he adivinado en %s intentos' % (posicion, n_intentos)
else:
 print 'No has pensado un numero entre 0 Y %s' % opcion
