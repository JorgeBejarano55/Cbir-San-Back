import numpy as np
import cv2 
import cv2 as cv
import matplotlib.pyplot as plt
from skimage import io,filters
import base64
import glob
import os
import shutil
import errno
import shutil

cv_img = []
img_sele=[]

def retornaImagenes():
#variables globales


#leyendo imagenes de la base de datos
    for img in glob.glob("images/*.jpg"):
        n= cv2.imread(img)
        cv_img.append(n)


#realizando procesamiento

    #leyendo imagen recibida del front metodo post

    img1 = cv.imread('imagenRecibida.jpg')          # queryImage
    
    # inicializando detector SIFT
    sift = cv.SIFT_create()

    # aplicando filtros a las imagenes para un mejor procesado
    imag18bit = cv2.normalize(img1, None, 0, 255, cv2.NORM_MINMAX).astype('uint8')
    img1=cv2.cvtColor(imag18bit,cv2.COLOR_BGR2GRAY)
    median = filters.median(img1)
    #encontrando puntos de interes con SIFT
    kp1, des1 = sift.detectAndCompute(median,None)
    
    banderax= False
    bandera=17
    if os.path.exists('Cbir-Front-SanAgustin/src/assets/seleccion'):
        shutil.rmtree('Cbir-Front-SanAgustin/src/assets/seleccion')
    
    os.mkdir('Cbir-Front-SanAgustin/src/assets/seleccion')
    for im in cv_img:
        #normalizando imagenes a 8bits
        image8bit = cv2.normalize(im, None, 0, 255, cv2.NORM_MINMAX).astype('uint8')
        img2=cv2.cvtColor(image8bit,cv2.COLOR_BGR2GRAY)
        median2 = filters.median(img2) 
        kp2, des2 = sift.detectAndCompute(median2,None)
        # BFMatcher con parametros por defecto entre dos imagenes
        bf = cv.BFMatcher()
        matches = bf.knnMatch(des1,des2,k=2)
        # aplicadon medidas de distancia
        good = []
        for m,n in matches:
            if m.distance < 0.60*n.distance:
                good.append([m])
                
        #codificando y guardando las seleccionadas
        if(len(good)>15):
            #plt.imshow(im), plt.show()
            #image_64_encode = base64.b64encode(im)
            cv2.imwrite('Cbir-Front-SanAgustin/src/assets/seleccion/'+str(bandera)+'.png',im)
            bandera+=1
            
            #img_sele.append(image_64_encode)
    aux=[]
    if os.path.exists('Cbir-Front-SanAgustin/src/assets/seleccion'):
        aux=os.listdir('Cbir-Front-SanAgustin/src/assets/seleccion/')
    
    return aux

array=retornaImagenes()   

