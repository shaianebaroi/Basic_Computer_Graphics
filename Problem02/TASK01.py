from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_points(x, y):  # METHOD TO DRAW POINTS
    glPointSize(5)  # PIXEL SIZE (1 BY DEFAULT)
    glBegin(GL_POINTS)
    glVertex2f(x, y)  # COORDINATES TO SHOW PIXEL
    glEnd()


def findZone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    if abs(dx) >= abs(dy):
        if dx > 0 and dy > 0:
            zone = 0
        elif dx <= 0 and dy > 0:
            zone = 3
        elif dx <= 0 and dy <= 0:
            zone = 4
        elif dx > 0 and dy <= 0:
            zone = 7

    elif abs(dy) >= abs(dx):
        if dx > 0 and dy > 0:
            zone = 1
        elif dx <= 0 and dy > 0:
            zone = 2
        elif dx <= 0 and dy <= 0:
            zone = 5
        elif dx > 0 and dy <= 0:
            zone = 6

    return zone


def zoneMtozone0(zone, x1, y1):
    if zone == 0:
        x = x1
        y = y1
    elif zone == 1:
        x = y1
        y = x1
    elif zone == 2:
        x = y1
        y = -x1
    elif zone == 3:
        x = -x1
        y = y1
    elif zone == 4:
        x = -x1
        y = -y1
    elif zone == 5:
        x = -y1
        y = -x1
    elif zone == 6:
        x = -y1
        y = x1
    elif zone == 7:
        x = x1
        y = -y1

    return [x, y]


def drawLine(x1, y1, x2, y2):
    intermediate_points = []
    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx
    incE = 2 * dy
    incNE = 2 * (dy - dx)
    y = y1
    x = x1

    while x <= x2:
        intermediate_points.append([x, y])
        if d > 0:
            d = d + incNE
            y = y + 1
        else:
            d = d + incE
        x += 1

    return intermediate_points


def zone0tozoneM(zone, x1, y1):
    if zone == 0:
        x = x1
        y = y1
    elif zone == 1:
        x = y1
        y = x1
    elif zone == 2:
        x = -y1
        y = x1
    elif zone == 3:
        x = -x1
        y = y1
    elif zone == 4:
        x = -x1
        y = -y1
    elif zone == 5:
        x = -y1
        y = -x1
    elif zone == 6:
        x = y1
        y = -x1
    elif zone == 7:
        x = x1
        y = -y1
    return [x, y]


def midpointLineAlgorithm(x1, y1, x2, y2):
    # FINDING THE ZONE
    zone = findZone(x1, y1, x2, y2)

    # CONVERTING TO ZONE 0
    converted1 = zoneMtozone0(zone, x1, y1)
    converted2 = zoneMtozone0(zone, x2, y2)

    x1 = converted1[0]
    y1 = converted1[1]
    x2 = converted2[0]
    y2 = converted2[1]

    # CALCULATING INTERMEDIATE POINTS
    intermediate_points = drawLine(x1, y1, x2, y2)

    # CONVERTING TO ZONE M
    final_coordinates = []
    for count in range(len(intermediate_points)):
        x1 = intermediate_points[count][0]
        y1 = intermediate_points[count][1]
        final_coordinates.append(zone0tozoneM(zone, x1, y1))

    # DRAWING THE PIXELS
    for count in range(len(final_coordinates)):
        x = final_coordinates[count][0]
        y = final_coordinates[count][1]
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
    glColor3f(1.0, 1.0, 0.0)  # COLOR SET (RGB)
    # CALL THE DRAW METHODS HERE
    midpointLineAlgorithm(50, 250, 50, 400)
    midpointLineAlgorithm(200, 100, 200, 400)
    midpointLineAlgorithm(300, 100, 300, 400)
    midpointLineAlgorithm(450, 100, 450, 400)

    midpointLineAlgorithm(50, 100, 200, 100)
    midpointLineAlgorithm(50, 250, 200, 250)
    midpointLineAlgorithm(50, 400, 200, 400)
    midpointLineAlgorithm(300, 400, 450, 400)
    midpointLineAlgorithm(300, 250, 450, 250)
    midpointLineAlgorithm(300, 100, 450, 100)

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)  # WINDOW SIZE
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")  # WINDOW NAME
glutDisplayFunc(showScreen)

glutMainLoop()
