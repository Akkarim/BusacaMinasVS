from random import randint, choice
import csv

j1="" # Jugador 1
j2="" # Jugador 2 
M=[] # Matrix
eleccion="" #Elección de guardado

def crearMatriz(): #Crea la matriz de 30x30 con igual cantidad de números pares e impares
    global eleccion 
    print("¿Desea cargar la partida anterior?(s/n)")
    eleccion= input()
    if eleccion == "n":
        cPares = 0
        cImpares = 0
        global M
        M = []
        for i in range(10):
            M.append([]) #La convierte matriz
            for j in range(10):
                M[i].append(randint(0, 9)) #Genera un número aleatorio entre 0 y 9
                if cPares == 50 and cImpares != 50: #Si ya hay 450 pares llena con impares
                    M[i][j] = choice([1,3,5,7,9]) # Random de Impares
                elif cPares != 50 and cImpares == 50: #Si ya hay 450 pares llena con impares
                    M[i][j] = choice([0,2,4,6,8]) # Random de Pares            
                n = M[i][j]
                if n%2 == 0: #Revisa si es Par
                    cPares=cPares+1
                elif n%2 != 0: #Revisa si es Impar
                    cImpares=cImpares+1               
        with open('matriz.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(M)
    elif eleccion == "s":
        # global M
        M = []
        with open('matriz.csv', newline='') as f:
            reader = csv.reader(f, delimiter = ',')
            i = 0
            for row in reader:
                M.append([]) #La convierte matriz
                for j in range(10):
                    row[j]=int(row[j])
                M[i] = row
                i=i+1
 
def jugada(Matriz):
    global j1
    global j2
    global M
    global eleccion
    print(eleccion)
    intentosJ1 = 0 # a los 3 termina el juego
    intentosJ2 = 0 # a los 3 termina el juego
    M = Matriz
    turnos = 0
    p1 = 0 #Puntaje jugador 1
    p2 = 0 #Puntaje jugador 2
    if eleccion == "s":
        datos=[] #Vector para guardar los datos  
        with open('Datos.csv') as csvarchivo:
            entrada = csv.reader(csvarchivo)
            for reg in entrada:
                datos.append(reg)
        j1 = datos[0][0]
        j2 = datos[1][0]
        p1 = int(datos[0][1])
        p2 = int(datos[1][1])
        intentosJ1 = int(datos[0][2])
        intentosJ1 = int(datos[1][2])
        print("El jugador 1 era: " + j1 + " con " + str(p1) + " puntos y " + str(intentosJ1) + " intentos.")
        print("El jugador 2 era: " + j2 + " con " + str(p2) + " puntos y " + str(intentosJ2) + " intentos.")
    elif eleccion == "n":    
        print("Ingrese el nombre del jugador 1: ")
        j1 = input()
        print(" ")
        print("Ingrese el nombre del jugador 2: ")
        j2 = input()
        print(" ")
        
    print(j1 + " va a jugar por los números impares.")
    print(j2 + " va a jugar por los números pares.") 
    
    print(" ") 
    salir = 1
    while intentosJ1 < 3 and intentosJ2 < 3 and  salir==1:
        turnos += 1
        print("/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-")
        print (j1 + " ingrese la posición x de la matriz: ")
        x1 = int(input())
        print (j1 + " ingrese la posición y de la matriz: ")
        y1 = int(input())    
        casilla1 = M[x1][y1]
        if casilla1 == -1:
            print("¡Esta casilla ya esta usada, pierde el turno!")
            print(" ")
        else:
            sc1 = str(casilla1) #El str de la casilla para imprimirlo
            print(j1 + " Su casilla es: " + sc1)
            print(" ")
            if casilla1%2 == 0 : #Si es par
                p1 = p1+1
                print("¡Ganó un punto!")
                print(" ")
            else: 
                p1 = p1-1
                intentosJ1 = intentosJ1+1
                if intentosJ1 == 3:
                    break
                print("¡Perdió un punto, manc@!")
                print(" ")
            M[x1][y1] = -1 # la marca como usada
        fJ1 = str(3 - intentosJ1) #El str que dice cuántos intentos quedan
        sp1 = str(p1) #El str del puntaje para imprimirlo
        print(j1 + " su puntaje acutal es: " + sp1)
        print("Le quedan " + fJ1 + " intento(s)...")
        print(" ")
        print("/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-")
        print (j2 + " ingrese la posición x de la matriz: ")
        x2 = int(input())
        print (j2 + " ingrese la posición y de la matriz: ")
        y2 = int(input())
        casilla2 = M[x2][y2]
        if casilla2 == -1:
            print("¡Esta casilla ya esta usada, pierde el turno!")
            print(" ")
        else:
            sc2 = str(casilla2) #El str de la casilla para imprimirlo
            print(j2 + " Su casilla es: " + sc2)
            print(" ")
        
            if casilla2%2 != 0 : #Si es impar
                p2 = p2+1
                print("¡Ganó un punto!")
                print(" ")
            else: 
                p2 = p2-1
                intentosJ2 = intentosJ2+1
                if intentosJ2 == 3:
                    break
                print("¡Perdió un punto, manc@!")
                print(" ")
            M[x2][y2] = -1 # la marca como usadas
        fJ2 = str(3 - intentosJ2) #El str que dice cuántos intentos quedan
        sp2 = str(p2) #El str del puntaje para imprimirlo
        print(j2 + " su puntaje acutal es: " + sp2)
        print("Le quedan " + fJ2 + " intento(s)...")
        print(" ")
        sTurnos = str(turnos)
        print("Número de turno " + sTurnos)
        if turnos%2 == 0:#**********-*-----------------------------------------
            print("¿Desea guardarla partida? (s/n)")
            respuesta1 = input()
            print("¿Desea seguir jugando? (s/n)")
            respuesta2 = input()
            if respuesta1 == "s":
                with open('matriz.csv', 'w', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerows(M)
                datos = [(j1, p1, intentosJ1), (j2, p2, intentosJ2)]
                csvsalida = open('Datos.csv', 'w', newline='') #Para guardar los datos del jugador
                archivo = csv.writer(csvsalida)
                archivo.writerows(datos)
                del archivo
                csvsalida.close()
            if respuesta2 =="n":
                salir = 0
    #final del while
    if salir == 0:
        print("¡Gracias por jugar!")
    if intentosJ1 < 3: # Gana el jugador 1
        print("¡¡FELICIDADES " + j1 +" GANÓ!!")
    elif intentosJ2 < 3: # Gana el jugador 2
        print("¡¡FELICIDADES " + j2 +" GANÓ!!")
    elif intentosJ1 == intentosJ2:
        if p1 > p2:
            print("¡¡FELICIDADES " + j1 +" GANÓ!!")
        if p1 < p2:
            print("¡¡FELICIDADES " + j2 +" GANÓ!!")
            

#datos=[] #Vector para guardar los datos  
#with open('Datos.csv') as csvarchivo:
#    entrada = csv.reader(csvarchivo)
#    for reg in entrada:
#        datos.append(reg)
#
#print(datos[0][1])

crearMatriz()
#jugadores()
jugada(M)


