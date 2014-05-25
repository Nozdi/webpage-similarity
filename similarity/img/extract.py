"""
.. module:: extract
    :synopsis: This module provides data extraction from image
"""
from __future__ import division
from PIL import (
    Image,
    ImageStat,
)


def get_fuzzy_colors(image):
    keys = list(image.mode)
    colors = dict.fromkeys(keys, 0)
    stats = ImageStat.Stat(image)
    for key, value in zip(keys, stats.mean):
        colors[key] = value/255
    return colors


def get_fuzzy_brightness(image):
    stats = ImageStat.Stat(image.convert('L'))
    return stats.rms[0]/100


def get_size(image):
    return image.size


if __name__ == '__main__':
    im = Image.open("../../red.jpg")
    print(get_fuzzy_colors(im))
    print(get_fuzzy_brightness(im))
