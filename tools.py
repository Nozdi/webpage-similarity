#!/usr/bin/env python
import codecs
from glob import glob
from unidecode import unidecode


def get_all_files():
    return glob("./texts/*/*.txt")


def remove_unicode():
    files = get_all_files()
    for filename in files:
        with codecs.open(filename, "r+", encoding="utf-8") as f:
            new_text = unidecode(f.read())
            f.seek(0)
            f.truncate()
            f.write(new_text)


if __name__ == '__main__':
    remove_unicode()
