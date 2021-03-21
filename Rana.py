from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *

class Rana():

    posicionX = 0.0
    posicionY = -0.9
    vida= 3.0
    angulo = 0

    def resetPosition(self):
        self.posicionX = 0.0
        self.posicionY = -0.9
        
    def vidas(self):
        self.vida = self.vida - 1.0
        if self.vida < 0:
            exit()

    def dibujar(self):

        #glScalef(1,1,1) #no se como se usa xd

        glPushMatrix()
        glTranslate(self.posicionX, self.posicionY, 0.0)
        glRotate(self.angulo, 0.0, 0.0, 1.0)
        glScalef(0.7,0.7,1) #aqui va xd
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

    def actualizar(self, window):
        estadoIzquierda = glfw.get_key(window, glfw.KEY_LEFT)
        estadoDerecha = glfw.get_key(window, glfw.KEY_RIGHT)
        estadoAbajo = glfw.get_key(window, glfw.KEY_DOWN)
        estadoArriba = glfw.get_key(window, glfw.KEY_UP)

        if estadoIzquierda == glfw.PRESS and self.posicionX - 0.05 > -1:
            self.angulo = 90
            self.posicionX = self.posicionX - 0.007
        if estadoDerecha == glfw.PRESS and self.posicionX + 0.05 < 1:
            self.angulo = 270
            self.posicionX = self.posicionX + 0.007
        if estadoAbajo == glfw.PRESS and self.posicionY - 0.05 - 0.001 > -1:
            self.angulo = 180
            self.posicionY = self.posicionY - 0.007
        # Para arriba hay que considerar que el viewport también
        # toma en cuenta la barra de titulo
        if estadoArriba == glfw.PRESS and self.posicionY + 0.05 + 0.1 < 1:
            self.angulo = 0
            self.posicionY = self.posicionY + 0.007
