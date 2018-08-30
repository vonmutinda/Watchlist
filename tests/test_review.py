import unittest

from app.models import Review

# Review = app.models.Review()

class ReviewTest(unittest.TestCase):
    def setUp(self):
        self.new_review = Review(1234,'Python Must Be Crazy','https://url.com/jpgjskdjf','this is a review')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_review,Review))