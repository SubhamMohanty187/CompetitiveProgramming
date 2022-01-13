def catAndMouse(x, y, z):
    d1 = abs(x-z) #distance of cat1 from mouse
    d2 = abs(y-z) #distance of cat2 from mouse
    if d1 < d2:
        return "Cat A"
    elif d1 > d2:
        return "Cat B"
    else:
        return "Mouse C"
