import math
import sys

def calculus(z,p,vn,na,ne,grupo,t1,t2): 
# Variables de entradas a tantear
    try:
        if p > 33:
            raise Exception("Se sobrepasa los límites permitidos por el modelo del ascensor")
    except Exception as ex:
        print(ex)
        sys.exit(1)



# Cuentas obtenidas de los datos de cada grupo de ascensores
    ep = 3.5                    #Altura entre pisos
    ns = na - ne                #Pisos recorridos
    B = ns*35 + 3*15            #Poblacion total
    phi = 1                     #Aceleración


#Valores pre-definidos por las reglas covenin, segun tablas
    try:
        pv = int(3.2/p +0.7*p +0.5)    #Personas por viaje-->Excel/Tabla 5      
        np = round(ns*(1-((ns-1)/ns)**pv),2)    #Número de paradas-->Excel/Tabla 3
        if np>250:
            raise Exception("Se sobrepasó el número máximo de paradas recomendado por el modelo del ascensor")
    except Exception as ex:
        print(ex)
        sys.exit(1)


#Calculo de otras variables
    ha = na * ep #Recorrido superior total
    he = round(ne* ep,4) # recorrido expreso
    hs = round(ha - he,4) # Recorrido sobre la planta principal con servicios de ascensores
    check = round(float(math.sqrt(hs*(phi)/np)),4)


# Calculo de los tiempos de un viaje completo
    if (check >= vn) and (grupo != "Grupo A"):
        tvc = 2*(ha/vn)+(vn/phi+t1)*(np+1)-hs/(np*vn)+t2*pv

    elif (check < vn) and (grupo != "Grupo A"):
        tvc =2*(ha/vn)-hs/vn+2*(vn/phi)+(2*hs/(np*check))*(np-1) + t1*(np+1) + t2*pv

 
    elif (check >= vn) and (grupo == "Grupo A"):
        tvc = 2*ha/vn + (vn/phi + t1)*(np + 1) + t2*pv

    elif (check < vn) and (grupo == "Grupo A"):
        tvc = 2*ha/math.sqrt((ha*(phi))/np)+vn/phi+ha/vn+t1*(np+1)+t2*pv
     
    else:
        print("Hay algo raro con la velocidad nominal")

    ta = (3/10)*tvc #Tiempo adicional
    ttv = tvc + ta #Tiempo de un circuito completo
    i = ttv/z
    i= round(i,2)
    c = (300*pv*(z*100))/(ttv*B)
    c = round(c,2)
    return (c,i)


def saludar():
    print("Hola")
