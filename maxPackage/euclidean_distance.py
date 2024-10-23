import math
def euclidean_distance(a: tuple, b: tuple) -> tuple:
    """
    Calculate the Euclidean Distance between two tuples.

    Keyword arguments:
    a -- the first point
    b -- the second point
    """
    if len(a) != len(b):
        raise SyntaxError("Tuples a and b should be the same length.")
    

    vector = tuple(b_i - a_i for a_i, b_i in zip(a, b))
    magnitude = math.sqrt(sum((b_i - a_i) ** 2 for a_i, b_i in zip(a, b)))
    return magnitude