"""
.. module:: extract
    :synopsis: This module provides data extraction from image
"""
from __future__ import division
from fuzzy.storage.fcl.Reader import Reader

import os
from PIL import (
    Image,
    ImageStat,
)


def get_fuzzy_size(image):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    controller = Reader().load_from_file(
        "{}/size.fcl".format(current_dir)
    )

    width, height = image.size

    input_variables = {
        "width": width,
        "height": height
    }
    output_variables = {
        "size": None
    }
    controller.calculate(input_variables, output_variables)
    return output_variables


def get_fuzzy_colors(image):
    keys = list(image.mode)
    colors = dict.fromkeys(keys, 0)
    stats = ImageStat.Stat(image)
    for key, value in zip(keys, stats.mean):
        colors[key] = value / 255
    return colors


def get_fuzzy_brightness(image):
    stats = ImageStat.Stat(image.convert('L'))
    return stats.rms[0] / 100


if __name__ == '__main__':
    im = Image.open("../../red.jpg")
    print(get_fuzzy_colors(im))
    print(get_fuzzy_brightness(im))
    get_fuzzy_size(im)
