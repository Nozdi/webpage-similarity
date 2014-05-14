"""
.. module:: fuzzy
    :synopsis: This module provides fuzzy logic functions
"""


def algebraic_sum(x, y):
    return x + y - x * y


def algebraic_product(x, y):
    return x * y


def jaccard(dictA, dictB, product_function, sum_function):
    default = 0.0
    numerator = 0.0
    denumerator = 0.0
    for term in dictA:
        numerator += product_function(
            dictA.get(term, default),
            dictB.get(term, default)
        )

        denumerator += sum_function(
            dictA.get(term, default),
            dictB.get(term, default)
        )
    return numerator / denumerator
