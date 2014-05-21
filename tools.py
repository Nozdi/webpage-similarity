#!/usr/bin/env python
import codecs
from glob import glob
from unidecode import unidecode


if __name__ == '__main__':
    files = glob("./texts/*/*.txt")
    for filename in files:
        with codecs.open(filename, "r+", encoding="utf-8") as f:
            new_text = unicode(f.read())
            f.seek(0)
            f.truncate()
            f.write(new_text)
