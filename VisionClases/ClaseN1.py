##### Clase 2 #####
#Open cv#
import cv2
import numpy as np


#Instruccion para cargar una imagen#
imagen = cv2.imread("Imagenes/perros.jpeg")

#Mostramos la imagen
cv2.imshow("Imagen cargada", imagen)
cv2.waitKey(0)  #Es para que muestre la imagen hasta que se presione una tecla

##Convertir en escala de grisies##
Gris=cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grises", Gris)
cv2.waitKey(0)

#Imformacion de la imagen
#Mostramos ancho, alto y canales
print("Tamaño: {} bytes".format(imagen.size))
print("Alto: {} pixeles".format(imagen.shape[0]))
print("Ancho: {} pixels".format(imagen.shape[1]))
print("Canales: {}".format(imagen.shape[2]))

#lo mismo de otra manera
print("Ancho: " + str(imagen.shape[1]) + " pixels")


###### Continuacion de la clase 2 ######

##Canales de color BGR
b=imagenbgr[:,:,0]
g=imagenbgr[:,:,1]
r=imagenbgr[:,:,2]

cv2.imshow("B",b)
cv2.waitKey(0)

cv2.imshow("G",g)
cv2.waitKey(0)

cv2.imshow("R",r)
cv2.waitKey(0)