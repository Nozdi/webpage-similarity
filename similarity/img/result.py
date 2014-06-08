class ImageComparisonResult(object):

    def __init__(self, similarity_result, image_pairs_results):
        """
            Used for holding data generated during comparison of two image lists.
        """
        self.similarity_result = similarity_result
        self.image_pairs_results = image_pairs_results