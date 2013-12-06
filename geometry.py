import math

# Finds the area of the intersection between a circle and a rectangle
# http://stackoverflow.com/questions/622287/area-of-intersection-between-circle-and-rectangle
def circleRectangleIntersectionArea(r, xcenter, ycenter, xleft, xright, ybottom, ytop):         
#find the signed (negative out) normalized distance from the circle center to each of the infinitely extended rectangle edge lines,
    d = [0, 0, 0, 0]
    d[0]=(xcenter-xleft)/r
    d[1]=(ycenter-ybottom)/r
    d[2]=(xright-xcenter)/r
    d[3]=(ytop-ycenter)/r
    #for convenience order 0,1,2,3 around the edge.

    # To begin, area is full circle
    area = math.pi*r*r

    # Check if circle is completely outside rectangle, or a full circle
    full = True
    for d_i in d:
        if d_i <= -1:   #Corresponds to a circle completely out of bounds
            return 0
        if d_i < 1:     #Corresponds to the circular segment out of bounds
            full = False

    if full:
        return area

    # this leave only one remaining fully outside case: circle center in an external quadrant, and distance to corner greater than circle radius:
    #for each adjacent i,j
    adj_quads = [1,2,3,0]
    for i in [0,1,2,3]:
        j=adj_quads[i]
        if d[i] <= 0 and d[j] <= 0 and d[i]*d[i]+d[j]*d[j] > 1:
            return 0

    # now begin with full circle area  and subtract any areas in the four external half planes
    a = [0, 0, 0, 0]
    for d_i in d:
        if d_i > -1 and d_i < 1:    
            a[i] = math.asin( d_i )  #save a_i for next step
            area -= 0.5*r*r*(math.pi - 2*a[i] - math.sin(2*a[i])) 

    # At this point note we have double counted areas in the four external quadrants, so add back in:
    #for each adjacent i,j
    
    for i in [0,1,2,3]:
        j=adj_quads[i] 
        if  d[i] < 1 and d[j] < 1 and d[i]*d[i]+d[j]*d[j] < 1 :
            # The formula for the area of a circle contained in a plane quadrant is readily derived as the sum of a circular segment, two right triangles and a rectangle.
            area += 0.25*r*r*(math.pi - 2*a[i] - 2*a[j] - math.sin(2*a[i]) - math.sin(2*a[j]) + 4*math.sin(a[i])*math.sin(a[j]))
    
    return area
