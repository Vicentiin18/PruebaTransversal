import csv
import time
import random
from math import prod

trabajadores = ['Juan Pérez','María García','Carlos López','Ana Martínez','Pedro Rodríguez','Laura Hernández','Miguel Sánchez','Isabel Gómez','Francisco Díaz','Elena Fernández']
sueldo=[]
menor_800k=[]
entre_800k_2000k=[]
mayor_2000k=[]

#1
def sueldo_aleatorio():#asignar sueldos aleatorios
    sueldo1=random.randint(300000,2500000) 
    sueldo.append(sueldo1)
    if sueldo1<800000:
        menor_800k.append(sueldo1)
    elif sueldo1>=800000 and sueldo1<=2000000:
        entre_800k_2000k.append(sueldo1)
    elif sueldo1>2000000:
        mayor_2000k.append(sueldo1)
    
    
    sueldo2=random.randint(300000,2500000)
    sueldo.append(sueldo2)
    if sueldo2<800000:
        menor_800k.append(sueldo2)
    elif sueldo2>=800000 and sueldo2<=2000000:
        entre_800k_2000k.append(sueldo2)
    elif sueldo2>2000000:
        mayor_2000k.append(sueldo2)
    
 
    
  
        
    sueldo3=random.randint(300000,2500000)
    sueldo.append(sueldo3)
    if sueldo3<800000:
        menor_800k.append(sueldo3)
    elif sueldo3>=800000 and sueldo3<=2000000:
        entre_800k_2000k.append(sueldo3)
    elif sueldo3>2000000:
        mayor_2000k.append(sueldo3)
    
    
    
    sueldo4=random.randint(300000,2500000)
    sueldo.append(sueldo4)
    if sueldo4<800000:
        menor_800k.append(sueldo4)
    elif sueldo4>=800000 and sueldo4<=2000000:
        entre_800k_2000k.append(sueldo4)
    elif sueldo4>2000000:
        mayor_2000k.append(sueldo4)
    
    
    sueldo5=random.randint(300000,2500000)
    sueldo.append(sueldo5)
    if sueldo5<800000:
        menor_800k.append(sueldo5)
    elif sueldo5>=800000 and sueldo5<=2000000:
        entre_800k_2000k.append(sueldo5)
    elif sueldo5>2000000:
        mayor_2000k.append(sueldo5)
    
    
    
    sueldo6=random.randint(300000,2500000)
    sueldo.append(sueldo6)
    if sueldo6<800000:
        menor_800k.append(sueldo6)
    elif sueldo6>=800000 and sueldo6<=2000000:
        entre_800k_2000k.append(sueldo6)
    elif sueldo6>2000000:
        mayor_2000k.append(sueldo6)
    
    
    sueldo7=random.randint(300000,2500000)
    sueldo.append(sueldo7)
    if sueldo7<800000:
        menor_800k.append(sueldo7)
    elif sueldo7>=800000 and sueldo7<=2000000:
        entre_800k_2000k.append(sueldo7)
    elif sueldo7>2000000:
        mayor_2000k.append(sueldo7)
    
    
    sueldo8=random.randint(300000,2500000)
    sueldo.append(sueldo8)
    if sueldo8<800000:
        menor_800k.append(sueldo8)
    elif sueldo8>=800000 and sueldo8<=2000000:
        entre_800k_2000k.append(sueldo8)
    elif sueldo8>2000000:
        mayor_2000k.append(sueldo8)
    
      
    
    sueldo9=random.randint(300000,2500000)
    sueldo.append(sueldo9)
    if sueldo9<800000:
        menor_800k.append(sueldo9)
    elif sueldo9>=800000 and sueldo9<=2000000:
        entre_800k_2000k.append(sueldo9)
    elif sueldo9>2000000:
        mayor_2000k.append(sueldo9)
    
    
    sueldo10=random.randint(300000,2500000)
    sueldo.append(sueldo10)
    if sueldo10<800000:
        menor_800k.append(sueldo10)
    elif sueldo10>=800000 and sueldo10<=2000000:
        entre_800k_2000k.append(sueldo10)
    elif sueldo10>2000000:
        mayor_2000k.append(sueldo10)
    print("Sueldos listos")
    menu()
   
    
        

#2
def clasificar_sueldos():
    for i in range (len(menor_800k)):
        total=i+1
    print(f"Sueldos menores a $800.000| total{total} ")
    print("Nombre Trabajador|Sueldo")
    for j in range (len(menor_800k)):
        trabajador=trabajadores[j]
        print(f"{trabajador}|{menor_800k[j]}")
        
    for i in range (len(entre_800k_2000k)):
        total=i+1
    print(f"Sueldos entre $800.000 y $2.000.000| total{total} ")
    print("Nombre Trabajador|Sueldo")
    for j in range (len(entre_800k_2000k)):
        trabajador=trabajadores[j]
        print(f"{trabajador}|{entre_800k_2000k[j]}")
        
    for i in range (len(mayor_2000k)):
        total=i+1
    print(f"Sueldos mayor a $2.000.000| total{total} ")
    print("Nombre Trabajador|Sueldo")
    for j in range (len(mayor_2000k)):
        trabajador=trabajadores[j]
        print(f"{trabajador}|{mayor_2000k[j]}")
    menu()
  
  
        
    
    
    
 
#3
def ver_estadisticas():
    sueldosmax=max(sueldo)
    sueldomin=min(sueldo)
    promediosueldo=sum(sueldo)/10
    producto=prod(sueldo)
    mediaG=producto**(1/10)
    
    print(f"Sueldo Maximo: {sueldosmax}")
    print(f"Sueldo Minimo: {sueldomin}")
    print(f"Promedio de Sueldos: {promediosueldo}")
    print(f"Media Geometrica: {mediaG:.2f}")
    
#4
#def reporte_sueldos():
#sueldo_aleatorio()   
#clasificar_sueldos()    
    
    
def salir_programa():
    print("Finalizando programa...\nDesarrollado por Vicente Alvarez\nRUT 21.980.872-0")
    time.sleep(3)
    
    
def menu():
    print("Bienvenido, seleccione una de las siguientes opciones:")
    print("1.Asignar sueldos aleatorios")
    print("2.Clasificar sueldos")
    print("3.Ver estadisticas")
    print("4.Reporte de sueldos")
    print("5.Salir del programa")
    opc=int(input())
    
    if opc==1:
        sueldo_aleatorio()
        
            
    if opc==2:
        clasificar_sueldos()
    if opc==3:
        ver_estadisticas()
    #if opc==4:
     #   reporte_sueldos()
    if opc==5:
        salir_programa()    
                
            

menu()
