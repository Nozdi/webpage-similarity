#!/usr/bin/env python
import codecs
from glob import glob
from unidecode import unidecode
from os import remove


def get_all_files():
    return glob("./texts/*/*.txt")


def files():
    files = get_all_files()
    for filename in files:
        with codecs.open(filename, "r+", encoding="utf-8") as f:
            yield f


def remove_unicode():
    for f in files():
        new_text = unidecode(f.read())
        f.seek(0)
        f.truncate()
        f.write(new_text)


def count_all():
    return len(get_all_files())


def remove_email_info():
    text = "An email with a link to: Thanks for sharing About.com with others!"
    files_to_delete = []
    for f in files():
        if text.split() == f.read().split():
            files_to_delete.append(f.name)

    for filename in files_to_delete:
        remove(filename)

if __name__ == '__main__':
    remove_unicode()
    print(count_all())
    remove_email_info()
