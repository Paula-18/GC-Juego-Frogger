from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *

class Tortuga():

    posicionX = 0.0
    posicionY = 0.0

    def __init__(self, x, y):
        self.posicionX = x
        self.posicionY = y
    
    def dibujar(self):

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

    def dibujarHilera2Tortuga(self):
        glPushMatrix()
        glTranslate(0.0, 0.0, 0.0)
        glScalef(0.6,0.8,1)
        self.dibujar()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0.2, 0.0, 0.0)
        glScalef(0.6,0.8,1)
        self.dibujar()
        glPopMatrix()

    def dibujarHilera3Tortuga(self):
        glPushMatrix()
        glTranslate(0.0, 0.0, 0.0)
        glScalef(0.6,0.8,1)
        self.dibujar()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0.2, 0.0, 0.0)
        glScalef(0.6,0.8,1)
        self.dibujar()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0.4, 0.0, 0.0)
        glScalef(0.6,0.8,1)
        self.dibujar()
        glPopMatrix()

    def dibujarTortuga1(self, rana):
        glPushMatrix()
        glTranslate(self.posicionX, self.posicionY, 0.0)
        glRotate(180, 0.0, 0.0, 1.0)
        glScalef(0.6,0.8,1)
        self.dibujarHilera3Tortuga()
        glPopMatrix()

        if self.posicionX < 1.3:
            self.posicionX = self.posicionX + 0.008
        else:
            self.posicionX = -1.2

        if rana.posicionX + 0.05 > self.posicionX - 0.2 and rana.posicionX - 0.05 < self.posicionX + 0.05 and rana.posicionY + 0.05 > self.posicionY - 0.05 and rana.posicionY - 0.05 < self.posicionY + 0.05:
            rana.vidas()
            rana.resetPosition()

    def dibujarTortuga2(self, rana):
        glPushMatrix()
        glTranslate(self.posicionX, self.posicionY, 0.0)
        glRotate(180, 0.0, 0.0, 1.0)
        glScalef(0.6,0.8,1)
        self.dibujarHilera2Tortuga()
        glPopMatrix()

        if self.posicionX < 1.3:
            self.posicionX = self.posicionX + 0.008
        else:
            self.posicionX = -1.2

        if rana.posicionX + 0.05 > self.posicionX - 0.2 and rana.posicionX - 0.05 < self.posicionX + 0.05 and rana.posicionY + 0.05 > self.posicionY - 0.05 and rana.posicionY - 0.05 < self.posicionY + 0.05:
            rana.vidas()
            rana.resetPosition()