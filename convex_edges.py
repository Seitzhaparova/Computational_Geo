#We'll consider the set of points P = {(0,0),(1,2),(2,1),(3,3),(4,0),(2,−1)}
#Although this algorithm is slow and uneffective, it's beneficial to write it so we understand the concept
# Pseudocode of algorithm
# ---input: a set of points P in the plane
# ---output: a list L containing the vertices of CH(P) in clockwise order
# 1. E <- /0
# 2. for all ordered pairs (p,q) ∈ P x P with p!=q
# 3.      do valid <- true
# 4.      for all points r ∈ P not equal to p and q
# 5.             do if r lies to the left of the directed line from p to q
# 6.                      then valid <- false
# 7.      if valid then Add the directed edge pq to E
# 8. From set E of edges contruct a list L of vertices of CH(P) sorted in clockwise order
def cross_product(p,q,r):
    return ((q[0]-p[0])*(r[1]-p[1]) - (q[1]-p[1])*(r[0]-p[0]))

def slow_convex_hull(P):
    E = set()
    n = len(P)

    for i in range(n):
        for j in range(n):
            if i != j:
                p, q = P[i], P[j]
                valid = True
                for k in range(n):
                    if k != i and k != j:
                        r = P[k]
                        if cross_product(p,q,r) > 0:
                            valid = False
                            break
                if valid:
                    E.add((p,q))
    L = []
    if E:
        edge = list(E)[0] #we take very first edge in E 
        p = edge[0]
        while edge:
            L.append(p)
            next_p = edge[1]
            E.remove(edge)
            for e in E:
                if e[0] == next_p:
                    edge = e
                    break
                elif e[1] == next_p:
                    edge = (e[1], e[0]) 
                    break
            else:
                break #if no connecting edge found
            p = next_p
    return L

points  = [(0,0),(1,2),(2,1),(3,3),(4,0),(2,-1)]
convex_hull_vertices = slow_convex_hull(points)
print("Convex vertices: ", convex_hull_vertices)