# Importamos las librerias
import cv2
import matplotlib.pyplot as plt
import os
# ruta de la imagen
ruta_imagen = os.path.join(
    "img-original-0106",
    "porshe.jpg"
)
# Imagen
# Vamos a crear nuestra matriz principal
porshe = cv2.imread(ruta_imagen)
print(porshe)
# convertir de BGR A RGB COLOR_BGR2RGB
porshi = cv2.cvtColor(porshe, cv2.COLOR_BGR2RGB)
# print (porshe) muestra
cv2.imshow("porshe original 0106", porshi)
cv2.waitKey(0) # tiempo de espera
cv2.destroyAllWindows # desttuye todas loas ventanas en memoria
print("Samuel Nicola 0106")