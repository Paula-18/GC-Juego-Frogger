from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *
#ubicacion de la mosca 1
xMosca1 = -0.8
yMosca1 = 0.85
#ubicacion de la mosca 2
xMosca2 = -0.3
yMosca2 = 0.85
#ubicacion de la mosca 3
xMosca3 = 0.3
yMosca3 = 0.85
#ubicacion de la mosca 4
xMosca4 = 0.78
yMosca4 = 0.85
#ubicacion del carro 1
xCarro1 = 1.2
yCarro1 = -0.65
#ubicacion del carro 2
xCarro2 = 1.7
yCarro2 = -0.65
#ubicacion del carro 3
xCarro3 = 2.4
yCarro3 = -0.65
#ubicacion del carro 4
xCarro4 = -1.2
yCarro4 = -0.15
#ubicacion del camion 1
xCamion1 = 1.2
yCamion1 = -0.3
#ubicacion del camion 2
xCamion2 = 2.0
yCamion2 = -0.3
#ubicacion del camion 3
xCamion3 = -1.2
yCamion3 = -0.5
#ubicacion del camion 4
xCamion4 = -2.0
yCamion4 = -0.5
#ubicacion de la priemra hilera de tortugas 
xTortuga1 = -1.2
yTortuga1 = 0.28
#ubicacion de la segunda hilera de tortugas 
xTortuga2 = -1.7
yTortuga2 = 0.28
#ubicacion de la teercera hilera de tortugas 
xTortuga3 = -2.5
yTortuga3 = 0.28
#ubicacion de la priemra hilera de nenufares  
xNenufar1 = -1.5
yNenufar1 = 0.7
#ubicacion de la segunda hilera de nenufares  
xNenufar2 = -2.0
yNenufar2 = 0.7
#ubicacion de la teercera hilera de nenufares 
xNenufar3 = -2.8
yNenufar3 = 0.7
#ubicacion del tronco 1
xTronco1 = 1.2
yTronco1 = 0.1
#ubicacion del tronco 2
xTronco2 = 1.8
yTronco2 = 0.1
#ubicacion del tronco 3
xTronco3 = 2.4
yTronco3 = 0.1
#ubicacion del tronco 4
xTronco4 = 1.6
yTronco4 = 0.5
#ubicacion del tronco 5
xTronco5 = 2.2
yTronco5 = 0.5
#ubicacion del tronco 6
xTronco6 = 2.8
yTronco6 = 0.5
#ubicacion de la rana al iniciar la partida
xRana = 0.0
yRana = -0.9
vidasdeRana = 3.0
xVidas = -0.9
yVidas = -0.9
#variables de colisiones de las moscas
colisionandoMosca1 = False
colisionandoMosca2 = False
colisionandoMosca3 = False
colisionandoMosca4 = False
colisionandoCarro = False
#angulo que se necesita para girar a la rana
angulo = 0
tiempo_anterior = 0.0


def checar_colisiones():
    global colisionandoMosca1
    global colisionandoMosca2
    global colisionandoMosca3
    global colisionandoMosca4
    global colisionandoCarro
    global xRana
    global yRana
    # Si extremaDerechaCarrito > extremaIzquierdaObstaculo
    # Y extremaIzquierdaCarrito < extremaDerechaObstaculo
    # Y extremoSuperiorCarrito > extremoInferiorObstaculo
    # Y extremoInferiorCarrito < extremoSuperiorObstaculo
    # Cuando la rana colisione con la mosca 1 se convertira en true y la rana regresara al punto de partida
    if xRana + 0.05 > xMosca1 - 0.05 and xRana - 0.05 < xMosca1 + 0.05 and yRana + 0.05 > yMosca1 - 0.05 and yRana - 0.05 < yMosca1 + 0.05:
        colisionandoMosca1 = True
        resetPosition()
    # Cuando la rana colisione con la mosca 2 se convertira en true y la rana regresara al punto de partida
    if xRana + 0.05 > xMosca2 - 0.05 and xRana - 0.05 < xMosca2 + 0.05 and yRana + 0.05 > yMosca2 - 0.05 and yRana - 0.05 < yMosca2 + 0.05:
        colisionandoMosca2 = True
        resetPosition()
    # Cuando la rana colisione con la mosca 3 se convertira en true y la rana regresara al punto de partida
    if xRana + 0.05 > xMosca3 - 0.05 and xRana - 0.05 < xMosca3 + 0.05 and yRana + 0.05 > yMosca3 - 0.05 and yRana - 0.05 < yMosca3 + 0.05:
        colisionandoMosca3 = True
        resetPosition()
    # Cuando la rana colisione con la mosca 4 se convertira en true y la rana regresara al punto de partida
    if xRana + 0.05 > xMosca4 - 0.05 and xRana - 0.05 < xMosca4 + 0.05 and yRana + 0.05 > yMosca4 - 0.05 and yRana - 0.05 < yMosca4 + 0.05:
        colisionandoMosca4 = True
        resetPosition()
    if colisionandoMosca1 == True and colisionandoMosca2 == True and colisionandoMosca3 == True and colisionandoMosca4 == True:
        exit()
    
def resetPosition():
    global xRana
    global yRana

    xRana = 0.0
    yRana = -0.9

def vidasRana():
    global vidasdeRana

    vidasdeRana = vidasdeRana - 1.0
    if vidasdeRana < 0:
        exit()

def actualizar(window):
    global angulo
    global xRana
    global yRana

    estadoIzquierda = glfw.get_key(window, glfw.KEY_LEFT)
    estadoDerecha = glfw.get_key(window, glfw.KEY_RIGHT)
    estadoAbajo = glfw.get_key(window, glfw.KEY_DOWN)
    estadoArriba = glfw.get_key(window, glfw.KEY_UP)

    if estadoIzquierda == glfw.PRESS and xRana - 0.05 > -1:
        angulo = 90
        xRana = xRana - 0.007
    if estadoDerecha == glfw.PRESS and xRana + 0.05 < 1:
        angulo = 270
        xRana = xRana + 0.007
    if estadoAbajo == glfw.PRESS and yRana - 0.05 - 0.001 > -1:
        angulo = 180
        yRana = yRana - 0.007
    # Para arriba hay que considerar que el viewport también
    # toma en cuenta la barra de titulo
    if estadoArriba == glfw.PRESS and yRana + 0.05 + 0.1 < 1:
        angulo = 0
        yRana = yRana + 0.007

    checar_colisiones()

def dibujarRana():
    global xRana
    global yRana

    #glScalef(1,1,1) #no se como se usa xd

    glPushMatrix()
    glTranslate(xRana, yRana, 0.0)
    glRotate(angulo, 0.0, 0.0, 1.0)
    glScalef(0.5,0.5,1) #aqui va xd
    glBegin(GL_POLYGON)
    #if colisionando == True:
        #glColor3f(1.0, 1.0, 1.0)
    #else:
        #glColor3f(0.513, 0.905, 0.180)

    glColor3f(0.513, 0.905, 0.180)
    glVertex3f(-0.03, 0.05, 0.0)
    glVertex3f(0.03, 0.05, 0.0)
    glVertex3f(0.03, -0.05, 0.0)
    glVertex3f(-0.03, -0.05, 0.0)

    glEnd()

    #Cara

    glBegin(GL_QUADS)
    glColor3f(0.513, 0.905, 0.180)
    glVertex3f(-0.02, 0.05, 0.0)
    glVertex3f(0.02, 0.05, 0.0)
    glVertex3f(0.02, 0.06, 0.0)
    glVertex3f(-0.02, 0.06, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(-0.03, 0.05, 0.0)
    glVertex3f(-0.02, 0.05, 0.0)
    glVertex3f(-0.02, 0.04, 0.0)
    glVertex3f(-0.03, 0.04, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.03, 0.05, 0.0)
    glVertex3f(0.02, 0.05, 0.0)
    glVertex3f(0.02, 0.04, 0.0)
    glVertex3f(0.03, 0.04, 0.0)
    glEnd()

    #Mano derecha

    glBegin(GL_QUADS)
    glColor3f(0.513, 0.905, 0.180)
    glVertex3f(0.03, 0.03, 0.0)
    glVertex3f(0.06, 0.03, 0.0)
    glVertex3f(0.06, 0.01, 0.0)
    glVertex3f(0.03, 0.01, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3f(0.05, 0.03, 0.0)
    glVertex3f(0.05, 0.04, 0.0)
    glVertex3f(0.06, 0.04, 0.0)
    glVertex3f(0.06, 0.03, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3f(0.06, 0.03, 0.0)
    glVertex3f(0.07, 0.03, 0.0)
    glVertex3f(0.07, 0.02, 0.0)
    glVertex3f(0.06, 0.02, 0.0)
    glEnd()

    #Mano izquierda

    glBegin(GL_QUADS)
    glVertex3f(-0.03, 0.03, 0.0)
    glVertex3f(-0.06, 0.03, 0.0)
    glVertex3f(-0.06, 0.01, 0.0)
    glVertex3f(-0.03, 0.01, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3f(-0.05, 0.03, 0.0)
    glVertex3f(-0.05, 0.04, 0.0)
    glVertex3f(-0.06, 0.04, 0.0)
    glVertex3f(-0.06, 0.03, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3f(-0.06, 0.03, 0.0)
    glVertex3f(-0.07, 0.03, 0.0)
    glVertex3f(-0.07, 0.02, 0.0)
    glVertex3f(-0.06, 0.02, 0.0)
    glEnd()

    #Pierna derecha

    glBegin(GL_QUADS)
    glVertex3f(0.03, -0.03, 0.0)
    glVertex3f(0.05, -0.03, 0.0)
    glVertex3f(0.05, -0.05, 0.0)
    glVertex3f(0.03, -0.05, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3f(0.04, -0.05, 0.0)
    glVertex3f(0.05, -0.05, 0.0)
    glVertex3f(0.05, -0.08, 0.0)
    glVertex3f(0.04, -0.08, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3f(0.05, -0.06, 0.0)
    glVertex3f(0.06, -0.06, 0.0)
    glVertex3f(0.06, -0.07, 0.0)
    glVertex3f(0.05, -0.07, 0.0)
    glEnd()

    #Pierna izquierda

    glBegin(GL_QUADS)
    glVertex3f(-0.03, -0.03, 0.0)
    glVertex3f(-0.05, -0.03, 0.0)
    glVertex3f(-0.05, -0.05, 0.0)
    glVertex3f(-0.03, -0.05, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3f(-0.04, -0.05, 0.0)
    glVertex3f(-0.05, -0.05, 0.0)
    glVertex3f(-0.05, -0.08, 0.0)
    glVertex3f(-0.04, -0.08, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3f(-0.05, -0.06, 0.0)
    glVertex3f(-0.06, -0.06, 0.0)
    glVertex3f(-0.06, -0.07, 0.0)
    glVertex3f(-0.05, -0.07, 0.0)
    glEnd()

    glPopMatrix()

def dibujarRanaSkin():

    #Cabeza
    glBegin(GL_QUADS)
    glColor3f(0.513, 0.905, 0.180)
    glVertex3f(-0.03, 0.06, 0.0)
    glVertex3f(0.03, 0.06, 0.0)
    glVertex3f(0.03, 0.02, 0.0)
    glVertex3f(-0.03, 0.02, 0.0)
    glEnd()
    #Cuerpo
    glBegin(GL_QUADS)
    glColor3f(0.513, 0.905, 0.180)
    glVertex3f(-0.04, 0.02, 0.0)
    glVertex3f(0.04, 0.02, 0.0)
    glVertex3f(0.04, -0.06, 0.0)
    glVertex3f(-0.04, -0.06, 0.0)
    glEnd()
    #Ojo1
    glBegin(GL_QUADS)
    glColor3f(0.513, 0.905, 0.180)
    glVertex3f(0.02, 0.04, 0.0)
    glVertex3f(0.05, 0.04, 0.0)
    glVertex3f(0.05, 0.07, 0.0)
    glVertex3f(0.02, 0.07, 0.0)
    glEnd()
    #Pupila
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.1, 0.0)
    glVertex3f(0.025, 0.055, 0.0)
    glVertex3f(0.045, 0.055, 0.0)
    glVertex3f(0.045, 0.065, 0.0)
    glVertex3f(0.025, 0.065, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.152, 0.952, 0.776)
    glVertex3f(0.025, 0.055, 0.0)
    glVertex3f(0.045, 0.055, 0.0)
    glVertex3f(0.045, 0.045, 0.0)
    glVertex3f(0.025, 0.045, 0.0)
    glEnd()

    #Ojo2
    glBegin(GL_QUADS)
    glColor3f(0.513, 0.905, 0.180)
    glVertex3f(-0.02, 0.04, 0.0)
    glVertex3f(-0.05, 0.04, 0.0)
    glVertex3f(-0.05, 0.07, 0.0)
    glVertex3f(-0.02, 0.07, 0.0)
    glEnd()

    #pupila2

    glBegin(GL_QUADS)
    glColor3f(0.0, 0.1, 0.0)
    glVertex3f(-0.025, 0.055, 0.0)
    glVertex3f(-0.045, 0.055, 0.0)
    glVertex3f(-0.045, 0.065, 0.0)
    glVertex3f(-0.025, 0.065, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.152, 0.952, 0.776)
    glVertex3f(-0.025, 0.055, 0.0)
    glVertex3f(-0.045, 0.055, 0.0)
    glVertex3f(-0.045, 0.045, 0.0)
    glVertex3f(-0.025, 0.045, 0.0)
    glEnd()

    #pata1
    glBegin(GL_QUADS)
    glColor3f(0.513, 0.905, 0.180)
    glVertex3f(-0.035, -0.06, 0.0)
    glVertex3f(-0.02, -0.06, 0.0)
    glVertex3f(-0.02, -0.08, 0.0)
    glVertex3f(-0.035, -0.08, 0.0)
    glEnd()

    #pata2
    glBegin(GL_QUADS)
    glColor3f(0.513, 0.905, 0.180)
    glVertex3f(0.035, -0.06, 0.0)
    glVertex3f(0.02, -0.06, 0.0)
    glVertex3f(0.02, -0.08, 0.0)
    glVertex3f(0.035, -0.08, 0.0)
    glEnd()

    #pata3
    glBegin(GL_QUADS)
    glColor3f(0.513, 0.905, 0.180)
    glVertex3f(0.04, 0.01, 0.0)
    glVertex3f(0.06, 0.01, 0.0)
    glVertex3f(0.06, -0.05, 0.0)
    glVertex3f(0.04, -0.05, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.513, 0.905, 0.180)
    glVertex3f(0.06, -0.05, 0.0)
    glVertex3f(0.08, -0.05, 0.0)
    glVertex3f(0.08, -0.07, 0.0)
    glVertex3f(0.06, -0.07, 0.0)
    glEnd()

    #pata4
    glBegin(GL_QUADS)
    glColor3f(0.513, 0.905, 0.180)
    glVertex3f(-0.04, 0.01, 0.0)
    glVertex3f(-0.06, 0.01, 0.0)
    glVertex3f(-0.06, -0.05, 0.0)
    glVertex3f(-0.04, -0.05, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.513, 0.905, 0.180)
    glVertex3f(-0.06, -0.05, 0.0)
    glVertex3f(-0.08, -0.05, 0.0)
    glVertex3f(-0.08, -0.07, 0.0)
    glVertex3f(-0.06, -0.07, 0.0)
    glEnd()

    #Boca
    glBegin(GL_QUADS)
    glColor3f(0.1, 0.0, 0.0)
    glVertex3f(-0.015, 0.01, 0.0)
    glVertex3f(0.015, 0.01, 0.0)
    glVertex3f(0.015, 0.00, 0.0)
    glVertex3f(-0.015, 0.00, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.1, 0.0, 0.0)
    glVertex3f(-0.015, 0.01, 0.0)
    glVertex3f(-0.025, 0.01, 0.0)
    glVertex3f(-0.025, 0.02, 0.0)
    glVertex3f(-0.015, 0.02, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.1, 0.0, 0.0)
    glVertex3f(0.015, 0.01, 0.0)
    glVertex3f(0.025, 0.01, 0.0)
    glVertex3f(0.025, 0.02, 0.0)
    glVertex3f(0.015, 0.02, 0.0)
    glEnd()

def dibujarTronco():

    glBegin(GL_QUADS)
    glColor3f(0.588, 0.427, 0.235)
    glVertex3f(-0.16, 0.08, 0.0)
    glVertex3f(0.16, 0.08, 0.0)
    glVertex3f(0.16, -0.08, 0.0)
    glVertex3f(-0.16, -0.08, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.07 - 0.14, sin(angulo) * 0.08 + 0.0, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.815, 0.615, 0.372)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.06 + 0.15, sin(angulo) * 0.08 + 0.0, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.588, 0.427, 0.235)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.04 + 0.15, sin(angulo) * 0.06 + 0.0, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.815, 0.615, 0.372)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.02 + 0.15, sin(angulo) * 0.04 + 0.0, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.588, 0.427, 0.235)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.01 + 0.15, sin(angulo) * 0.02 + 0.0, 0.0)
    glEnd()

def dibujarTronco1():
    global xTronco1
    global yTronco1

    glPushMatrix()
    glTranslate(xTronco1, yTronco1, 0.0)
    glScalef(0.7,0.7,1) 
    dibujarTronco()
    glPopMatrix()

    if xTronco1 > -1.3:
        xTronco1 = xTronco1 - 0.003
    else:
        xTronco1 = 1.2

    if xRana + 0.05 > xTronco1 - 0.11 and xRana - 0.05 < xTronco1 + 0.13 and yRana + 0.05 > yTronco1 - 0.05 and yRana - 0.05 < yTronco1 + 0.05:
        vidasRana()
        resetPosition()

def dibujarTronco2():
    global xTronco2
    global yTronco2

    glPushMatrix()
    glTranslate(xTronco2, yTronco2, 0.0)
    glScalef(0.7,0.7,1) 
    dibujarTronco()
    glPopMatrix()

    if xTronco2 > -1.3:
        xTronco2 = xTronco2 - 0.003
    else:
        xTronco2 = 1.2

    if xRana + 0.05 > xTronco2 - 0.11 and xRana - 0.05 < xTronco2 + 0.13 and yRana + 0.05 > yTronco2 - 0.05 and yRana - 0.05 < yTronco2 + 0.05:
        vidasRana()
        resetPosition()

def dibujarTronco3():
    global xTronco3
    global yTronco3

    glPushMatrix()
    glTranslate(xTronco3, yTronco3, 0.0)
    glScalef(0.7,0.7,1) 
    dibujarTronco()
    glPopMatrix()

    if xTronco3 > -1.3:
        xTronco3 = xTronco3 - 0.003
    else:
        xTronco3 = 1.2
    
    if xRana + 0.05 > xTronco3 - 0.11 and xRana - 0.05 < xTronco3 + 0.13 and yRana + 0.05 > yTronco3 - 0.05 and yRana - 0.05 < yTronco3 + 0.05:
        vidasRana()
        resetPosition()

def dibujarTronco4():
    global xTronco4
    global yTronco4

    glPushMatrix()
    glTranslate(xTronco4, yTronco4, 0.0)
    glScalef(0.7,1.1,1) 
    dibujarTronco()
    glPopMatrix()

    if xTronco4 > -1.3:
        xTronco4 = xTronco4 - 0.003
    else:
        xTronco4 = 1.2

    # Cuando la rana colisione con el tronco 1 se convertira en True, la rana muera y regresara al punto de partida
    if xRana + 0.05 > xTronco4 - 0.11 and xRana - 0.05 < xTronco4 + 0.13 and yRana + 0.05 > yTronco4 - 0.05 and yRana - 0.05 < yTronco4 + 0.05:
        vidasRana()
        resetPosition()

def dibujarTronco5():
    global xTronco5
    global yTronco5

    glPushMatrix()
    glTranslate(xTronco5, yTronco5, 0.0)
    glScalef(0.7,1.1,1) 
    dibujarTronco()
    glPopMatrix()

    if xTronco5 > -1.3:
        xTronco5 = xTronco5 - 0.003
    else:
        xTronco5 = 1.2

    # Cuando la rana colisione con el tronco 1 se convertira en True, la rana muera y regresara al punto de partida
    if xRana + 0.05 > xTronco5 - 0.11 and xRana - 0.05 < xTronco5 + 0.13 and yRana + 0.05 > yTronco5 - 0.05 and yRana - 0.05 < yTronco5 + 0.05:
        vidasRana()
        resetPosition()

def dibujarTronco6():
    global xTronco6
    global yTronco6

    glPushMatrix()
    glTranslate(xTronco6, yTronco6, 0.0)
    glScalef(0.7,1.1,1) 
    dibujarTronco()
    glPopMatrix()

    if xTronco6 > -1.3:
        xTronco6 = xTronco6 - 0.003
    else:
        xTronco6 = 1.2

    if xRana + 0.05 > xTronco6 - 0.11 and xRana - 0.05 < xTronco6 + 0.13 and yRana + 0.05 > yTronco6 - 0.05 and yRana - 0.05 < yTronco6 + 0.05:
        resetPosition()
        vidasRana()

def dibujarAllTronco():
    dibujarTronco1()
    dibujarTronco2()
    dibujarTronco3()
    dibujarTronco4()
    dibujarTronco5()
    dibujarTronco6()

def dibujarCarro():
    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-0.14, 0.0, 0.0)
    glVertex3f(-0.08, 0.08, 0.0)
    glVertex3f(0.14, 0.08, 0.0)
    glVertex3f(0.14, -0.08, 0.0)
    glVertex3f(-0.08, -0.08, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.1, 0.0, 0.0)
    glVertex3f(-0.06, 0.08, 0.0)
    glVertex3f(-0.01, 0.08, 0.0)
    glVertex3f(-0.01, 0.10, 0.0)
    glVertex3f(-0.06, 0.10, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.1, 0.0, 0.0)
    glVertex3f(-0.06, -0.08, 0.0)
    glVertex3f(-0.01, -0.08, 0.0)
    glVertex3f(-0.01, -0.10, 0.0)
    glVertex3f(-0.06, -0.10, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.1, 0.0, 0.0)
    glVertex3f(0.05, -0.08, 0.0)
    glVertex3f(0.12, -0.08, 0.0)
    glVertex3f(0.12, -0.10, 0.0)
    glVertex3f(0.05, -0.10, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.1, 0.0, 0.0)
    glVertex3f(0.05, 0.08, 0.0)
    glVertex3f(0.12, 0.08, 0.0)
    glVertex3f(0.12, 0.10, 0.0)
    glVertex3f(0.05, 0.10, 0.0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0.537, 0.788, 0.945)
    glVertex3f(-0.085, 0.06, 0.0)
    glVertex3f(-0.085, -0.06, 0.0)
    glVertex3f(-0.125, 0.0, 0.0)
    glEnd()

def dibujarCarro_2():

    glBegin(GL_POLYGON)
    glColor3f(0.952, 0.976, 0.427)
    #glVertex3f(-0.14, 0.0, 0.0)
    glVertex3f(-0.08, 0.08, 0.0)
    glVertex3f(0.14, 0.08, 0.0)
    glVertex3f(0.14, -0.08, 0.0)
    glVertex3f(-0.08, -0.08, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.1, 0.0, 0.0)
    glVertex3f(0.05, 0.08, 0.0)
    glVertex3f(0.10, 0.08, 0.0)
    glVertex3f(0.10, 0.10, 0.0)
    glVertex3f(0.05, 0.10, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.1, 0.0, 0.0)
    glVertex3f(0.05, -0.08, 0.0)
    glVertex3f(0.10, -0.08, 0.0)
    glVertex3f(0.10, -0.10, 0.0)
    glVertex3f(0.05, -0.10, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.1, 0.0, 0.0)
    glVertex3f(-0.06, -0.08, 0.0)
    glVertex3f(-0.01, -0.08, 0.0)
    glVertex3f(-0.01, -0.10, 0.0)
    glVertex3f(-0.06, -0.10, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.1, 0.0, 0.0)
    glVertex3f(-0.06, 0.08, 0.0)
    glVertex3f(-0.01, 0.08, 0.0)
    glVertex3f(-0.01, 0.10, 0.0)
    glVertex3f(-0.06, 0.10, 0.0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0.5, 0.7, 0.9)
    glVertex3f(0.07, 0.06, 0.0)
    glVertex3f(0.07, -0.06, 0.0)
    glVertex3f(0.12, 0.0, 0.0)
    glEnd()

def dibujarCarro1():
    global xCarro1
    global yCarro1

    glPushMatrix()
    glTranslate(xCarro1, yCarro1, 0.0)
    glScalef(0.5,0.5,1)
    dibujarCarro()
    glPopMatrix()

    if xCarro1 > -1.3:
        xCarro1 = xCarro1 - 0.004
    else:
        xCarro1 = 1.2

    if xRana + 0.05 > xCarro1 - 0.05 and xRana - 0.05 < xCarro1 + 0.05 and yRana + 0.05 > yCarro1 - 0.05 and yRana - 0.05 < yCarro1 + 0.05:
        resetPosition()
        vidasRana()

def dibujarCarro2():
    global xCarro2
    global yCarro2

    glPushMatrix()
    glTranslate(xCarro2, yCarro2, 0.0)
    glScalef(0.5,0.5,1)
    dibujarCarro()
    glPopMatrix()

    if xCarro2 > -1.3:
        xCarro2 = xCarro2 - 0.004
    else:
        xCarro2 = 1.2
    
    if xRana + 0.05 > xCarro2 - 0.05 and xRana - 0.05 < xCarro2 + 0.05 and yRana + 0.05 > yCarro2 - 0.05 and yRana - 0.05 < yCarro2 + 0.05:
        resetPosition()
        vidasRana()

def dibujarCarro3():
    global xCarro3
    global yCarro3

    glPushMatrix()
    glTranslate(xCarro3, yCarro3, 0.0)
    glScalef(0.5,0.5,1)
    dibujarCarro()
    glPopMatrix()

    if xCarro3 > -1.3:
        xCarro3 = xCarro3 - 0.004
    else:
        xCarro3 = 1.2

    if xRana + 0.05 > xCarro3 - 0.05 and xRana - 0.05 < xCarro3 + 0.05 and yRana + 0.05 > yCarro3 - 0.05 and yRana - 0.05 < yCarro3 + 0.05:
        resetPosition()
        vidasRana()

def dibujarCarro4():
    global xCarro4
    global yCarro4

    glPushMatrix()
    glTranslate(xCarro4, yCarro4, 0.0)
    glScalef(0.5,0.5,1)
    dibujarCarro_2()
    glPopMatrix()

    if xCarro4 < 1.3:
        xCarro4 = xCarro4 + 0.01
    else:
        xCarro4 = -1.2

    if xRana + 0.05 > xCarro4 - 0.05 and xRana - 0.05 < xCarro4 + 0.05 and yRana + 0.05 > yCarro4 - 0.05 and yRana - 0.05 < yCarro4 + 0.05:
        resetPosition()
        vidasRana()

def dibujarAllCarros():
    dibujarCarro1()
    dibujarCarro2()
    dibujarCarro3()
    dibujarCarro4()

def dibujarCamion():
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-0.08, 0.08, 0.0)
    glVertex3f(0.18, 0.08, 0.0)
    glVertex3f(0.18, -0.08, 0.0)
    glVertex3f(-0.08, -0.08, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.1, 0.0, 0.0)
    glVertex3f(-0.06, 0.08, 0.0)
    glVertex3f(-0.01, 0.08, 0.0)
    glVertex3f(-0.01, 0.10, 0.0)
    glVertex3f(-0.06, 0.10, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.1, 0.0, 0.0)
    glVertex3f(-0.06, -0.08, 0.0)
    glVertex3f(-0.01, -0.08, 0.0)
    glVertex3f(-0.01, -0.10, 0.0)
    glVertex3f(-0.06, -0.10, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.1, 0.0, 0.0)
    glVertex3f(0.07+0.04, -0.08, 0.0)
    glVertex3f(0.12+0.04, -0.08, 0.0)
    glVertex3f(0.12+0.04, -0.10, 0.0)
    glVertex3f(0.07+0.04, -0.10, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.1, 0.0, 0.0)
    glVertex3f(0.07+0.04, 0.08, 0.0)
    glVertex3f(0.12+0.04, 0.08, 0.0)
    glVertex3f(0.12+0.04, 0.10, 0.0)
    glVertex3f(0.07+0.04, 0.10, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.910, 0.0, 0.0)
    glVertex3f(-0.08, 0.03, 0.0)
    glVertex3f(-0.098, 0.03, 0.0)
    glVertex3f(-0.098, -0.03, 0.0)
    glVertex3f(-0.08, -0.03, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-0.098, 0.08, 0.0)
    glVertex3f(-0.18, 0.08, 0.0)
    glVertex3f(-0.18, -0.08, 0.0)
    glVertex3f(-0.098, -0.08, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.1, 0.0, 0.0)
    glVertex3f(-0.15, 0.08, 0.0)
    glVertex3f(-0.11, 0.08, 0.0)
    glVertex3f(-0.11, 0.10, 0.0)
    glVertex3f(-0.15, 0.10, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.1, 0.0, 0.0)
    glVertex3f(-0.15, -0.08, 0.0)
    glVertex3f(-0.11, -0.08, 0.0)
    glVertex3f(-0.11, -0.10, 0.0)
    glVertex3f(-0.15, -0.10, 0.0)
    glEnd()

def dibujarCamion_2():

    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-0.08, 0.08, 0.0)
    glVertex3f(0.18, 0.08, 0.0)
    glVertex3f(0.18, -0.08, 0.0)
    glVertex3f(-0.08, -0.08, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.1, 0.0, 0.0)
    glVertex3f(-0.06, 0.08, 0.0)
    glVertex3f(-0.01, 0.08, 0.0)
    glVertex3f(-0.01, 0.10, 0.0)
    glVertex3f(-0.06, 0.10, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.1, 0.0, 0.0)
    glVertex3f(-0.06, -0.08, 0.0)
    glVertex3f(-0.01, -0.08, 0.0)
    glVertex3f(-0.01, -0.10, 0.0)
    glVertex3f(-0.06, -0.10, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.1, 0.0, 0.0)
    glVertex3f(0.07+0.04, -0.08, 0.0)
    glVertex3f(0.12+0.04, -0.08, 0.0)
    glVertex3f(0.12+0.04, -0.10, 0.0)
    glVertex3f(0.07+0.04, -0.10, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.1, 0.0, 0.0)
    glVertex3f(0.07+0.04, 0.08, 0.0)
    glVertex3f(0.12+0.04, 0.08, 0.0)
    glVertex3f(0.12+0.04, 0.10, 0.0)
    glVertex3f(0.07+0.04, 0.10, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.910, 0.0, 0.0)
    glVertex3f(0.08+0.10, 0.03, 0.0)
    glVertex3f(0.098+0.10, 0.03, 0.0)
    glVertex3f(0.098+0.10, -0.03, 0.0)
    glVertex3f(0.08+0.10, -0.03, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.098+0.10, 0.08, 0.0)
    glVertex3f(0.18+0.10, 0.08, 0.0)
    glVertex3f(0.18+0.10, -0.08, 0.0)
    glVertex3f(0.098+0.10, -0.08, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.1, 0.0, 0.0)
    glVertex3f(0.15+0.10, 0.08, 0.0)
    glVertex3f(0.11+0.10, 0.08, 0.0)
    glVertex3f(0.11+0.10, 0.10, 0.0)
    glVertex3f(0.15+0.10, 0.10, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.1, 0.0, 0.0)
    glVertex3f(0.15+0.10, -0.08, 0.0)
    glVertex3f(0.11+0.10, -0.08, 0.0)
    glVertex3f(0.11+0.10, -0.10, 0.0)
    glVertex3f(0.15+0.10, -0.10, 0.0)
    glEnd()

def dibujarCamion1():
    global xCamion1
    global yCamion1
    
    glPushMatrix()
    glTranslate(xCamion1, yCamion1, 0.0)
    glScalef(0.5,0.8,1)
    dibujarCamion()
    glPopMatrix()

    if xCamion1 > -1.3:
        xCamion1 = xCamion1 - 0.002
    else:
        xCamion1 = 1.2

    if xRana + 0.05 > xCamion1 - 0.055 and xRana - 0.05 < xCamion1 + 0.055 and yRana + 0.05 > yCamion1 - 0.05 and yRana - 0.05 < yCamion1 + 0.05:
        resetPosition()
        vidasRana()

def dibujarCamion2():
    global xCamion2
    global yCamion2

    glPushMatrix()
    glTranslate(xCamion2, yCamion2, 0.0)
    glScalef(0.5,0.8,1)
    dibujarCamion()
    glPopMatrix()

    if xCamion2 > -1.3:
        xCamion2 = xCamion2 - 0.002
    else:
        xCamion2 = 1.2

    if xRana + 0.05 > xCamion2 - 0.055 and xRana - 0.05 < xCamion2 + 0.055 and yRana + 0.05 > yCamion2 - 0.05 and yRana - 0.05 < yCamion2 + 0.05:
        resetPosition()
        vidasRana()

def dibujarCamion3():
    global xCamion3
    global yCamion3
    
    glPushMatrix()
    glTranslate(xCamion3, yCamion3, 0.0)
    glScalef(0.5,0.8,1)
    dibujarCamion_2()
    
    glPopMatrix()

    if xCamion3 < 1.3:
        xCamion3 = xCamion3 + 0.002
    else:
        xCamion3 = -1.2
    if xRana + 0.05 > xCamion3 - 0.04 and xRana - 0.05 < xCamion3 + 0.12 and yRana + 0.05 > yCamion3 - 0.05 and yRana - 0.05 < yCamion3 + 0.05:
        resetPosition()
        vidasRana()

def dibujarCamion4():
    global xCamion4
    global yCamion4
    
    glPushMatrix()
    glTranslate(xCamion4, yCamion4, 0.0)
    glScalef(0.5,0.8,1)
    dibujarCamion_2()
    
    glPopMatrix()

    if xCamion4 < 1.3:
        xCamion4 = xCamion4 + 0.002
    else:
        xCamion4 = -1.2
    if xRana + 0.05 > xCamion4 - 0.04 and xRana - 0.05 < xCamion4 + 0.12 and yRana + 0.05 > yCamion4 - 0.05 and yRana - 0.05 < yCamion4 + 0.05:
        resetPosition()
        vidasRana()

def dibujarAllCamiones():
    dibujarCamion1()
    dibujarCamion2()
    dibujarCamion3()
    dibujarCamion4()

def dibujarTortuga():

    #pata delantera izq
    glPushMatrix()
    glRotatef(-44, 0, 0, 1)
    glBegin(GL_POLYGON)
    glColor3f(0.411, 0.662, 0.090)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.02 - 0.10, sin(angulo) * 0.04 - 0.18 , 0.0)
    glEnd()
    glPopMatrix()

    #pata delantera der
    glPushMatrix()
    glRotatef(44, 0, 0, 1)
    glBegin(GL_POLYGON)
    glColor3f(0.411, 0.662, 0.090)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.02 - 0.10, sin(angulo) * 0.04 + 0.18 , 0.0)
    glEnd()
    glPopMatrix()

    #pata trasera der
    glPushMatrix()
    glRotatef(-44, 0, 0, 1)
    glBegin(GL_POLYGON)
    glColor3f(0.411, 0.662, 0.090)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.02 - 0.09, sin(angulo) * 0.04 - 0.02, 0.0)
    glEnd()
    glPopMatrix()

    #pata trasera izq
    glPushMatrix()
    glRotatef(44, 0, 0, 1)
    glBegin(GL_POLYGON)
    glColor3f(0.411, 0.662, 0.090)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.02 - 0.08, sin(angulo) * 0.04 + 0.02, 0.0)
    glEnd()
    glPopMatrix()

    #cabeza

    glBegin(GL_POLYGON)
    glColor3f(0.411, 0.662, 0.090)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.06 - 0.23, sin(angulo) * 0.03 + 0.0, 0.0)
    glEnd()

    #caparazón

    glBegin(GL_POLYGON)
    glColor3f(0.894, 0.376, 0.078)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.10 - 0.15, sin(angulo) * 0.07 + 0.0, 0.0)
    glEnd()

def dibujarHilera2Tortuga():
    glPushMatrix()
    glTranslate(0.0, 0.0, 0.0)
    glScalef(0.6,0.8,1)
    dibujarTortuga()
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.2, 0.0, 0.0)
    glScalef(0.6,0.8,1)
    dibujarTortuga()
    glPopMatrix()

def dibujarHilera3Tortuga():
    glPushMatrix()
    glTranslate(0.0, 0.0, 0.0)
    glScalef(0.6,0.8,1)
    dibujarTortuga()
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.2, 0.0, 0.0)
    glScalef(0.6,0.8,1)
    dibujarTortuga()
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.4, 0.0, 0.0)
    glScalef(0.6,0.8,1)
    dibujarTortuga()
    glPopMatrix()

def dibujarTortuga1():
    global xTortuga1
    global yTortuga1

    glPushMatrix()
    glTranslate(xTortuga1, yTortuga1, 0.0)
    glRotate(180, 0.0, 0.0, 1.0)
    glScalef(0.6,0.8,1)
    dibujarHilera3Tortuga()
    glPopMatrix()

    if xTortuga1 < 1.3:
        xTortuga1 = xTortuga1 + 0.004
    else:
        xTortuga1 = -1.2

    if xRana + 0.05 > xTortuga1 - 0.2 and xRana - 0.05 < xTortuga1 + 0.05 and yRana + 0.05 > yTortuga1 - 0.05 and yRana - 0.05 < yTortuga1 + 0.05:
        vidasRana()
        resetPosition()

def dibujarTortuga2():
    global xTortuga2
    global yTortuga2

    glPushMatrix()
    glTranslate(xTortuga2, yTortuga2, 0.0)
    glRotate(180, 0.0, 0.0, 1.0)
    glScalef(0.6,0.8,1)
    dibujarHilera2Tortuga()
    glPopMatrix()

    if xTortuga2 < 1.3:
        xTortuga2 = xTortuga2 + 0.004
    else:
        xTortuga2 = -1.2

    if xRana + 0.05 > xTortuga2 - 0.1 and xRana - 0.05 < xTortuga2 + 0.08 and yRana + 0.05 > yTortuga2 - 0.05 and yRana - 0.05 < yTortuga2 + 0.05:
        vidasRana()
        resetPosition()

def dibujarTortuga3():
    global xTortuga3
    global yTortuga3

    glPushMatrix()
    glTranslate(xTortuga3, yTortuga3, 0.0)
    glRotate(180, 0.0, 0.0, 1.0)
    glScalef(0.6,0.8,1)
    dibujarHilera2Tortuga()
    glPopMatrix()

    if xTortuga3 < 1.3:
        xTortuga3 = xTortuga3 + 0.004
    else:
        xTortuga3 = -1.2

    # Cuando la rana colisione con el carro 1 se convertira en True, la rana muera y regresara al punto de partida
    if xRana + 0.05 > xTortuga3 - 0.1 and xRana - 0.05 < xTortuga3 + 0.08 and yRana + 0.05 > yTortuga3 - 0.05 and yRana - 0.05 < yTortuga3 + 0.05:
        vidasRana()
        resetPosition()

def dibujarAllTortuga():
    dibujarTortuga1()
    dibujarTortuga2()
    dibujarTortuga3()

def dibujarNenufar():

    glPushMatrix()
    glRotatef(-44, 0, 0, 1)
    glBegin(GL_POLYGON)
    glColor3f(0.258, 0.6, 0.109)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.08 + 0.0, sin(angulo) * 0.05 + 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glRotatef(44, 0, 0, 1)
    glBegin(GL_POLYGON)
    glColor3f(0.258, 0.6, 0.109)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.08 + 0.0, sin(angulo) * 0.05 + 0.0, 0.0)
    glEnd()
    glPopMatrix()

def dibujarHilera2Nenufar():
    glPushMatrix()
    glTranslate(0.0, 0.0, 0.0)
    glScalef(0.6,0.8,1)
    dibujarNenufar()
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.1, 0.0, 0.0)
    glScalef(0.6,0.8,1)
    dibujarNenufar()
    glPopMatrix()

def dibujarHilera3Nenufar():
    glPushMatrix()
    glTranslate(0.0, 0.0, 0.0)
    glScalef(0.6,0.8,1)
    dibujarNenufar()
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.1, 0.0, 0.0)
    glScalef(0.6,0.8,1)
    dibujarNenufar()
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.2, 0.0, 0.0)
    glScalef(0.6,0.8,1)
    dibujarNenufar()
    glPopMatrix()

def dibujarNenufar1():
    global xNenufar1
    global yNenufar1

    glPushMatrix()
    glTranslate(xNenufar1, yNenufar1, 0.0)
    glRotate(180, 0.0, 0.0, 1.0)
    glScalef(1.0,0.8,1)
    dibujarHilera2Nenufar()
    glPopMatrix()

    if xNenufar1 < 1.3:
        xNenufar1 = xNenufar1 + 0.004
    else:
        xNenufar1 = -1.2

    # Cuando la rana colisione con el carro 1 se convertira en True, la rana muera y regresara al punto de partida
    if xRana + 0.05 > xNenufar1 - 0.1 and xRana - 0.05 < xNenufar1 + 0.08 and yRana + 0.05 > yNenufar1 - 0.05 and yRana - 0.05 < yNenufar1 + 0.05:
        vidasRana()
        resetPosition()

def dibujarNenufar2():
    global xNenufar2
    global yNenufar2

    glPushMatrix()
    glTranslate(xNenufar2, yNenufar2, 0.0)
    glRotate(180, 0.0, 0.0, 1.0)
    glScalef(0.6,0.8,1)
    dibujarHilera3Nenufar()
    glPopMatrix()

    if xNenufar2 < 1.3:
        xNenufar2 = xNenufar2 + 0.004
    else:
        xNenufar2 = -1.2

    # Cuando la rana colisione con el carro 1 se convertira en True, la rana muera y regresara al punto de partida
    if xRana + 0.05 > xNenufar2 - 0.2 and xRana - 0.05 < xNenufar2 + 0.05 and yRana + 0.05 > yNenufar2 - 0.05 and yRana - 0.05 < yNenufar2 + 0.05:
        vidasRana()
        resetPosition()

def dibujarNenufar3():
    global xNenufar3
    global yNenufar3

    glPushMatrix()
    glTranslate(xNenufar3, yNenufar3, 0.0)
    glRotate(180, 0.0, 0.0, 1.0)
    glScalef(1.0,0.8,1)
    dibujarHilera2Nenufar()
    glPopMatrix()

    if xNenufar3 < 1.3:
        xNenufar3 = xNenufar3 + 0.004
    else:
        xNenufar3 = -1.2

    # Cuando la rana colisione con el carro 1 se convertira en True, la rana muera y regresara al punto de partida
    if xRana + 0.05 > xNenufar3 - 0.1 and xRana - 0.05 < xNenufar3 + 0.08 and yRana + 0.05 > yNenufar3 - 0.05 and yRana - 0.05 < yNenufar3 + 0.05:
        vidasRana()
        resetPosition()

def dibujarAllNenufar():
    dibujarNenufar1()
    dibujarNenufar2()
    dibujarNenufar3()

def dibujarMosca():
    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.1, 0.090)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.016 - 0.01, sin(angulo) * 0.016 + 0.0, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.1, 0.090)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.02 + 0.01, sin(angulo) * 0.02 + 0.0, 0.0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-0.01, 0.00, 0.0)
    glVertex3f(0.04, 0.06, 0.0)
    glVertex3f(0.04, 0.02, 0.0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-0.01, 0.00, 0.0)
    glVertex3f(0.04, -0.06, 0.0)
    glVertex3f(0.04, -0.02, 0.0)
    glEnd()

def dibujarMosca1():
    global colisionandoMosca1
    global xMosca1
    global yMosca1

    glPushMatrix()
    glTranslate(xMosca1, yMosca1, 0.0)
    # Si colisionando es False se creara la mosca, pero si es True se creara la rana para sustituirla
    if colisionandoMosca1 == False:
        dibujarMosca()

    else: 
        glScalef(0.7,0.7,1)
        dibujarRanaSkin()
    glPopMatrix()

def dibujarMosca2():
    global colisionandoMosca2
    global xMosca2
    global yMosca2

    glPushMatrix()
    glTranslate(xMosca2, yMosca2, 0.0)
    # Si colisionando es False se creara la mosca, pero si es True se creara la rana para sustituirla
    if colisionandoMosca2 == False:
        dibujarMosca()
    else:
        glScalef(0.7,0.7,1)
        dibujarRanaSkin()
    glPopMatrix()

def dibujarMosca3():
    global colisionandoMosca3
    global xMosca3
    global yMosca3

    glPushMatrix()
    glTranslate(xMosca3, yMosca3, 0.0)
    # Si colisionando es False se creara la mosca, pero si es True se creara la rana para sustituirla
    if colisionandoMosca3 == False:
        dibujarMosca()
    else:
        glScalef(0.7,0.7,1)
        dibujarRanaSkin()
    glPopMatrix()

def dibujarMosca4():
    global colisionandoMosca4
    global xMosca4
    global yMosca4

    glPushMatrix()
    glTranslate(xMosca4, yMosca4, 0.0)
    # Si colisionando es False se creara la mosca, pero si es True se creara la rana para sustituirla
    if colisionandoMosca4 == False:
        dibujarMosca()
    else:
        glScalef(0.7,0.7,1)
        dibujarRanaSkin()    
    glPopMatrix()

def dibujarAllMoscas():
    dibujarMosca1()
    dibujarMosca2()
    dibujarMosca3()
    dibujarMosca4()

def dibujarCesped():

    glBegin(GL_QUADS)
    glColor3f(0.352, 0.137, 0.501)
    glVertex3f(-1.0, -0.73, 0.0)
    glVertex3f(1.0, -0.73, 0.0)
    glVertex3f(1.0, -1.0, 0.0)
    glVertex3f(-1.0, -1.0, 0.0)
    glEnd()

def dibujarCamino():

    glBegin(GL_QUADS)
    #glColor3f(0.674, 0.674, 0.674)
    glColor3f(0.35, 0.35, 0.35)
    glVertex3f(-1.0, -0.09, 0.0)
    glVertex3f(1.0, -0.09, 0.0)
    glVertex3f(1.0, -0.73, 0.0)
    glVertex3f(-1.0, -0.73, 0.0)
    glEnd()

def dibujarCesped2():

    glBegin(GL_QUADS)
    glColor3f(0.658, 0.549, 0.341)
    glVertex3f(-1.0, -0.09, 0.0)
    glVertex3f(1.0, -0.09, 0.0)
    glVertex3f(1.0, 0.04, 0.0)
    glVertex3f(-1.0, 0.04, 0.0)
    glEnd()

def dibujarParteArriba():

    glBegin(GL_QUADS)
    glColor3f(0.411, 0.662, 0.090)
    #glColor3f(0.588, 0.427, 0.235)
    glVertex3f(-1.0, 1.0, 0.0)
    glVertex3f(-0.9, 1.0, 0.0)
    glVertex3f(-0.9, 0.78, 0.0)
    glVertex3f(-1.0, 0.78, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.411, 0.662, 0.090)
    glVertex3f(1.0, 1.0, 0.0)
    glVertex3f(0.88, 1.0, 0.0)
    glVertex3f(0.88, 0.78, 0.0)
    glVertex3f(1.0, 0.78, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.411, 0.662, 0.090)
    glVertex3f(1.0, 1.0, 0.0)
    glVertex3f(-1.0, 1.0, 0.0)
    glVertex3f(-1.0, 0.95, 0.0)
    glVertex3f(1.0, 0.95, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.411, 0.662, 0.090)
    glVertex3f(-0.68, 1.0, 0.0)
    glVertex3f(-0.4, 1.0, 0.0)
    glVertex3f(-0.4, 0.78, 0.0)
    glVertex3f(-0.68, 0.78, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.411, 0.662, 0.090)
    glVertex3f(0.68, 1.0, 0.0)
    glVertex3f(0.4, 1.0, 0.0)
    glVertex3f(0.4, 0.78, 0.0)
    glVertex3f(0.68, 0.78, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.411, 0.662, 0.090)
    glVertex3f(0.19, 1.0, 0.0)
    glVertex3f(-0.2, 1.0, 0.0)
    glVertex3f(-0.2, 0.78, 0.0)
    glVertex3f(0.19, 0.78, 0.0)
    glEnd()

def dibujarCaraRana():
    #Cabeza
    glBegin(GL_QUADS)
    glColor3f(0.513, 0.905, 0.180)
    glVertex3f(-0.03, 0.06, 0.0)
    glVertex3f(0.03, 0.06, 0.0)
    glVertex3f(0.03, 0.0, 0.0)
    glVertex3f(-0.03, 0.0, 0.0)
    glEnd()

    #Ojo1
    glBegin(GL_QUADS)
    glColor3f(0.513, 0.905, 0.180)
    glVertex3f(0.02, 0.04, 0.0)
    glVertex3f(0.05, 0.04, 0.0)
    glVertex3f(0.05, 0.07, 0.0)
    glVertex3f(0.02, 0.07, 0.0)
    glEnd()
    #Pupila
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.1, 0.0)
    glVertex3f(0.025, 0.055, 0.0)
    glVertex3f(0.045, 0.055, 0.0)
    glVertex3f(0.045, 0.065, 0.0)
    glVertex3f(0.025, 0.065, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.152, 0.952, 0.776)
    glVertex3f(0.025, 0.055, 0.0)
    glVertex3f(0.045, 0.055, 0.0)
    glVertex3f(0.045, 0.045, 0.0)
    glVertex3f(0.025, 0.045, 0.0)
    glEnd()

    #Ojo2
    glBegin(GL_QUADS)
    glColor3f(0.513, 0.905, 0.180)
    glVertex3f(-0.02, 0.04, 0.0)
    glVertex3f(-0.05, 0.04, 0.0)
    glVertex3f(-0.05, 0.07, 0.0)
    glVertex3f(-0.02, 0.07, 0.0)
    glEnd()

    #pupila2

    glBegin(GL_QUADS)
    glColor3f(0.0, 0.1, 0.0)
    glVertex3f(-0.025, 0.055, 0.0)
    glVertex3f(-0.045, 0.055, 0.0)
    glVertex3f(-0.045, 0.065, 0.0)
    glVertex3f(-0.025, 0.065, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.152, 0.952, 0.776)
    glVertex3f(-0.025, 0.055, 0.0)
    glVertex3f(-0.045, 0.055, 0.0)
    glVertex3f(-0.045, 0.045, 0.0)
    glVertex3f(-0.025, 0.045, 0.0)
    glEnd()

    #Boca
    glBegin(GL_QUADS)
    glColor3f(0.1, 0.0, 0.0)
    glVertex3f(-0.015, 0.02, 0.0)
    glVertex3f(0.015, 0.02, 0.0)
    glVertex3f(0.015, 0.01, 0.0)
    glVertex3f(-0.015, 0.01, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.1, 0.0, 0.0)
    glVertex3f(-0.015, 0.02, 0.0)
    glVertex3f(-0.025, 0.02, 0.0)
    glVertex3f(-0.025, 0.03, 0.0)
    glVertex3f(-0.015, 0.03, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.1, 0.0, 0.0)
    glVertex3f(0.015, 0.02, 0.0)
    glVertex3f(0.025, 0.02, 0.0)
    glVertex3f(0.025, 0.03, 0.0)
    glVertex3f(0.015, 0.03, 0.0)
    glEnd()

def dibujarHilera2Vidas():
    glPushMatrix()
    glTranslate(0.0, 0.0, 0.0)
    glScalef(0.6,0.8,1)
    dibujarCaraRana()
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.1, 0.0, 0.0)
    glScalef(0.6,0.8,1)
    dibujarCaraRana()
    glPopMatrix()

def dibujarHilera3Vidas():
    glPushMatrix()
    glTranslate(0.0, 0.0, 0.0)
    glScalef(0.6,0.8,1)
    dibujarCaraRana()
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.1, 0.0, 0.0)
    glScalef(0.6,0.8,1)
    dibujarCaraRana()
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.2, 0.0, 0.0)
    glScalef(0.6,0.8,1)
    dibujarCaraRana()
    glPopMatrix()

def dibujarVidas():
    global vidasdeRana
    global xVidas
    global yVidas

    glPushMatrix()
    glTranslate(xVidas, yVidas, 0.0)
    # Si colisionando es False se creara la mosca, pero si es True se creara la rana para sustituirla
    if vidasdeRana == 3:
        dibujarHilera3Vidas()
    elif vidasdeRana == 2:
        dibujarHilera2Vidas()
    elif vidasdeRana == 1:
        glPushMatrix()
        glTranslate(0.0, 0.0, 0.0)
        glScalef(0.6,0.8,1)
        dibujarCaraRana()
        glPopMatrix()

    glPopMatrix()

def dibujarFlor():

    glPushMatrix()

    glTranslatef(0.0, 0.885, 0.0)

    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.741, 0.988)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.04 + 0.065, sin(angulo) * 0.02 + 0.0, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.741, 0.988)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.04 - 0.065, sin(angulo) * 0.02 + 0.0, 0.0)
    glEnd()

    glPushMatrix()
    glRotatef(45,0,0,1)
    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.741, 0.988)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.04 + 0.065, sin(angulo) * 0.02 + 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glRotatef(-45,0,0,1)
    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.741, 0.988)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.04 + 0.065, sin(angulo) * 0.02 + 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glRotatef(135,0,0,1)
    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.741, 0.988)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.04 + 0.065, sin(angulo) * 0.02 + 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glRotatef(-135,0,0,1)
    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.741, 0.988)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.04 + 0.065, sin(angulo) * 0.02 + 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.741, 0.988)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.02 + 0.0, sin(angulo) * 0.04 + 0.066, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.741, 0.988)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.02 + 0.0, sin(angulo) * 0.04 - 0.06, 0.0)
    glEnd()

    #centro
    glBegin(GL_POLYGON)
    glColor3f(0.96, 0.96, 0.094)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.025 + 0.0, sin(angulo) * 0.025 + 0.0, 0.0)
    glEnd()

    glPopMatrix()

def dibujarFlor2():

    glPushMatrix()

    glTranslatef(0.542, 0.885, 0.0)

    glBegin(GL_POLYGON)
    glColor3f(0.423, 0.984, 0.964)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.04 + 0.065, sin(angulo) * 0.02 + 0.0, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.423, 0.984, 0.964)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.04 - 0.065, sin(angulo) * 0.02 + 0.0, 0.0)
    glEnd()

    glPushMatrix()
    glRotatef(45,0,0,1)
    glBegin(GL_POLYGON)
    glColor3f(0.423, 0.984, 0.964)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.04 + 0.065, sin(angulo) * 0.02 + 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glRotatef(-45,0,0,1)
    glBegin(GL_POLYGON)
    glColor3f(0.423, 0.984, 0.964)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.04 + 0.065, sin(angulo) * 0.02 + 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glRotatef(135,0,0,1)
    glBegin(GL_POLYGON)
    glColor3f(0.423, 0.984, 0.964)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.04 + 0.065, sin(angulo) * 0.02 + 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glRotatef(-135,0,0,1)
    glBegin(GL_POLYGON)
    glColor3f(0.423, 0.984, 0.964)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.04 + 0.065, sin(angulo) * 0.02 + 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glBegin(GL_POLYGON)
    glColor3f(0.423, 0.984, 0.964)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.02 + 0.0, sin(angulo) * 0.04 + 0.066, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.423, 0.984, 0.964)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.02 + 0.0, sin(angulo) * 0.04 - 0.06, 0.0)
    glEnd()

    #centro
    glBegin(GL_POLYGON)
    glColor3f(0.96, 0.96, 0.094)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.025 + 0.0, sin(angulo) * 0.025 + 0.0, 0.0)
    glEnd()

    glPopMatrix()

def dibujarFlor3():

    glPushMatrix()

    glTranslatef(-0.54, 0.885, 0.0)

    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.823, 0.423)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.04 + 0.065, sin(angulo) * 0.02 + 0.0, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.823, 0.423)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.04 - 0.065, sin(angulo) * 0.02 + 0.0, 0.0)
    glEnd()

    glPushMatrix()
    glRotatef(45,0,0,1)
    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.823, 0.423)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.04 + 0.065, sin(angulo) * 0.02 + 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glRotatef(-45,0,0,1)
    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.823, 0.423)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.04 + 0.065, sin(angulo) * 0.02 + 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glRotatef(135,0,0,1)
    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.823, 0.423)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.04 + 0.065, sin(angulo) * 0.02 + 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glRotatef(-135,0,0,1)
    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.823, 0.423)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.04 + 0.065, sin(angulo) * 0.02 + 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.823, 0.423)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.02 + 0.0, sin(angulo) * 0.04 + 0.066, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.823, 0.423)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.02 + 0.0, sin(angulo) * 0.04 - 0.06, 0.0)
    glEnd()

    #centro
    glBegin(GL_POLYGON)
    glColor3f(0.96, 0.96, 0.094)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.025 + 0.0, sin(angulo) * 0.025 + 0.0, 0.0)
    glEnd()

    glPopMatrix()

def dibujarAllFlor():
    tiempo_actual = glfw.get_time()

    if tiempo_actual < 30:
        dibujarFlor()
    elif tiempo_actual < 40:
        dibujarFlor2()
    elif tiempo_actual < 50:
        dibujarFlor3()

def dibujarFloresRocas():
    tiempo_actual = glfw.get_time()

    if tiempo_actual < 20:
        dibujarAllRocas()
    elif tiempo_actual < 50:
        dibujarAllFlor()

def dibujarRocas():
    
    glBegin(GL_POLYGON)
    glColor3f(0.509, 0.368, 0.105)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.0, sin(angulo) * 0.010 + 0.0, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.08, sin(angulo) * 0.010 + 0.03, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.0 +0.08, sin(angulo) * 0.010 + 0.0-0.05, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.08 -0.05, sin(angulo) * 0.010 + 0.03 -0.12, 0.0)
    glEnd()

    #

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 + 0.08, sin(angulo) * 0.010 + 0.01, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.0 +0.04, sin(angulo) * 0.010 + 0.0-0.09, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.08 -0.13, sin(angulo) * 0.010 + 0.03 -0.07, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.0, sin(angulo) * 0.010 + 0.0, 0.0)
    glEnd()

    #AA

    glPushMatrix()
    glTranslatef(0.4, 0, 0)

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.08, sin(angulo) * 0.010 + 0.03, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.0 +0.08, sin(angulo) * 0.010 + 0.0-0.05, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.08 -0.05, sin(angulo) * 0.010 + 0.03 -0.12, 0.0)
    glEnd()

    #

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 + 0.08, sin(angulo) * 0.010 + 0.01, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.0 +0.04, sin(angulo) * 0.010 + 0.0-0.09, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.08 -0.13, sin(angulo) * 0.010 + 0.03 -0.07, 0.0)
    glEnd()

    glPopMatrix()

    #AAA

    glPushMatrix()
    glTranslatef(-0.4, 0, 0)

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.08, sin(angulo) * 0.010 + 0.03, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.0 +0.08, sin(angulo) * 0.010 + 0.0-0.05, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.08 -0.05, sin(angulo) * 0.010 + 0.03 -0.12, 0.0)
    glEnd()

    #

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 + 0.08, sin(angulo) * 0.010 + 0.01, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.0 +0.04, sin(angulo) * 0.010 + 0.0-0.09, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.08 -0.13, sin(angulo) * 0.010 + 0.03 -0.07, 0.0)
    glEnd()

    glPopMatrix()

    #AAA

    glPushMatrix()
    glTranslatef(0.9, 0, 0)

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.08, sin(angulo) * 0.010 + 0.03, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.0 +0.08, sin(angulo) * 0.010 + 0.0-0.05, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.08 -0.05, sin(angulo) * 0.010 + 0.03 -0.12, 0.0)
    glEnd()

    #

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 + 0.08, sin(angulo) * 0.010 + 0.01, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.0 +0.04, sin(angulo) * 0.010 + 0.0-0.09, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.08 -0.13, sin(angulo) * 0.010 + 0.03 -0.07, 0.0)
    glEnd()

    glPopMatrix()

    #AAA

    glPushMatrix()
    glTranslatef(-0.8, 0, 0)

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.08, sin(angulo) * 0.010 + 0.03, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.0 +0.08, sin(angulo) * 0.010 + 0.0-0.05, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.08 -0.05, sin(angulo) * 0.010 + 0.03 -0.12, 0.0)
    glEnd()

    #

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 + 0.08, sin(angulo) * 0.010 + 0.01, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.0 +0.04, sin(angulo) * 0.010 + 0.0-0.09, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.08 -0.13, sin(angulo) * 0.010 + 0.03 -0.07, 0.0)
    glEnd()

    glPopMatrix()

def dibujarRocas2():
    
    glPushMatrix()
    glTranslatef(0,-0.9,0)
    glRotate(180,0,0,1)

    glBegin(GL_POLYGON)
    glColor3f(0.517, 0.313, 0.505)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.0, sin(angulo) * 0.010 + 0.0, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.08, sin(angulo) * 0.010 + 0.03, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.0 +0.08, sin(angulo) * 0.010 + 0.0-0.05, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.08 -0.05, sin(angulo) * 0.010 + 0.03 -0.12, 0.0)
    glEnd()

    #

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 + 0.08, sin(angulo) * 0.010 + 0.01, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.0 +0.04, sin(angulo) * 0.010 + 0.0-0.09, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.08 -0.13, sin(angulo) * 0.010 + 0.03 -0.07, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.0, sin(angulo) * 0.010 + 0.0, 0.0)
    glEnd()

    #AA

    glPushMatrix()
    glTranslatef(0.4, 0, 0)

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.08, sin(angulo) * 0.010 + 0.03, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.0 +0.08, sin(angulo) * 0.010 + 0.0-0.05, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.08 -0.05, sin(angulo) * 0.010 + 0.03 -0.12, 0.0)
    glEnd()

    #

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 + 0.08, sin(angulo) * 0.010 + 0.01, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.0 +0.04, sin(angulo) * 0.010 + 0.0-0.09, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.08 -0.13, sin(angulo) * 0.010 + 0.03 -0.07, 0.0)
    glEnd()

    glPopMatrix()

    #AAA

    glPushMatrix()
    glTranslatef(-0.4, 0, 0)

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.08, sin(angulo) * 0.010 + 0.03, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.0 +0.08, sin(angulo) * 0.010 + 0.0-0.05, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.08 -0.05, sin(angulo) * 0.010 + 0.03 -0.12, 0.0)
    glEnd()

    #

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 + 0.08, sin(angulo) * 0.010 + 0.01, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.0 +0.04, sin(angulo) * 0.010 + 0.0-0.09, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.08 -0.13, sin(angulo) * 0.010 + 0.03 -0.07, 0.0)
    glEnd()

    glPopMatrix()

    #AAA

    glPushMatrix()
    glTranslatef(0.9, 0, 0)

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.08, sin(angulo) * 0.010 + 0.03, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.0 +0.08, sin(angulo) * 0.010 + 0.0-0.05, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.08 -0.05, sin(angulo) * 0.010 + 0.03 -0.12, 0.0)
    glEnd()

    #

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 + 0.08, sin(angulo) * 0.010 + 0.01, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.0 +0.04, sin(angulo) * 0.010 + 0.0-0.09, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.08 -0.13, sin(angulo) * 0.010 + 0.03 -0.07, 0.0)
    glEnd()

    glPopMatrix()

    #AAA

    glPushMatrix()
    glTranslatef(-0.8, 0, 0)

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.08, sin(angulo) * 0.010 + 0.03, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.0 +0.08, sin(angulo) * 0.010 + 0.0-0.05, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.08 -0.05, sin(angulo) * 0.010 + 0.03 -0.12, 0.0)
    glEnd()

    #

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 + 0.08, sin(angulo) * 0.010 + 0.01, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.0 +0.04, sin(angulo) * 0.010 + 0.0-0.09, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.015 - 0.08 -0.13, sin(angulo) * 0.010 + 0.03 -0.07, 0.0)
    glEnd()

    glPopMatrix()

    glPopMatrix()

def dibujarAllRocas():
    tiempo_actual = glfw.get_time()

    if tiempo_actual < 10:
        dibujarRocas2()
    elif tiempo_actual < 20:
        dibujarRocas()

def dibujar():
    # rutinas de dibujo
    #dibujarObstaculo()
    dibujarCamino()
    dibujarCesped()
    dibujarCesped2()
    dibujarParteArriba()
    dibujarAllTronco()
    dibujarAllCamiones()
    dibujarAllCarros()
    dibujarAllTortuga()
    dibujarAllNenufar()
    dibujarAllMoscas()
    dibujarFloresRocas()
    dibujarVidas()
    dibujarRana()
    #dibujarRanaSkin()


def main():
    # inicia glfw
    if not glfw.init():
        return

    # crea la ventana,
    # independientemente del SO que usemos
    window = glfw.create_window(800, 800, "Mi ventana", None, None)

    # Configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    # Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    # Establecemos el contexto
    glfw.make_context_current(window)

    # Activamos la validación de
    # funciones modernas de OpenGL
    glewExperimental = True

    # Inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    # Obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    while not glfw.window_should_close(window):
        # Establece regiond e dibujo
        glViewport(0, 0, 800, 800)
        # Establece color de borrado
        glClearColor(0.120,0.600,1.0,0.0)
        # Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Dibujar
        actualizar(window)
        dibujar()

        # Preguntar si hubo entradas de perifericos
        # (Teclado, mouse, game pad, etc.)
        glfw.poll_events()
        # Intercambia los buffers
        glfw.swap_buffers(window)

    # Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    # Termina los procesos que inició glfw.init
    glfw.terminate()


if __name__ == "__main__":
    main()