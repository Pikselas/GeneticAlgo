
def Triangular(x , lower , center , upper):
    if x <= lower:
        return 0
    elif x > lower and x <= center:
        return (x - lower) / (center - lower)
    elif x > center and x <= upper:
        return (upper - x) / (upper - center)
    else:
        return 0

def Trapezoidal(x , lower , center1 , center2 , upper):
    if x <= lower:
        return 0
    elif x > lower and x <= center1:
        return (x - lower) / (center1 - lower)
    elif x > center1 and x <= center2:
        return 1
    elif x > center2 and x <= upper:
        return (upper - x) / (upper - center2)
    else:
        return 0

def Gaussian(x , center , width , fuzzification_factor):
    return math.exp( ( ( (x - center) / width ) ** fuzzification_factor) / -2 )
