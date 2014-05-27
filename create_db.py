#!/usr/bin/env python

from similarity.serialization import dump_objects
from similarity.text.train import (
    create_categories_with_documents,
    create_terms_to_categories_relevance,
)

dump_objects(create_categories_with_documents(), './data/cats')
dump_objects(create_terms_to_categories_relevance(), './data/db')
