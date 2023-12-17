
def FuzzyOperation(zipped_sets , Predicator):
    Predication = []
    for zipped_set in list(zipped_sets):
        Predication.append(Predicator(zipped_set))
    return Predication

# calculate min & max of given fuzzy sets

A = [0.2, 0.4, 0.6, 0.8]
B = [0.1, 0.3, 0.5, 0.7]
C = [0.2, 0.3, 0.4, 0.5]

# Union
print(FuzzyOperation(zip(A, B, C), max))

# Intersection
print(FuzzyOperation(zip(A, B, C), min))
