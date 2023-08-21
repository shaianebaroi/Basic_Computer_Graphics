from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math


def WritePixel(x, y):  # METHOD TO DRAW POINTS
    glPointSize(1)  # PIXEL SIZE (1 BY DEFAULT)
    glBegin(GL_POINTS)
    glVertex2f(x, y)  # COORDINATES TO SHOW PIXEL
    glEnd()


def Origin():
    x = 250
    y = 250
    glPointSize(5)  # PIXEL SIZE (1 BY DEFAULT)
    glBegin(GL_POINTS)
    glVertex2f(x, y)  # COORDINATES TO SHOW PIXEL
    glEnd()

    # 50, 100, 250, 250


def Circlepoints(x, y, c_x, c_y):
    # x_f = x + c_x  # = 300
    # y_f = y + c_y  # = 350
    print(x)
    print(y)
    WritePixel(x + c_x, y + c_y)  # ZONE = 1
    WritePixel(y + c_x, x + c_y)  # ZONE = 0
    WritePixel(c_x - x, y + c_y)  # ZONE = 2
    WritePixel(c_x - y, c_y + x)  # ZONE = 3
    WritePixel(c_x - y, c_y - x)  # ZONE = 4
    WritePixel(c_x - x, c_y - y)  # ZONE = 5
    WritePixel(x + c_x, c_y - y)  # ZONE = 6
    WritePixel(y + c_x, c_y - x)  # ZONE = 7


def MidpointCircle(radius, c_x, c_y):

    x = 0
    y = radius
    d = 1 - radius

    Circlepoints(x, y, c_x, c_y)

    while x < y:
        if d < 0:
            # CHOOSE EAST
            d = d + (2 * x) + 3
            x += 1
        else:
            # CHOOSE SOUTH-EAST
            d = d + (2 * x) - (2 * y) + 5
            x += 1
            y -= 1
        Circlepoints(x, y, c_x, c_y)


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
    Origin()
    MidpointCircle(200, 250, 250)
    MidpointCircle(100, 350, 250)
    MidpointCircle(100, 150, 250)
    MidpointCircle(100, 250, 350)
    MidpointCircle(100, 250, 150)
    MidpointCircle(
        100, (math.cos(math.pi / 4) * 100) + 250, (math.cos(math.pi / 4) * 100) + 250
    )
    MidpointCircle(
        100, (math.cos(math.pi / 4) * 100) + 110, (math.cos(math.pi / 4) * 100) + 110
    )
    MidpointCircle(
        100, (math.cos(math.pi / 4) * 100) + 110, (math.cos(math.pi / 4) * 100) + 250
    )
    MidpointCircle(
        100, (math.cos(math.pi / 4) * 100) + 250, (math.cos(math.pi / 4) * 100) + 110
    )

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)  # WINDOW SIZE
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")  # WINDOW NAME
glutDisplayFunc(showScreen)

glutMainLoop()
