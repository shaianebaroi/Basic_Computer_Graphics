from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def vertical(x1, y1, x2, y2):
    glBegin(GL_POINTS)
    glVertex2f(x1, y1)
    while y1 < y2:
        y1 += 1
        glVertex2f(x1, round(y1))
    glEnd()


def horizontal(x1, y1, x2, y2):
    glBegin(GL_POINTS)
    glVertex2f(x1, y1)
    while x1 < x2:
        x1 += 5
        glVertex2f(x1, round(y1))
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
    vertical(250, 125, 250, 375)
    horizontal(125, 375, 375, 375)
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)  # WINDOW SIZE
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")  # WINDOW NAME
glutDisplayFunc(showScreen)

glutMainLoop()
