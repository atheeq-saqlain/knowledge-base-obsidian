import math

def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

def section(A, B, m1, m2):
    x = (m1 * B[0] + m2 * A[0]) / (m1 + m2)
    y = (m1 * B[1] + m2 * A[1]) / (m1 + m2)
    return (x, y)

def area(A, B, C):
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2

print("7.1.1", dist((2, 3), (4, 1)), dist((-5, 7), (-1, 3)))
a, b = 2, 3
print("7.1.1iii symbolic 2sqrt(a^2+b^2)", dist((a, b), (-a, -b)))
print("7.1.2", dist((0, 0), (36, 15)))
print("7.1.4", dist((5, -2), (6, 4)), dist((6, 4), (7, -2)), dist((5, -2), (7, -2)))
print(
    "7.1.5",
    [dist(p, q) for p, q in [((3, 4), (6, 7)), ((6, 7), (9, 4)), ((9, 4), (6, 1)), ((6, 1), (3, 4))]],
    dist((3, 4), (9, 4)),
    dist((6, 7), (6, 1)),
)
pts = [(-1, -2), (1, 0), (-1, 2), (-3, 0)]
print("7.1.6i", [dist(pts[i], pts[(i + 1) % 4]) for i in range(4)], dist(pts[0], pts[2]), dist(pts[1], pts[3]))
pts = [(-3, 5), (3, 1), (0, 3), (-1, -4)]
print("7.1.6ii", [dist(pts[i], pts[(i + 1) % 4]) for i in range(4)], dist(pts[0], pts[2]), dist(pts[1], pts[3]))
pts = [(4, 5), (7, 6), (4, 3), (1, 2)]
print("7.1.6iii", [dist(pts[i], pts[(i + 1) % 4]) for i in range(4)], dist(pts[0], pts[2]), dist(pts[1], pts[3]))
print("7.1.9", dist((0, 1), (4, 6)), dist((5, -3), (4, 6)), dist((5, -3), (-4, 6)))

print("7.2.1", section((-1, 7), (4, -3), 2, 3))
print("7.2.2", section((4, -1), (-2, -3), 1, 2), section((4, -1), (-2, -3), 2, 1))
print("7.2.3", dist((2, 25), (8, 20)), section((2, 25), (8, 20), 1, 1))
print("7.2.5", section((1, -5), (-4, 5), 1, 1))
print("7.2.7", (3, -10))
print("7.2.8", section((-2, -2), (2, -4), 3, 4))
print("7.2.9", section((-2, 2), (2, 8), 1, 3), section((-2, 2), (2, 8), 1, 1), section((-2, 2), (2, 8), 3, 1))
A, B, C, D = (3, 0), (4, 5), (-1, 4), (-2, -1)
print("7.2.10", dist(A, C), dist(B, D), dist(A, C) * dist(B, D) / 2)

print("7.3.1", area((2, 3), (-1, 0), (2, -4)), area((-5, -1), (3, -5), (5, 2)))
A, B, C = (0, -1), (2, 1), (0, 3)
Mab, Mbc, Mca = section(A, B, 1, 1), section(B, C, 1, 1), section(C, A, 1, 1)
print("7.3.3", Mab, Mbc, Mca, area(Mab, Mbc, Mca), area(A, B, C))
print("7.3.4", area((-4, -2), (-3, -5), (3, -2)) + area((-4, -2), (3, -2), (2, 3)))
A, B, C = (4, -6), (3, -2), (5, 2)
M = section(B, C, 1, 1)
print("7.3.5", M, area(A, B, M), area(A, C, M))

print("7.4.6", area((4, 6), (1, 5), (7, 2)), area((4, 6), (1, 5), (7, 2)) / 16)
A, B, C = (4, 2), (6, 5), (1, 4)
D = section(B, C, 1, 1)
P = section(A, D, 2, 1)
E = section(A, C, 1, 1)
Q = section(B, E, 2, 1)
F = section(A, B, 1, 1)
R = section(C, F, 2, 1)
print("7.4.7", D, P, Q, R)
A, B, C, D = (-1, -1), (-1, 4), (5, 4), (5, -1)
P, Q, R, S = section(A, B, 1, 1), section(B, C, 1, 1), section(C, D, 1, 1), section(D, A, 1, 1)
print("7.4.8", P, Q, R, S, dist(P, Q), dist(Q, R), dist(R, S), dist(S, P), dist(P, R), dist(Q, S))
