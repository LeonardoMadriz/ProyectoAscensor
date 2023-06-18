import math
import pandas
import sys
import trafico_vertical
import dimensiones
import potencias

#Lectura de Archivo excel a trabajar
df = pandas.read_excel("trafico_vertical.xls")
df2 = pandas.read_excel("dimensiones.xls")

#calculo del contrapeso
def contrapeso(n):
    return round(1.5*n,2)

#calculo de la velocidad angular
def angular_velocity(vn,radio):
    return round(vn/radio,2)

#calculo del número de engranajes necesario
def gears(w):
    return int((120*math.pi)/w)

def run():
# Ascensor del grupo A
    #Lectura de archivo
    grupo1 = str(df.iloc[0,0])   #Nombre del grupo a trabajar
    z_a= float(df.iloc[0,1])    #Número de ascensores-->Excel
    p_a= float(df.iloc[0,2])    #Capacidad nominal-->Excel
    vn_a= float(df.iloc[0,3])   #Velocidad nominal-->Excel
    na_a = float(df.iloc[0,5])  #Pisos totales encima de la plataforma princial-->Excel
    ne_a = float(df.iloc[0,4])  #Pisos no atendidos-->Excel
    t1 = float(df.iloc[0,6])    #Tiempo -->Excel/Tabla 7
    t2 = float(df.iloc[0,7])    #Excel/Tabla 8

    sup1_a = float(df2.iloc[0,1])       #Carga nominal superior a la del ascensor, tabla 6, COVENIN 621-4
    inf1_a = float(df2.iloc[0,2])       #Carga nominal inferior a la del ascensor, tabla 6, COVENIN 621-4 
    sup2max_a = float(df2.iloc[0,3])    #superficie útil maxima 
    inf2max_a = float(df2.iloc[0,4])    #superficie util maxima 
    sup2min_a = float(df2.iloc[0,5])    #superficie util minima
    inf2min_a = float(df2.iloc[0,6])    #superficie util minima
    nom_a = float(df2.iloc[0,7])        #carga nominal de nuestro ascensor
    mc_a = nom_a/2                      #Peso de la cabina

    radio_a = 0.14                      #Radio de la polea del motor(m)
    
    c_a, i_a = trafico_vertical.calculus(z_a,p_a,vn_a,na_a,ne_a,grupo1,t1,t2)        #Cálculo del tráfico vertical
    dimin_a = dimensiones.interpolacion(sup1_a,sup2min_a,inf1_a,inf2min_a,nom_a)    #Cálculo de las dimensiones de la cabina Mínimas
    dimax_a = dimensiones.interpolacion(sup1_a,sup2max_a,inf1_a,inf2max_a,nom_a)    #Cálculo de las dimensiones de la cabina Máximas
    cp_a = contrapeso(nom_a)                                                        #Cálculo del contrapeso
    w_a = angular_velocity(vn_a,radio_a)                                            #Cálculo de la velocidad angular
    gears_a = gears(w_a)                                                            #Calculo del número de engranajes para la caja
    box_power_a = potencias.box_power(nom_a,vn_a,radio_a,w_a)/1000              #Potencia de la caja
    engine_power_a = potencias.engine_power(box_power_a)                            #Potencia del motor





#Ascensor del Grupo B
    #Lectura de archivo
    grupo2 = str(df.iloc[1,0])   #Nombre del grupo a trabajar
    z_b= float(df.iloc[1,1])    #Número de ascensores-->Excel
    p_b= float(df.iloc[1,2])    #Capacidad nominal-->Excel
    vn_b= float(df.iloc[1,3])   #Velocidad nominal-->Excel
    na_b = float(df.iloc[1,5])  #Pisos totales encima de la plataforma princial-->Excel
    ne_b = float(df.iloc[1,4])  #Pisos no atendidos-->Excel
    t1 = float(df.iloc[1,6])    #Tiempo -->Excel/Tabla 7
    t2 = float(df.iloc[1,7])    #Excel/Tabla 8


    sup1_b = float(df2.iloc[1,1])       #Carga nominal superior a la del ascensor, tabla 6, COVENIN 621-4
    inf1_b = float(df2.iloc[1,2])       #Carga nominal inferior a la del ascensor, tabla 6, COVENIN 621-4
    sup2max_b = float(df2.iloc[1,3])    #superficie útil maxima
    inf2max_b = float(df2.iloc[1,4])    #superficie util maxima
    sup2min_b = float(df2.iloc[1,5])    #superficie util minima
    inf2min_b = float(df2.iloc[1,6])    #superficie util minima
    nom_b = float(df2.iloc[1,7])        #carga nominal de nuestro ascensor
    mc_b = nom_b/2                      #Peso de la cabina

  
    radio_b = 0.12                      #Radio de la polea (m)
    
    c_b, i_b =trafico_vertical.calculus(z_b,p_b,vn_b,na_b,ne_b,grupo2,t1,t2)         #Cálculo vertical
    dimin_b = dimensiones.interpolacion(sup1_b,sup2min_b,inf1_b,inf2min_b,nom_b)    #Cálculo de las dimensiones de la cabina Mínimas
    dimax_b = dimensiones.interpolacion(sup1_b,sup2max_b,inf1_b,inf2max_b,nom_b)    # Cálculo de las dimensiones de la cabina Máximas
    cp_b = contrapeso(nom_b)                                                        #Cálculo del contrapeso
    w_b = angular_velocity(vn_b,radio_b)                                            #Cálculo de la velocidad angular
    gears_b = gears(w_b)                                                            #Calculo del número de engranajes para la caja
    box_power_b = potencias.box_power(nom_b,vn_b,radio_b,w_b)/1000              #Potencia de la caja
    engine_power_b = potencias.engine_power(box_power_b)                            #Potencia del motor







#Ascensor del Grupo C
    #Lectura de archivo
    grupo3 = str(df.iloc[2,0])   #Nombre del grupo a trabajar
    z_c= float(df.iloc[2,1])    #Número de ascensores-->Excel
    p_c= float(df.iloc[2,2])    #Capacidad nominal-->Excel
    vn_c= float(df.iloc[2,3])   #Velocidad nominal-->Excel
    na_c = float(df.iloc[2,5])  #Pisos totales encima de la plataforma princial-->Excel
    ne_c = float(df.iloc[2,4])  #Pisos no atendidos-->Excel
    t1 = float(df.iloc[2,6])    #Tiempo -->Excel/Tabla 7
    t2 = float(df.iloc[2,7])    #Excel/Tabla 8


    sup1_c = float(df2.iloc[2,1])       #Carga nominal superior a la del ascensor, tabla 6, COVENIN 621-4
    inf1_c = float(df2.iloc[2,2])       #Carga nominal inferior a la del ascensor, tabla 6, COVENIN 621-4
    sup2max_c = float(df2.iloc[2,3])    #superficie útil maxima
    inf2max_c = float(df2.iloc[2,4])    #superficie útil maxima
    sup2min_c = float(df2.iloc[2,5])    #superficie util minima
    inf2min_c = float(df2.iloc[2,6])    #superficie util minima
    nom_c = float(df2.iloc[2,7])        #capacidad nominal de nuestro ascensor
    mc_c = nom_c/2                      #Peso de la cabina

  
    radio_c = 0.12                      #Radio de la polea(m)
    
    c_c, i_c =trafico_vertical.calculus(z_c,p_c,vn_c,na_c,ne_c,grupo3,t1,t2)         #Cálculo vertical
    dimin_c = dimensiones.interpolacion(sup1_c,sup2min_c,inf1_c,inf2min_c,nom_c)    #Cálculo de las dimensiones de la cabina Mínimas
    dimax_c = dimensiones.interpolacion(sup1_c,sup2max_c,inf1_c,inf2max_c,nom_c)    #Cálculo de las dimensiones de la cabina Máximas
    cp_c = contrapeso(nom_c)                                                        #Cálculo del contrapeso
    w_c = angular_velocity(vn_c,radio_c)                                            #Cálculo de la velocidad angular
    gears_c = gears(w_c)                                                            #Calculo del número de engranajes para la caja
    box_power_c = potencias.box_power(nom_c,vn_c,radio_c,w_c)/1000              #Potencia de la caja
    engine_power_c = potencias.engine_power(box_power_c)                            #Potencia del motor






#Ascensor del Grupo D
    #Lectura de archivo
    grupo4 = str(df.iloc[3,0])   #Nombre del grupo a trabajar
    z_d = float(df.iloc[3,1])   #Número de ascensores-->Excel
    p_d = float(df.iloc[3,2])   #Capacidad nominal-->Excel
    vn_d = float(df.iloc[3,3])  #Velocidad nominal-->Excel
    na_d = float(df.iloc[3,5])  #Pisos totales encima de la plataforma princial-->Excel
    ne_d = float(df.iloc[3,4])  #Pisos no atendidos-->Excel
    t1 = float(df.iloc[3,6])    #Tiempo -->Excel/Tabla 7
    t2 = float(df.iloc[3,7])    #Excel/Tabla 8

    sup1_d = float(df2.iloc[3,1])        #Carga nominal superior a la del ascensor, tabla 6, COVENIN 621-4
    inf1_d = float(df2.iloc[3,2])        #Carga nominal inferior a la del ascensor, tabla 6, COVENIN 621-4
    sup2max_d = float(df2.iloc[3,3])     #superficie útil maxima
    inf2max_d = float(df2.iloc[3,4])     #superficie útil maxima
    sup2min_d= float(df2.iloc[3,5])      #superficie util minima
    inf2min_d = float(df2.iloc[3,6])     #superficie util minima
    nom_d = float(df2.iloc[3,7])         #Carga nominal de nuestro ascensor
    mc_d = nom_d/2                      #Peso de la cabina

  
    radio_d = 0.14                        #Radio de la polea(m)
    
    c_d, i_d =trafico_vertical.calculus(z_d,p_d,vn_d,na_d,ne_d,grupo4,t1,t2)        #Cálculo vertical
    dimin_d = dimensiones.interpolacion(sup1_d,sup2min_d,inf1_d,inf2min_d,nom_d)    #Cálculo de las dimensiones de la cabina Mínimas
    dimax_d = dimensiones.interpolacion(sup1_d,sup2max_d,inf1_d,inf2max_d,nom_d)    #Cálculo de las dimensiones de la cabina Máximas
    cp_d = contrapeso(nom_d)                                                        #Cálculo del contrapeso
    w_d = angular_velocity(vn_d,radio_d)                                            #Cálculo de la velocidad angular
    gears_d = gears(w_d)                                                            #Calculo del número de engranajes para la caja
    box_power_d = potencias.box_power(nom_d,vn_d,radio_d,w_d)/1000              #Potencia de la caja
    engine_power_d = potencias.engine_power(box_power_d)                            #Potencia del motor



#Escritura de los datos
    writer = pandas.ExcelWriter('Resultados.xlsx')
    data1 = {
            'grupo':[grupo1, grupo2, grupo3, grupo4], 
            'Capacidad de transporte': [c_a,c_b,c_c,c_d],
            'Intervalo probable': [i_a,i_b,i_c,i_d],
            'Dimensión mínima': [dimin_a,dimin_b,dimin_c,dimin_d],
            'Dimensión máxima' : [dimax_a,dimax_b,dimax_c,dimax_d],
            'Contrapeso': [cp_a,cp_b,cp_c,cp_d],
            'Velocidad angular' : [w_a,w_b,w_c,w_d],
            'Números de engranes' : [gears_a,gears_b,gears_c,gears_d],
            'Potencia de la caja[Kw]' : [box_power_a,box_power_b,box_power_c,box_power_d],
            'Potencia del motor[Kw]': [engine_power_a,engine_power_b,engine_power_c,engine_power_d]
            }
    df1=pandas.DataFrame(data1)
    df1.to_excel(writer,'Objetos de casa', index=False)
    writer.close()

    print("El programa finalizó exitosamente!!")
if __name__ == "__main__":
    run()
