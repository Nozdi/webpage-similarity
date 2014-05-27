"""
.. module:: compare
    :synopsis: This module provides fuzzy comparison between two images
"""

import heapq
from similarity.img.extract import (
    get_fuzzy_colors,
    get_fuzzy_brightness,
    get_fuzzy_size,
)
from similarity.fuzzy import jaccard


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
    weight = len(img_list1)

    for img1 in img_list1:
        for img2 in img_list2:
            results.append(compare(img1, img2))

    # for correct result when comparing lists of the same images
    return sum(heapq.nlargest(weight, results)) / weight
