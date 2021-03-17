from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *

class Tronco():
    posicionX = 0.0
    posicionY = 0.0 
    scaleY = 0.0
    vel = 0.0

    def __init__(self, x, y, scaley, vel):
        self.posicionX = x
        self.posicionY = y
        self.scaleY = scaley
        self.vel = vel

    def dibujar(self, rana):
        glPushMatrix()
        glTranslate(self.posicionX, self.posicionY, 0.0)
        glScalef(0.7,self.scaleY,1) 
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

        glPopMatrix()

        if self.posicionX > -1.3:
            self.posicionX = self.posicionX - self.vel
        else:
            self.posicionX = 1.2
        
        if rana.posicionX + 0.05 > self.posicionX - 0.11 and rana.posicionX - 0.05 < self.posicionX + 0.13 and rana.posicionY + 0.05 > self.posicionY - 0.05 and rana.posicionY - 0.05 < self.posicionY + 0.05:
            rana.vidas()
            rana.resetPosition()


    #def dibujarTronco(self):
        
        
        #    # Cuando la rana colisione con el tronco 1 se convertira en True, la rana muera y regresara al punto de partida
        #    if xRana + 0.05 > xTronco4 - 0.11 and xRana - 0.05 < xTronco4 + 0.13 and yRana + 0.05 > yTronco4 - 0.05 and yRana - 0.05 < yTronco4 + 0.05:
        #        vidasRana()
        #        resetPosition()