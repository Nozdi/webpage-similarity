#!/usr/bin/env python
import codecs
import os
from glob import glob
from unidecode import unidecode
import os


def get_all_files():
    """
    :returns: list with all textes
    """
    return glob("./texts/*/*.txt")


def files():
    """
    :yields: file -- current text from all texts
    """
    files = get_all_files()
    for filename in files:
        with codecs.open(filename, "r+", encoding="utf-8") as f:
            yield f


def remove_unicode():
    """
    Removes unicode characters
    """
    for f in files():
        new_text = unidecode(f.read())
        f.seek(0)
        f.truncate()
        f.write(new_text)


def count_all():
    """
    :returns: int -- number of files
    """
    return len(get_all_files())


def remove_email_info(sentence=None):
    """
    Removes files with sentence
    """
    if not sentence:
        sentence = "An email with a link to: Thanks for sharing About.com with others!"
    files_to_delete = []
    for f in files():
        if sentence.split() == f.read().split():
            files_to_delete.append(f.name)

    for filename in files_to_delete:
        os.remove(filename)

#TODO: Kacper
def renumber_files(root_dir):
    for root, subFolders, files in os.walk(root_dir):
        counter = 0
        for file in files:
            counter+=1
            old_file = os.path.join(root, file)
            new_file = os.path.join(root, str(counter)  + ".txt")
            os.rename(old_file, new_file)


if __name__ == '__main__':
    remove_unicode()
    print(count_all())
    # remove_email_info()
