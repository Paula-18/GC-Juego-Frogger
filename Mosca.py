from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *

class Mosca():
    posicionX = 0.0
    posicionY = 0.0
    colision = False
    
    def __init__(self, x, y):
        self.posicionX = x
        self.posicionY = y

    def dibujar(self):
        #global colisionandoMosca1

        glPushMatrix()
        glTranslate(self.posicionX, self.posicionY, 0.0)
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

        # Si colisionando es False se creara la mosca, pero si es True se creara la rana para sustituirla
        #if colision == False:
        #    dibujar()
        #else: 
        #    glScalef(0.7,0.7,1)
        #    dibujarRanaSkin()
        #    glPopMatrix()
        
    #def checar_colisiones():
    #    global colisionandoMosca1
    #    global colisionandoMosca2
    #    global colisionandoMosca3
    #    global colisionandoMosca4
    #    global colisionandoCarro
    #    global rana
    #    # Si extremaDerechaCarrito > extremaIzquierdaObstaculo
    #    # Y extremaIzquierdaCarrito < extremaDerechaObstaculo
    #    # Y extremoSuperiorCarrito > extremoInferiorObstaculo
    #    # Y extremoInferiorCarrito < extremoSuperiorObstaculo
    #    # Cuando la rana colisione con la mosca 1 se convertira en true y la rana regresara al punto de partida
    #    if rana.posicionX + 0.05 > xMosca1 - 0.05 and rana.posicionX - 0.05 < xMosca1 + 0.05 and rana.posicionY + 0.05 > yMosca1 - 0.05 and rana.posicionY - 0.05 < yMosca1 + 0.05:
    #        colisionandoMosca1 = True
    #        rana.resetPosition()
    #    # Cuando la rana colisione con la mosca 2 se convertira en true y la rana regresara al punto de partida
    #    if rana.posicionX + 0.05 > xMosca2 - 0.05 and rana.posicionX - 0.05 < xMosca2 + 0.05 and rana.posicionY + 0.05 > yMosca2 - 0.05 and rana.posicionY - 0.05 < yMosca2 + 0.05:
    #        colisionandoMosca2 = True
    #        rana.resetPosition()
    #    # Cuando la rana colisione con la mosca 3 se convertira en true y la rana regresara al punto de partida
    #    if rana.posicionX + 0.05 > xMosca3 - 0.05 and rana.posicionX - 0.05 < xMosca3 + 0.05 and rana.posicionY + 0.05 > yMosca3 - 0.05 and rana.posicionY - 0.05 < yMosca3 + 0.05:
    #        colisionandoMosca3 = True
    #        rana.resetPosition()
    #    # Cuando la rana colisione con la mosca 4 se convertira en true y la rana regresara al punto de partida
    #    if rana.posicionX + 0.05 > xMosca4 - 0.05 and rana.posicionX - 0.05 < xMosca4 + 0.05 and rana.posicionY + 0.05 > yMosca4 - 0.05 and rana.posicionY - 0.05 < yMosca4 + 0.05:
    #        colisionandoMosca4 = True
    #        rana.resetPosition()
    #    if colisionandoMosca1 == True and colisionandoMosca2 == True and colisionandoMosca3 == True and colisionandoMosca4 == True:
    #        exit()