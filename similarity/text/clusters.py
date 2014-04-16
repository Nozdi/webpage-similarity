"""
.. module:: clusters
    :synopsis: This module provides document clustering
"""
from __future__ import unicode_literals

from glob import glob
from os import path
from similarity.text.document import TrainingDocument

import numpy


def vectorspaced(document, all_terms):
    """
        :param document: document object
        :type document: TrainingDocument
        :returns: distance vector
    """
    return numpy.array([
        document.termsWithWeights.get(word, 0)
        for word in all_terms
    ])


def cluster_documents(directory, regex, clusterer, *args, **kwargs):
    """
        :param directory: directory with documents
        :type directory: string
        :param regex: regex to search in directory
        :type regex: string
        :param clusterer: choosen clusterer
        :type clusterer: nltk.cluster class
        :returns: None
    """
    files = glob(path.join(directory, regex))

    documents = []
    for filename in files:
        with open(filename) as f:
            documents.append(
                TrainingDocument(name=filename, text=f.read().decode("utf-8"))
            )

    # is it magic?
    all_terms = set(
        reduce(list.__add__, map(lambda d: d.termsWithWeights.keys(), documents))
    )

    cluster = clusterer(*args, **kwargs)

    vectors = [vectorspaced(doc, all_terms) for doc in documents]
    cluster.cluster(vectors)

    classified = [cluster.classify(vector) for vector in vectors]
    for cluster_id, doc in sorted(zip(classified, documents)):
        print cluster_id, doc
