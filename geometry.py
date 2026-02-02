import math

def rectangle(a,b):
    return a*b

def triangle(a,b):
    return a*b/2

def circle_area_from_radius(a):
    return math.pi*(a**2)

def circle_area_from_diameter(a):
    return math.pi*((a/2)**2)

def circle_area_from_circumference(a):
    return math.pi*((a/(math.pi*2))**2)

