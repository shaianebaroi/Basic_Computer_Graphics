from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random


def draw_points(x, y):
    glPointSize(5)                                  # PIXEL SIZE (1 BY DEFAULT)
    glBegin(GL_POINTS)
    glVertex2f(x, y)                                # COORDINATES TO SHOW PIXEL
    glEnd()


def pixelGenerator(limit):
    for count in range(limit):
        x = random.randrange(0, 500)
        y = random.randrange(0, 500)
        draw_points(x, y)


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
    glColor3f(1.0, 1.0, 0.0)                        # COLOR SET (RGB)
    # CALL THE DRAW METHODS HERE
    pixelGenerator(50)
    
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)                        # WINDOW SIZE
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")  # WINDOW NAME
glutDisplayFunc(showScreen)

glutMainLoop()
