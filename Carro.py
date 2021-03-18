from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *

class Carro():

    posicionX = 0.0
    posicionY = 0.0

    #posicion1X = 1.2
    #posicion1Y = -0.65
    #posicion2X = 1.7
    #posicion2Y = -0.65
    #posicion3X = 2.4
    #posicion3Y = -0.65
    #posicion4X = -1.2
    #posicion4Y = -0.15

    def __init__(self, x, y):
        self.posicionX = x
        self.posicionY = y
    
    def dibujar1():
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

    def dibujar2():

        glBegin(GL_POLYGON)
        glColor3f(0.952, 0.976, 0.427)
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

    def dibujar_1(self,rana):

        glPushMatrix()
        glTranslate(self.posicionX, self.posicionY, 0.0)
        glScalef(0.5,0.5,1)
        self.dibujar_1()
        glPopMatrix()

        if self.posicionX > -1.3:
            self.posicionX = self.posicionX - 0.01
        else:
            self.posicionX = 1.2

        if rana.posicionX + 0.05 > self.posicionX - 0.05 and rana.posicionX - 0.05 < self.posicionX + 0.05 and rana.posicionY + 0.05 > self.posicionY - 0.05 and rana.posicionY - 0.05 < self.posicionY + 0.05:
            rana.resetPosition()
            rana.vidas()

    def dibujar_2(self, rana):

        glPushMatrix()
        glTranslate(self.posicionX, self.posicionY, 0.0)
        glScalef(0.5,0.5,1)
        self.dibujar2()
        glPopMatrix()

        if self.posicionX > -1.3:
            self.posicionX = self.posicionX - 0.01
        else:
            self.posicionX = 1.2
        
        if rana.posicionX + 0.05 > self.posicionX - 0.05 and rana.posicionX - 0.05 < self.posicionX + 0.05 and rana.posicionY + 0.05 > self.posicionY - 0.05 and rana.posicionY - 0.05 < self.posicionY + 0.05:
            rana.resetPosition()
            rana.vidas()
