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


def get_properties(image):
    properties = get_fuzzy_colors(image)
    properties["brightness"] = get_fuzzy_brightness(image)
    properties["size"] = get_fuzzy_size(image)
    return properties


def compare(image1, image2):
    return jaccard(
        get_properties(image1),
        get_properties(image2),
        min,
        max
    )
