"""
.. module:: compare
    :synopsis: This module provides fuzzy comparison between two images
"""

from similarity.img.extract import (
    get_fuzzy_colors,
    get_fuzzy_brightness,
    get_fuzzy_size,
)
from similarity.fuzzy import jaccard
from similarity.fuzzy import algebraic_sum


def get_properties(image):
    properties = get_fuzzy_colors(image)
    properties["brightness"] = get_fuzzy_brightness(image)
    properties.update(get_fuzzy_size(image))
    return properties


def compare(image1, image2):
    return jaccard(
        get_properties(image1),
        get_properties(image2),
        min,
        max
    )


def compare_many(img_list1, img_list2):
    results = []
    temp = []
    detailed_results = {}

    for img1 in img_list1:
        for img2 in img_list2:
            compared = compare(img1[1], img2[1])
            temp.append(compared)
            detailed_results[(img1[0], img2[0])] = compared

        result = max(temp)
        results.append(result)

        temp = []

    #return reduce(lambda x, y: x * y, results)
    #return reduce(lambda x, y: algebraic_sum(x, y), results)
    return sum(results) / len(results), detailed_results
