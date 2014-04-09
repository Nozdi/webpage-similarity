from __future__ import unicode_literals
import numpy
import nltk
import glob
from os import path
from nltk.cluster import KMeansClusterer, GAAClusterer, euclidean_distance
from nltk.decorators import memoize


@memoize
def normalize_word(word):
    return nltk.stem.snowball.EnglishStemmer().stem(word.lower())


def get_words(titles):
    words = {
        normalize_word(word) for line in titles for word in line.split()
    }
    return list(words)


@memoize
def vectorspaced(title):
    """
    Befor using add vector of all words
    """
    stopwords = nltk.corpus.stopwords.words('english')
    title_components = [normalize_word(word) for word in title.split()]  # << Kacper
    return numpy.array([
        word in title_components and not word in stopwords
        for word in vectorspaced.words], numpy.short)


def get_all_words_from_files(files):
    words = set()
    for filename in files:
        with open(filename) as f:
            for line in f:
                for word in line.split():
                    words.add(normalize_word(word))
    return list(words)


def cluster_documents(directory, clusterer, *args, **kwargs):
    files = glob.glob(path.join(directory, "*/[0-9]*.txt"))
    vectorspaced.words = get_all_words_from_files(files)

    cluster = clusterer(*args, **kwargs)

    vect = [vectorspaced(open(filename).read()) for filename in files]
    cluster.cluster(vect)

    classified = [cluster.classify(v) for v in vect]
    for cluster_id, filename in sorted(zip(classified, files)):
        print cluster_id, filename


if __name__ == '__main__':

    with open('example.txt') as title_file:

        job_titles = [line.strip() for line in title_file.readlines()]

        vectorspaced.words = get_words(job_titles)  # << Kacper

        cluster = KMeansClusterer(7, euclidean_distance, )
        # cluster = GAAClusterer(5)
        vect = [vectorspaced(title) for title in job_titles if title]
        print(vect)
        cluster.cluster(vect)
        classified = [cluster.classify(v) for v in vect]

        for cluster_id, title in sorted(zip(classified, job_titles)):
            print cluster_id, title
