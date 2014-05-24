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


def count_all():
	return len(get_all_files())


if __name__ == '__main__':
	remove_unicode()
	print(count_all())


def renumber_files(root_dir):
	renumber_files_with_suffix(root_dir, "a")
	renumber_files_with_suffix(root_dir, "")


def renumber_files_with_suffix(root_dir, suffix):
	import os

	dict = {}
	for root, subFolders, files in os.walk(root_dir):
		dict.setdefault(root, 0)
		for file in files:
			dict[root] = dict[root] + 1
			old_file = os.path.join(root, file)
			new_file = os.path.join(root, str(dict[root]) + suffix + ".txt")
			os.rename(old_file, new_file)