#Importamos librerias para ejecutar algunas variables 
import time 
import csv
from random import randint
from datetime import datetime 

#obtener datos de ppm(simulacion)
def datospulsasiones():
    return randint(60,200)
    
#obtener datos del gps
def datosgps():
    latitud = randint(0,90)
    longitud = randint(0,180)
    return latitud,longitud

#obtener datos de oxigeno 
def niveldeoxigeno():
    return randint(90,100)

#funcion para guardas datos 
def guardardatoscsv(data):
    archivo_existente = True  
    try:
        with open('resgistrodeportistas.csv','r') as file: 
            pass     
    except FileNotFoundError:
        archivo_existente = False 
        
    with open('resgistrodeportistas.csv', mode='a', newline='') as file:
         writer = csv.writer(file)
    
         if not archivo_existente:
             writer.writerow(["Tiempo","Latitud","Longitud","Pulsaciones","Nivel de oxigeno"])
             writer.writerow(data)    
try:
     while True:
      latitud,longitud = datosgps()
      pulsaciones = datospulsasiones()
      nivel_oxigneo = niveldeoxigeno()
      tiempoactual = datetime.now().strftime("%y-%m-%%d %H:%M:%S")
except KeyboardInterrupt: print("Algo salio mal")
#datos en tiempo real 
print(f"Tiempo:{tiempoactual}")
print(f"Latitud:{latitud}, Longitud: {longitud}")
print(f"Pulsaciones por minuto: {pulsaciones}")
print(f"Nivel de oxigeno:{nivel_oxigneo}%\n")

#Estableceremos tiempo para tomar datos
time.sleep(40)

