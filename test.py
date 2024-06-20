#test git bash
def right_or_left_turn(p1, p2, p3):
    print("Last three points: ", p1, p2, p3)
    cross_product = (p2[0] - p1[0]) * (p3[1] - p2[1]) - (p2[1] - p1[1]) * (p3[0] - p2[0])
    right = cross_product < 0  # Change to strictly less than for right turn
    print("Cross product: ", cross_product, " Right turn: ", right)
    return right

def convex_hull(points):
    L_upper = []
    L_lower = []
    n = len(points)
    
    # Constructing the upper part of the hull
    L_upper.append(points[0])
    L_upper.append(points[1])
    print("Initial L_upper: ", L_upper)
    
    for i in range(2, n):
        L_upper.append(points[i])
        while len(L_upper) > 2 and not right_or_left_turn(L_upper[-3], L_upper[-2], L_upper[-1]):
            del L_upper[-2]
            print("L(U) after deletion: ", L_upper)
    print("Final L(U): ", L_upper)
    
    # Constructing the lower part of the hull
    L_lower.append(points[-1])
    L_lower.append(points[-2])
    print("Initial L(L): ", L_lower)
    
    for i in range(n-3, -1, -1):
        L_lower.append(points[i])
        while len(L_lower) > 2 and right_or_left_turn(L_lower[-3], L_lower[-2], L_lower[-1]):
            del L_lower[-2]
            print("L(L) after deletion: ", L_lower)
    
    # Removing the first and last point of L_lower to avoid duplication with L_upper
    L_lower = L_lower[1:-1]
    print("Final L(L): ", L_lower)
    
    # Combine upper and lower parts to get the full convex hull
    convex_hull_vertices = L_upper + L_lower
    return convex_hull_vertices

P = [(0, 0), (1, 2), (2, 1), (3, 3), (4, 0), (2, -1)]
sorted_points = sorted(P, key=lambda point: (point[0], point[1]))
print('Sorted points: ', sorted_points)
convex_hull_vertices = convex_hull(sorted_points)
print("Convex vertices: ", convex_hull_vertices)
