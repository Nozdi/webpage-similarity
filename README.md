webpage-similarity
==================

Create objects and pickle:
```
$[i]python
>>> from similarity.text.train import *
>>> dump_objects(create_categories_with_documents(), "cats")
>>> dump_objects(create_terms_to_categories_relevance(), "db")
```

Install
```
MAC:
[sudo] port install antlr3 graphviz gnuplot
Debian/Ubuntu:
[sudo] apt-get install antlr3 graphviz gnuplot
```

Install python dependencies:
```
pip install -r requirements.txt [--allow-all-external --allow-unverified antlr-python-runtime --allow-unverified gnuplot-py]
```
If any problems install packages from system utils (port, brew, apt-get, yum, ...)


Install pyfuzzy:
```
svn checkout svn://svn.code.sf.net/p/pyfuzzy/code/trunk pyfuzzy-code
cd pyfuzzy-code/pyfuzzy
python setup.py install
```
