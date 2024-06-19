#In this code we'll try to implement pseusocode of the incremental algorithm of constructing CH(P)
# Algorithm Convex Hull Increment Development
# ---input:  a set of points P in the plane
# ---output: a list containing the vertices CH(P) in clockwise order
# 1. Sort the points by x-coordinate resulting in new sequence of points {p1,p2,...,pn}
# 2. Put the points p1a and p2 in Lupper, with p1 as the first point
# 3. for i<- 3 to n
# 4.      do append pi to Lupper
# 5.          while Lupper contains more than two points and the last three points in Lupper do not make a right turn
# 6.             do delete the middle of the last three points from Lupper
# 7. Put the point pn to p(n-1) in a list Llower with pn as the first point
# 8. for i<-n-2 downto 1
# 9.      do append pi to Llower
# 10.         while Llower contains more than 2 points and the last three points in Llower do not make a right turn
# 11.             do delete the middle of the last three points from Llower
# 12. Remove the first and the last point from Llower to avoid duplication of the points where the upper and the lower hulls meet
# 13. Append Llower to Lupper and call the resulting list L
# 14. Return L
#Cross product is (dx1*dy2) - (dy1*dx2)
#where dx1 = x2 - x1, dy2 = y3 -y2, dy1 = y2 - y1, dx2 = x3 - x2
def right_or_left_turn(p1,p2,p3):
    right = True
    print("Last three points: ", p1,p2,p3 )
    if ((p2[0] - p1[0])*(p3[1]-p2[1]) - (p2[1]-p1[1])*(p3[0]-p2[0])) >= 0:
        right = False
    print("Cross product: ", ((p2[0] - p1[0])*(p3[1]-p2[1]) - (p2[1]-p1[1])*(p3[0]-p2[0])), right)
    return right

def convex_hull(points):
    L_upper = []
    L_lower = []
    n= len(points)
    L_upper.append(points[0]), L_upper.append(points[1])
    print("L_upper: ", L_upper)
    for i in range(2, n):
        L_upper.append(points[i])
        while len(L_upper) > 2 and right_or_left_turn(L_upper[len(L_upper)-3], L_upper[len(L_upper)-2],L_upper[len(L_upper)-1] ) == False:
            del L_upper[len(L_upper)-2]
            print("L(U) after deletion: ", L_upper)
    print("Final L(U): ", L_upper)
    L_lower.append(points[n-1]), L_lower.append(points[n-2])
    print("Initial L(L): ", L_lower)
    for i in range(n-3, -1, -1):
        L_lower.append(points[i])
        while len(L_lower) > 2 and right_or_left_turn(L_lower[len(L_lower)-3], L_lower[len(L_lower)-2],L_lower[len(L_lower)-1] ) == False:
            del L_lower[len(L_lower)-2]
            print("L(L) after deletion: ", L_lower)
    L_lower = L_lower[1:-1]
    print("Final L(L): ", L_lower)
    L = L_upper + L_lower
    return L

P = [(0,0),(1,2),(2,1),(3,3),(4,0),(2,-1)] #For learning purposes let's take the same set of points as in previous algorithm
sorted_points =  sorted(P, key = lambda point: (point[0], point[1]))
print('Sorted points: ', sorted_points)
convex_hull_vertices = convex_hull(sorted_points)
print("Convex vertices: ", convex_hull_vertices)

