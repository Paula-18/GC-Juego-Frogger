from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *

xObstaculo = 0.0
yObstaculo = 0.6

xCarrito = 0.0
yCarrito = -0.8

colisionando = False


def checar_colisiones():
    global colisionando
    # Si extremaDerechaCarrito > extremaIzquierdaObstaculo
    # Y extremaIzquierdaCarrito < extremaDerechaObstaculo
    # Y extremoSuperiorCarrito > extremoInferiorObstaculo
    # Y extremoInferiorCarrito < extremoSuperiorObstaculo
    if xCarrito + 0.05 > xObstaculo - 0.15 and xCarrito - 0.05 < xObstaculo + 0.15 and yCarrito + 0.05 > yObstaculo - 0.15 and yCarrito - 0.05 < yObstaculo + 0.15:
        colisionando = True
    else:
        colisionando = False


def actualizar(window):
    global xCarrito
    global yCarrito

    estadoIzquierda = glfw.get_key(window, glfw.KEY_LEFT)
    estadoDerecha = glfw.get_key(window, glfw.KEY_RIGHT)
    estadoAbajo = glfw.get_key(window, glfw.KEY_DOWN)
    estadoArriba = glfw.get_key(window, glfw.KEY_UP)

    if estadoIzquierda == glfw.PRESS and xCarrito - 0.05 > -1:
        xCarrito = xCarrito - 0.005
    if estadoDerecha == glfw.PRESS and xCarrito + 0.05 < 1:
        xCarrito = xCarrito + 0.005
    if estadoAbajo == glfw.PRESS and yCarrito - 0.05 - 0.001 > -1:
        yCarrito = yCarrito - 0.005
    # Para arriba hay que considerar que el viewport también
    # toma en cuenta la barra de titulo
    if estadoArriba == glfw.PRESS and yCarrito + 0.05 < 1:
        yCarrito = yCarrito + 0.005

    checar_colisiones()


def dibujarObstaculo():
    global xObstaculo
    global yObstaculo

    glPushMatrix()
    glTranslate(xObstaculo, yObstaculo, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 1.0)
    glVertex(-0.15, 0.15, 0.0)
    glVertex(0.15, 0.15, 0.0)
    glVertex(0.15, -0.15, 0.0)
    glVertex(-0.15, -0.15, 0.0)
    glEnd()
    glPopMatrix()

def dibujarRana():
    global colisionando
    global xCarrito
    global yCarrito

    #glScalef(1,1,1) #no se como se usa xd

    glPushMatrix()
    glTranslate(xCarrito, yCarrito, 0.0)
    #glScalef(0.7,0.7,1) #aqui va xd
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
    glVertex3f(-1.0, -0.13, 0.0)
    glVertex3f(1.0, -0.13, 0.0)
    glVertex3f(1.0, -0.73, 0.0)
    glVertex3f(-1.0, -0.73, 0.0)
    glEnd()

def dibujarCesped2():

    glBegin(GL_QUADS)
    glColor3f(0.658, 0.549, 0.341)
    glVertex3f(-1.0, -0.13, 0.0)
    glVertex3f(1.0, -0.13, 0.0)
    glVertex3f(1.0, 0.05, 0.0)
    glVertex3f(-1.0, 0.05, 0.0)
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

def dibujarTronco_2():

    glBegin(GL_QUADS)
    glColor3f(0.588, 0.427, 0.235)
    glVertex3f(-0.20, 0.08, 0.0)
    glVertex3f(0.20, 0.08, 0.0)
    glVertex3f(0.20, -0.08, 0.0)
    glVertex3f(-0.20, -0.08, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.07 - 0.19, sin(angulo) * 0.08 + 0.0, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.815, 0.615, 0.372)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.06 + 0.19, sin(angulo) * 0.08 + 0.0, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.588, 0.427, 0.235)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.04 + 0.19, sin(angulo) * 0.06 + 0.0, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.815, 0.615, 0.372)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.02 + 0.19, sin(angulo) * 0.04 + 0.0, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.588, 0.427, 0.235)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.01 + 0.19, sin(angulo) * 0.02 + 0.0, 0.0)
    glEnd()

def dibujarMuerteRana():

    glBegin(GL_POLYGON)
    glColor3f(0.772, 0.925, 0.780)
    glVertex3f(-0.03, 0.05, 0.0)
    glVertex3f(0.03, 0.05, 0.0)
    glVertex3f(0.03, -0.05, 0.0)
    glVertex3f(-0.03, -0.05, 0.0)

    glEnd()

    #Cara

    glBegin(GL_QUADS)
    glColor3f(0.772, 0.925, 0.780)
    glVertex3f(-0.02, 0.05, 0.0)
    glVertex3f(0.02, 0.05, 0.0)
    glVertex3f(0.02, 0.06, 0.0)
    glVertex3f(-0.02, 0.06, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-0.03, 0.05, 0.0)
    glVertex3f(-0.02, 0.05, 0.0)
    glVertex3f(-0.02, 0.04, 0.0)
    glVertex3f(-0.03, 0.04, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.03, 0.05, 0.0)
    glVertex3f(0.02, 0.05, 0.0)
    glVertex3f(0.02, 0.04, 0.0)
    glVertex3f(0.03, 0.04, 0.0)
    glEnd()

    #Mano derecha

    glBegin(GL_QUADS)
    glColor3f(0.772, 0.925, 0.780)
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

def dibujar():
    # rutinas de dibujo
    #dibujarObstaculo()
    #dibujarTronco()
    #dibujarCarro()
    #dibujarCamion()
    #dibujarTortuga()
    #dibujarMosca()
    #dibujarNenufar()
    #dibujarRanaSkin()
    #dibujarCaraRana()
    dibujarParteArriba()
    dibujarCamino()
    dibujarCesped()
    dibujarCesped2()
    #dibujarCarro_2()
    #dibujarCamion_2()
    #dibujarTronco_2()
    #dibujarMuerteRana()
    dibujarFlor()
    dibujarFlor2()
    dibujarFlor3()
    dibujarRocas()
    dibujarRocas2()
    dibujarRana()

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