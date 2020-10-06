from turtle import distance
from point import *
from math import gcd
from graph import *

p1 = Point(1,1)
p2 = Point(2,2)
print(p1 == p2)

print(-42%39)
print(gcd(-42,39))

print(hash((2, 2)))
print({
    Point(1,1):[Point(2,2)],
    Point(2,2):[Point(3,3),Point(1,1)],
    Point(3,3):[]
})

print({
    (1,1):[(2,2)],
    (2,2):[(3,3),(1,1)],
    (3,3):[]
})

print(Graph().addNode("A")==Graph().addNode("A"))
g = Graph()
print(g.graph)
g.addNode("B")
print(g.graph)

d = {
    (1,1):[(2,2)],
    (2,2):[(3,3),(1,1)],
    (3,3):[]
}
print(d[(1,1)])

import matplotlib.pyplot as plt
x_coordinates = [1, 2, 3, 2]
y_coordinates = [1, 2, 1, 1]

plt.scatter(x_coordinates, y_coordinates)
plt.plot(x_coordinates, y_coordinates)
plt.show()


