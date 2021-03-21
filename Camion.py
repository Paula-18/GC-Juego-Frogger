from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *

class Camion():
    posicionX = 0.0
    posicionY = 0.0

    def __init__(self, x, y):
        self.posicionX = x
        self.posicionY = y


    def dibujar(self):
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

    def dibujar2(self):
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

    def dibujarCamion(self, rana):
        glPushMatrix()
        glTranslate(self.posicionX, self.posicionY, 0.0)
        glScalef(0.5,0.8,1)
        self.dibujar()
        glPopMatrix()

        if self.posicionX > -1.3:
            self.posicionX = self.posicionX - 0.006
        else:
            self.posicionX = 1.2

        if rana.posicionX + 0.05 > self.posicionX - 0.055 and rana.posicionX - 0.05 < self.posicionX + 0.055 and rana.posicionY + 0.05 > self.posicionY - 0.05 and rana.posicionY - 0.05 < self.posicionY + 0.05:
            rana.resetPosition()
            rana.vidas()

    def dibujarCamion2(self, rana):
        glPushMatrix()
        glTranslate(self.posicionX, self.posicionY, 0.0)
        glScalef(0.5,0.8,1)
        self.dibujar2()
        glPopMatrix()

        if self.posicionX < 1.3:
            self.posicionX = self.posicionX + 0.003
        else:
            self.posicionX = -1.2

        if rana.posicionX + 0.05 > self.posicionX - 0.055 and rana.posicionX - 0.05 < self.posicionX + 0.055 and rana.posicionY + 0.05 > self.posicionY - 0.05 and rana.posicionY - 0.05 < self.posicionY + 0.05:
            rana.resetPosition()
            rana.vidas()