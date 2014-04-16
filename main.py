#!/usr/bin/env python
"""
.. module:: main
    :synopsis: This module shows example usage
"""

from similarity.text.document import TrainingDocument
from similarity.text.clusters import cluster_documents

from nltk.cluster import (
    KMeansClusterer,
    GAAClusterer,
    euclidean_distance,
)

doc = TrainingDocument(name="Test", text="To jest taki, a nie inny tekst. TO jest to.")
doc.calculate_terms_belongness()

print "Lista termow z dokumentu:"
print doc.termsWithWeights.keys()
# print "Zbior termow z dokumemntu (lista bez powtorzen):"
# print doc.uniqueTerms
print "Wagi termow w dokumencie:"
print doc.termsWithWeights
print "Stopien przynaleznosci termow do dokumentu:"
print doc.termsBelongness

cluster_documents("texts/ufo/", "[0-9]*.txt", KMeansClusterer, 2, euclidean_distance)
# cluster_documents("texts/", "*/[0-9]*.txt", KMeansClusterer, 5, euclidean_distance)
