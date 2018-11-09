from random import randint, choice
import csv
j1="" # Jugador 1
j2="" # Jugador 2 
M=[] # Matrix
eleccion = ""

def crearMatriz(): #Crea la matriz de 30x30 con igual cantidad de números pares e impares
    print("¿Desea cargar la partida anterior?(s/n)")
    global eleccion = input()
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
    print (M)
                
def jugadores():
    global j1
    global j2
    print("Ingrese el nombre del jugador 1: ")
    j1 = input()
    print(" ")
    print("Ingrese el nombre del jugador 2: ")
    j2 = input()
    print(" ")
    print(j1 + " va a jugar por los números impares.")
    print(j2 + " va a jugar por los números pares.")  
    
def jugada(jugador1, jugador2, Matriz):
    print(" ")
    global j1
    global j2
    global M
    if eleccion == "S":
        j1 
        
    j1 = jugador1
    j2 = jugador2
    M = Matriz
    turnos = 0
    intentosJ1 = 0 # a los 3 termina el juego
    intentosJ2 = 0 # a los 3 termina el juego
    p1 = 0 #Puntaje jugador 1
    p2 = 0 #Puntaje jugador 2
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
        if turnos%2 == 0:
            print("¿Desea guardarla partida? (s/n)")
            respuesta1 = input()
            print("¿Desea seguir jugando? (s/n)")
            respuesta2 = input()
            if respuesta1 == "s":
                with open('matriz.csv', 'w', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerows(M)
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
            
crearMatriz()
jugadores()
jugada(j1, j2, M)









#!/usr/bin/python--------------------------------------------------------------
# 
#from random import randint
# 
## este es el juego buscaminas desarrollado en python.
## crear matriz, esta funcion no invoca ninguna otra funcion del programa
#def matriz(filas,columnas,caracter=False):
#    tablero = []
#    for i in xrange(0,filas):
#        v = [caracter]*columnas
#        tablero.append(v)
#    return tablero
# 
## poner minas aleatoriamente, esta funcion no invoca ninguna otra funcion del programa
#def minas(filas,columnas,tablero,minaz):
#    mi = 1
#    while mi <= minaz:
#        fil = randint(0,filas - 1)
#        col = randint(0,columnas - 1)
#        if not tablero[fil][col]:
#            tablero[fil][col] = True
#            mi += 1
#    return tablero
# 
## se crea el tablero de acuerdo a las especificaciones del jugador esta funcion invoca
## a la funcion matriz(es para crear una matriz dado el numero de filas y columnas)
## y a la funcion minas(es para colocar las pistas. las pistas son los numeros que aparecen en el juego)
#def tablero1():
#    opcion = input("quiere un juego aleatorio (si = 1)(no = 0): ")
#    if opcion :
#        while True:
#            print ("que dificultad desea?")
#            print 
#            print ("\t1. facil.")
#            print ("\t2. medio.")
#            print ("\t3. dificil.")
#            print 
#            opcion = raw_input("elija una opcion(f o facil)(m o medio)(d o dificil): ")
#            if opcion.lower() == ("f" or "facil"):
#                tablero = matriz(15,10)
#                minas(15,10,tablero,75)
#                return tablero,15,10
#            elif opcion.lower() == ("m" or "medio"):
#                tablero = matriz(25,20)
#                minas(25,20,tablero,250)
#                return tablero,25,20
#            elif opcion.lower() == ("d" or "dificil"):
#                tablero = matriz(35,30)
#                minas(35,30,tablero,525)
#                return tablero,35,30
#            else :
#                "debe escoger una de las opciones del menu."
#    else :
#        filas = input("ingresa el numero de filas que deseas: ")
#        columnas = input("ingresa el numero de columnas que desea: ")
#        while True:
#            mina = input("ingresa el numero de minas que desea: ")
#            if mina <= filas * columnas:
#                break
#            print "el numero de minas debe ser menor que %d."%(filas*columnas)
#        tablero = matriz(filas,columnas)
#        minas(filas,columnas,tablero,mina)
#        return tablero,filas,columnas
# 
## poner las pistas que son los numeros que aparecen en el tablero
## esta funcion solo hace uso de la funcion matriz
#def numeros(tablero,filas,columnas):
#    nueva = matriz(filas,columnas,".")
#    for i in xrange(0,filas):
#        for j in xrange(0,columnas):
#            # calcular el numero de vecinos de la celula que se esta vicitando
#            n = 0
#            if i > 0 and j > 0 and tablero[i - 1][j - 1]:
#                n += 1
#            if j > 0 and tablero[i][j - 1]:
#                n += 1
#            if i < filas - 1 and j > 0 and tablero[i + 1][j - 1]:
#                n += 1
#            if i > 0 and tablero[i - 1][j]:
#                n += 1
#            if i < filas - 1 and tablero[i + 1][j]:
#                n += 1
#            if i > 0 and j < columnas - 1 and tablero[i - 1][j + 1]:
#                n += 1
#            if j < columnas - 1 and tablero[i][j + 1]:
#                n += 1
#            if i < filas - 1 and j < columnas - 1 and tablero[i + 1][j + 1]:
#                n += 1
#            if not tablero[i][j]:
#                nueva[i][j] = n
#            else :
#                nueva[i][j] = True
#    tablero = nueva
#    return tablero
# 
## mostrar el tablero de juego, esta funcion no hace uso de ninguna otra funcion
#def mostrar(tablero,filas,columnas,caracter):
#    for i in xrange(0,filas):
#        for j in xrange(0,columnas):
#            if j != columnas - 1 :
#                if type(tablero[i][j]) == (int or str):
#                    print tablero[i][j],
#                elif (type(tablero[i][j]) == bool) and (tablero[i][j]):
#                    print "*",
#                else :
#    
#                    print caracter,
#            else :
#                if type(tablero[i][j]) == (int or str):
#                    print tablero[i][j]
#                elif (type(tablero[i][j]) == bool) and (tablero[i][j]):
#                    print "*"
#                else:
#            
#                    print caracter
# 
## esta es la funcion que desapa el tablero
#def destapar(filas,columnas,fila,columna,tablero,nuevo):
#    nuevo[fila][columna] = tablero[fila][columna]
#    if tablero[fila][columna] == 0:
#        if fila > 0:
#            if (not tablero[fila - 1][columna]) and (nuevo[fila - 1][columna] != 0):
#                destapar(filas,columnas,fila - 1,columna,tablero,nuevo)
#            else :
#                nuevo[fila - 1][columna] = tablero[fila - 1][columna]
#        if fila < filas - 1:
#            if (not tablero[fila + 1][columna]) and (nuevo[fila + 1][columna] != 0):
#                destapar(filas,columnas,fila + 1,columna,tablero,nuevo)
#            else :
#                nuevo[fila + 1][columna] = tablero[fila + 1][columna]
#        if columna > 0:
#            if (not tablero[fila][columna - 1]) and (nuevo[fila][columna - 1] != 0):
#                destapar(filas,columnas,fila,columna - 1,tablero,nuevo)
#            else :
#                nuevo[fila][columna - 1] = tablero[fila][columna - 1]
#        if columna < columnas - 1:
#            if (not tablero[fila][columna + 1]) and (nuevo[fila][columna + 1] != 0):
#                destapar(filas,columnas,fila,columna + 1,tablero,nuevo)
#            else :
#                nuevo[fila][columna + 1] = tablero[fila][columna + 1]
# 
##esta funcion toma la jugada del jugador, esta funcion no hace uso de ninguna otra funcion
#def jugada(filas,columnas):
#    print "para hacer su jugada debe especificar tanto la fila como la columna."
#    while True:
#        fila = input("ingrese la fila: ")
#        columna = input("ingrese la columna: ")
#        if (1 <= fila <= filas) and (1 <= columna <= columnas):
#            break
#        print "debe escoger una ficha que este dentro del rango de fila y columna."
#    return fila,columna
# 
## esta es la funcion principal en la que corre el juego. esta funcion hace uso de las siguientes funciones
## matriz : cre una matriz dado el numero de filas y de columnas
## mostrar : esta funcion muestra cualquier matriz en forma de tablero
## jugada : esta funcion toma la jugada que hace el jugador
#def jugar(tablero,filas,columnas):
#    nueva = matriz(filas,columnas,".")
#    while True:
#        mostrar(nueva,filas,columnas,".")
#        fila,columna = jugada(filas,columnas)
#        if type(tablero[fila - 1][columna - 1]) == int:
#            nueva[fila - 1][columna - 1] = tablero[fila - 1][columna - 1]
#            if tablero[fila - 1][columna - 1] == 0:
#                destapar(filas,columnas,fila - 1,columna - 1,tablero,nueva)
#        else :
#            mostrar(tablero,filas,columnas," ")
#            print "has perdido!!!"
#            print "eso te pasa por destapar la ficha en la posicion (%d,%d)."%(fila,columna)
#            break
#        acabar = True
#        for i in xrange(0,filas):
#            for j in range(0,columnas):
#                if nueva[i][j] == ".":
#                    acabar = False
#                    break
#                if not acabar:
#                    break
#        if acabar:
#            print "habeis ganado el juego."
#            print "felicitaciones!!!"
# 
#print "este es el clasico juego buscaminas."
#print "el juego consiste en descubrir todas las fichas que no tengan minas(las cuales estan representadas por \"*\""
#print "los numeros que aparecen en la pantalla indica cuantas bomas aparecen al rededor."
#print "cuando aparece el numero 0 es porque no hay ninguna bomba al rededor."
#print "para seleccionar la ficha a destapar tendra que especificar la fila y la columna."
#print "que empieze el juego."
# 
#jugar1 = True
# 
#while jugar1:
# 
#    tablero,filas,columnas = tablero1()
#    tablero = numeros(tablero,filas,columnas)
#    jugar(tablero,filas,columnas)
# 
#    jugar1 = input("desea jugar ora vez (si = 1)(no = 0)")