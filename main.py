import math
import geometry

# Sample rectangle info
xmin = -350
xmax = 350
ymin = -250
ymax = 250

# Sample circle info
r = 80
xcenter = -300
ycenter = 220

area = geometry.circleRectangleIntersectionArea(r, xcenter, ycenter, xmin, xmax, ymin, ymax)

print area
