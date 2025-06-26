from math import dist
from random import random
from turtle import *
def visual(cls):
    screensize(10000, 10000); up(); tracer(0)
    for cl in cls:
        col = (random(), random(), random())
        [goto(p[0] * 80, p[1] * 80) or dot(10, col) for _, p in cl]
    done()
a = [list(map(float, x.replace(',','.').split())) for x in open('27.txt')]
c = []
while a:
    c += [[[0, a.pop()]]]
    for s, p1 in c[-1]:
        for p in a:
            if dist(p1, p) < 1:
                s = 0
                for n in c[-1]:
                    d = dist(p, n[1])
                    n[0] += d
                    s += d
                c[-1].append([s,p])
cents = [min(c1) for c1 in c]
print(sum(c[1][0] for c in cents)/len(cents) * 10000, sum(c[1][1] for c in cents) * 10000)
visual(cls)