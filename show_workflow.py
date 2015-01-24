from similarity.text.document import AnalizedDocument

if __name__ == '__main__':
    text = """
    A hedgehog is any of the spiny mammals of the subfamily Erinaceinae,
    which is in order Erinaceomorpha. There are seventeen species of
    hedgehog in five genera, found through parts of Europe, Asia, Africa and New Zealand.
    """

    ad = AnalizedDocument(text)
    print ad.terms_quantity
    for term in ad.terms_quantity:
        print "Term:", term
        for cat, items in sorted(
            ad.terms_relevance.items(),
            key=lambda x: x[1].get(term), reverse=True
        ):
            relevance = items.get(term, 0)
            if relevance:
                print "\t", cat, ":", relevance

    print '-'*100

    ad.calculate_terms_membership()
    print ad.terms_membership

    print '-'*100
    ad.calculate_membership_to_categories()

    for cat, value in sorted(
        ad.categories_membership.items(),
        key=lambda x: x[1], reverse=True
    ):
        print cat, ':', value
