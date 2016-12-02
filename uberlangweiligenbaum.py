"""Growing Tree Animation

    Boring a boring tree.
"""

from cs1graphics import *
from time import sleep

paper_from = Color((30, 29, 29))
paper_to = Color('white')
paper = Canvas(500, 500, title='School of Hacking, 케이MIT')
paper.setBackgroundColor(paper_from)

from math import cos, sin, degrees, radians

def gradient(fr, to, t):
    fr = fr.getColorValue()
    to = to.getColorValue()
    r, g, b = fr[0]*(1-t) + to[0]*t, fr[1]*(1-t) + to[1]*t, fr[2]*(1-t) + to[2]*t

    return Color((r, g, b))

sun_from = Color('white')
sun_to = Color((255, 111, 86))
sun = Circle(40, Point(440, 60))
sun.setFillColor(sun_from)
sun.setBorderColor('transparent')
paper.add(sun)

sleep(1)

for f in range(0, 40+1):
    sleep(.01)
    sun.setFillColor(gradient(sun_from, sun_to, f/40))
    paper.setBackgroundColor(gradient(paper_from, paper_to, f/40))

sleep(1)

def draw_tree():
    n = 2
    depth = 5
    spread_angle = 23
    trunk_length = 100
    length = 50
    length_scalar = 0.9
    tree_color = Color((140, 126, 92))
    leaf_color = Color((78, 178, 110))

    points = []
    angles = []
    paths = []
    leaves = []
    circles = []

    angles.append(90)
    points.append(Point(250, 500))

    # Tree trunk
    theta = angles[0]
    angles.append(theta)
    theta = radians(-theta)
    x, y = trunk_length, 0
    x, y = x*cos(theta) - y*sin(theta), x*sin(theta) + y*cos(theta)
    x += points[0].getX()
    y += points[0].getY()
    points.append(Point(x, y))
    paths.append(Path(points[0], points[1]))
    paths[-1].setBorderColor(tree_color)
    paths[-1].setBorderWidth(2)
    paths[-1].scale(.1)

    paper.add(paths[-1])

    #depth_text = Text('0', 18, Point(250, 30))
    #depth_text.setFontColor('red')
    #paper.add(depth_text)

    prev_s = .1
    maxs = 50
    for s in range(0, maxs): # .5s
        sleep(.01)
        cur_s = (s+1)/maxs
        paths[0].scale(1/prev_s)
        paths[0].scale(cur_s)
        prev_s = cur_s

    # Branches
    for d in range(depth):
        #depth_text.setMessage(str(d+1))

        for i in range(2**d):
            l = length * length_scalar**d
            
            par_idx = len(points)//n
            par_point = points[par_idx]
            par_angle = angles[par_idx]
            
            # First child
            theta = par_angle - spread_angle
            angles.append(theta)
            
            theta = radians(-theta)
            x, y = l, 0
            x, y = x*cos(theta) - y*sin(theta), x*sin(theta) + y*cos(theta)
            x += par_point.getX()
            y += par_point.getY()
            
            points.append(Point(x, y))
            paths.append(Path(points[par_idx], points[-1]))
            paths[-1].setBorderColor(tree_color)
            paths[-1].setBorderWidth(2)
            paths[-1].scale(.1)

            if d >= 3:
                leaves.append((points[-1] - points[par_idx])*(1/3) + points[par_idx])
                leaves.append((points[-1] - points[par_idx])*(1/3)*2 + points[par_idx])
                leaves.append(points[-1])

            paper.add(paths[-1])
            
            # Second child
            theta = par_angle + spread_angle
            angles.append(theta)
            
            theta = radians(-theta)
            x, y = l, 0
            x, y = x*cos(theta) - y*sin(theta), x*sin(theta) + y*cos(theta)
            x += par_point.getX()
            y += par_point.getY()
            
            points.append(Point(x, y))
            paths.append(Path(points[par_idx], points[-1]))
            paths[-1].setBorderColor(tree_color)
            paths[-1].setBorderWidth(2)
            paths[-1].scale(.1)

            if d >= 3:
                leaves.append((points[-1] - points[par_idx])*(1/3) + points[par_idx])
                leaves.append((points[-1] - points[par_idx])*(1/3)*2 + points[par_idx])
                leaves.append(points[-1])

            paper.add(paths[-1])

        prev_s = .1
        maxs = int(l/length*10)+1
        for s in range(0, maxs): # .5s
            sleep(.01)
            cur_s = (s+1)/maxs
            for i in range(2**(d+1)):
                paths[-i-1].scale(1/prev_s)
                paths[-i-1].scale(cur_s)
            prev_s = cur_s

    for i in range(len(leaves)):
        c = Circle(1, leaves[i])
        c.setFillColor(leaf_color)
        c.setBorderWidth(0)
        circles.append(c)
        paper.add(circles[-1])

    import random

    random.shuffle(circles)

    for r in range(2, 5): # .5s
        for i in range(0, len(circles), 30):
            sleep(.01)
            for j in range(i, min(i+30, len(circles))):
                circles[j].setRadius(r)

"""
    for i in range(len(paths)):
        paper.add(paths[i])"""

def draw_animal():
    draw_tree()

def show_animation():
    # - But... but drawing and animating is done simultaneously.
    # - WTF? Are you what? A Nazi?
    # - No!... No, absolutely not...
    # - ...
    # - But I want to seize the means of production...
    pass

draw_animal()
show_animation()

"""
for theta in range(0, 180, 15):
    paper.clear()
    draw_tree()
    sleep(0.01)
    """
