from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def border():  # METHOD TO DRAW LINES
    glBegin(GL_LINES)
    glVertex2f(100, 10)  # COORDINATES MUST BE IN ANTICLOCKWISE ORDER
    glVertex2f(400, 10)
    glVertex2f(400, 10)
    glVertex2f(400, 300)
    glVertex2f(400, 300)
    glVertex2f(100, 300)
    glVertex2f(100, 300)
    glVertex2f(100, 10)
    glEnd()


def roof():  # METHOD TO DRAW TRIANGLE
    glBegin(GL_TRIANGLES)
    glVertex2f(100, 300)  # COORDINATES MUST BE IN ANTICLOCKWISE ORDER
    glVertex2f(250, 490)
    glVertex2f(400, 300)
    glEnd()


def door():  # METHOD TO DRAW LINES
    glBegin(GL_LINES)
    glVertex2f(290, 10)  # COORDINATES MUST BE IN ANTICLOCKWISE ORDER
    glVertex2f(290, 120)
    glVertex2f(290, 120)
    glVertex2f(210, 120)
    glVertex2f(210, 120)
    glVertex2f(210, 10)
    glEnd()


def window1():  # METHOD TO DRAW LINES
    glBegin(GL_LINES)
    glVertex2f(130, 180)  # COORDINATES MUST BE IN ANTICLOCKWISE ORDER
    glVertex2f(220, 180)
    glVertex2f(220, 180)
    glVertex2f(220, 270)
    glVertex2f(220, 270)
    glVertex2f(130, 270)
    glVertex2f(130, 270)
    glVertex2f(130, 180)
    glEnd()


def window2():  # METHOD TO DRAW LINES
    glBegin(GL_LINES)
    glVertex2f(280, 180)  # COORDINATES MUST BE IN ANTICLOCKWISE ORDER
    glVertex2f(370, 180)
    glVertex2f(370, 180)
    glVertex2f(370, 270)
    glVertex2f(370, 270)
    glVertex2f(280, 270)
    glVertex2f(280, 270)
    glVertex2f(280, 180)
    glEnd()


def handle(x, y):  # METHOD TO DRAW POINTS
    glPointSize(5)  # PIXEL SIZE (1 BY DEFAULT)
    glBegin(GL_POINTS)
    glVertex2f(x, y)  # COORDINATES TO SHOW PIXEL
    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0)  # COLOR SET (RGB)
    # CALL THE DRAW METHODS HERE
    border()
    roof()
    door()
    window1()
    window2()
    handle(280, 65)
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)  # WINDOW SIZE
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")  # WINDOW NAME
glutDisplayFunc(showScreen)

glutMainLoop()
