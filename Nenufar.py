from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *

class Nenufar():

    posicionX = 0.0
    posicionY = 0.0

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

    def dibujarHilera2Nenufar(self):
        glPushMatrix()
        glTranslate(0.0, 0.0, 0.0)
        glScalef(0.6,0.8,1)
        self.dibujarNenufar()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0.1, 0.0, 0.0)
        glScalef(0.6,0.8,1)
        dibujarNenufar()
        glPopMatrix()

    def dibujarHilera3Nenufar(self):
        glPushMatrix()
        glTranslate(0.0, 0.0, 0.0)
        glScalef(0.6,0.8,1)
        self.dibujarNenufar()
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

    def dibujarNenufar1(self, rana):

        glPushMatrix()
        glTranslate(self.posicionX, self.posicionY, 0.0)
        glRotate(180, 0.0, 0.0, 1.0)
        glScalef(1.0,0.8,1)
        self.dibujarHilera2Nenufar()
        glPopMatrix()

        if self.posicionX < 1.3:
            self.posicionX = self.posicionX + 0.011
        else:
            self.posicionX = -1.2

        # Cuando la rana colisione con el carro 1 se convertira en True, la rana muera y regresara al punto de partida
        if rana.posicionX + 0.05 > self.posicionX - 0.1 and rana.posicionX - 0.05 < self.posicionX + 0.08 and rana.posicionY + 0.05 > self.posicionY - 0.05 and rana.posicionY - 0.05 < self.posicionY + 0.05:
            rana.vidas()
            rana.resetPosition()

    def dibujarNenufar2(self, rana):

        glPushMatrix()
        glTranslate(self.posicionX, self.posicionY, 0.0)
        glRotate(180, 0.0, 0.0, 1.0)
        glScalef(1.0,0.8,1)
        self.dibujarHilera3Nenufar()
        glPopMatrix()

        if self.posicionX < 1.3:
            self.posicionX = self.posicionX + 0.011
        else:
            self.posicionX = -1.2

        # Cuando la rana colisione con el carro 1 se convertira en True, la rana muera y regresara al punto de partida
        if rana.posicionX + 0.05 > self.posicionX - 0.1 and rana.posicionX - 0.05 < self.posicionX + 0.08 and rana.posicionY + 0.05 > self.posicionY - 0.05 and rana.posicionY - 0.05 < self.posicionY + 0.05:
            rana.vidas()
            rana.resetPosition()