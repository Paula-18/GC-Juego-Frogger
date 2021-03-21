from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *    
from Rana import *
from Tronco import *
from Carro import *
from Nenufar import *
from Camion import * 
from Tortuga import *

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

#ubicacion de la rana al iniciar la partida
xVidas = -0.9
yVidas = -0.9

#variables de colisiones de las moscas
colisionandoMosca1 = False
colisionandoMosca2 = False
colisionandoMosca3 = False
colisionandoMosca4 = False
colisionandoCarro = False

#angulo que se necesita para girar a la rana
tiempo_anterior = 0.0

#Clases importadas
rana = Rana()

#dibujar a los troncos
tronco1 = Tronco(1.2, 0.1, 0.7, 0.007)
tronco2 = Tronco(1.8, 0.1, 0.7, 0.007)
tronco3 = Tronco(2.4, 0.1, 0.7, 0.007)
tronco4 = Tronco(1.6, 0.5, 1.1, 0.004)
tronco5 = Tronco(2.2, 0.5, 1.1, 0.004)
tronco6 = Tronco(2.8, 0.5, 1.1, 0.004)

#dibujar a los carros
carro1 = Carro(1.2,-0.65)
carro2 = Carro(1.7,-0.65)
carro3 = Carro(2.4,-0.65)
carro4 = Carro(-1.2,-0.15)

#dibujar a los nenufares
nenufar1 = Nenufar(-1.5, 0.7)
nenufar2 = Nenufar(-2.0, 0.7)
nenufar3 = Nenufar(-2.8, 0.7)

#dibujar a los camiones
camion1 = Camion(1.2,-0.3)
camion2 = Camion(2.0, -0.3)
camion3 = Camion(-1.2,-0.5)
camion4 = Camion(-2.0,-0.5)

#dibujar a las tortugas
tortuga1 = Tortuga(-1.2, 0.28)
tortuga2 = Tortuga(-1.7, 0.28)
tortuga3 = Tortuga(-2.5,0.28)

def checar_colisiones():
    global colisionandoMosca1
    global colisionandoMosca2
    global colisionandoMosca3
    global colisionandoMosca4
    global rana
    # Si extremaDerechaCarrito > extremaIzquierdaObstaculo
    # Y extremaIzquierdaCarrito < extremaDerechaObstaculo
    # Y extremoSuperiorCarrito > extremoInferiorObstaculo
    # Y extremoInferiorCarrito < extremoSuperiorObstaculo
    # Cuando la rana colisione con la mosca 1 se convertira en true y la rana regresara al punto de partida
    if rana.posicionX + 0.05 > xMosca1 - 0.05 and rana.posicionX - 0.05 < xMosca1 + 0.05 and rana.posicionY + 0.05 > yMosca1 - 0.05 and rana.posicionY - 0.05 < yMosca1 + 0.05:
        colisionandoMosca1 = True
        rana.resetPosition()
    # Cuando la rana colisione con la mosca 2 se convertira en true y la rana regresara al punto de partida
    if rana.posicionX + 0.05 > xMosca2 - 0.05 and rana.posicionX - 0.05 < xMosca2 + 0.05 and rana.posicionY + 0.05 > yMosca2 - 0.05 and rana.posicionY - 0.05 < yMosca2 + 0.05:
        colisionandoMosca2 = True
        rana.resetPosition()
    # Cuando la rana colisione con la mosca 3 se convertira en true y la rana regresara al punto de partida
    if rana.posicionX + 0.05 > xMosca3 - 0.05 and rana.posicionX - 0.05 < xMosca3 + 0.05 and rana.posicionY + 0.05 > yMosca3 - 0.05 and rana.posicionY - 0.05 < yMosca3 + 0.05:
        colisionandoMosca3 = True
        rana.resetPosition()
    # Cuando la rana colisione con la mosca 4 se convertira en true y la rana regresara al punto de partida
    if rana.posicionX + 0.05 > xMosca4 - 0.05 and rana.posicionX - 0.05 < xMosca4 + 0.05 and rana.posicionY + 0.05 > yMosca4 - 0.05 and rana.posicionY - 0.05 < yMosca4 + 0.05:
        colisionandoMosca4 = True
        rana.resetPosition()
    if colisionandoMosca1 == True and colisionandoMosca2 == True and colisionandoMosca3 == True and colisionandoMosca4 == True:
        exit()



def actualizar(window):
    global rana
    rana.actualizar(window)
    checar_colisiones()

def dibujarAllTronco():
    global tronco1
    global tronco2
    global tronco3
    global tronco4
    global tronco5
    global tronco6
    global rana
    tronco1.dibujar(rana)
    tronco2.dibujar(rana)
    tronco3.dibujar(rana)
    tronco4.dibujar(rana)
    tronco5.dibujar(rana)
    tronco6.dibujar(rana)

def dibujarAllCarros():
    global carro1
    global carro2
    global carro3
    global carro4
    global rana

    carro1.dibujar_1(rana)
    carro2.dibujar_1(rana)
    carro3.dibujar_1(rana)
    carro4.dibujar_2(rana)

def dibujarAllCamiones():
    global camion1
    global camion2
    global camion3
    global camion4
    global rana

    camion1.dibujarCamion(rana)
    camion2.dibujarCamion(rana)
    camion3.dibujarCamion2(rana)
    camion4.dibujarCamion2(rana)

def dibujarAllTortuga():
    global tortuga1
    global tortuga2
    global tortuga3
    global rana
    
    tortuga1.dibujarTortuga1(rana)
    tortuga2.dibujarTortuga2(rana)
    tortuga3.dibujarTortuga2(rana)

def dibujarAllNenufar():
    global nenufar1
    global nenufar2
    global nenufar3
    global rana 

    nenufar1.dibujarNenufar1(rana)
    nenufar2.dibujarNenufar2(rana)
    nenufar3.dibujarNenufar1(rana)

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
    global rana
    global xVidas
    global yVidas

    glPushMatrix()
    glTranslate(xVidas, yVidas, 0.0)
    # Si colisionando es False se creara la mosca, pero si es True se creara la rana para sustituirla
    if rana.vida == 3:
        dibujarHilera3Vidas()
    elif rana.vida == 2:
        dibujarHilera2Vidas()
    elif rana.vida == 1:
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
    global rana
    
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
    rana.dibujar()
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