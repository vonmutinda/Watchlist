import unittest

from .models import movie

Movie = movie.Movie

class MovieTest(unittest.TestCase):
    '''
    Test Class for behaviour of Movie Class
    '''
    def setUp(self):
        self.new_movie = Movie(1234,"python's sick","A series that'll left  you sick",'https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)

    # def test__init__(self):
    #     self.assertEqual(self.id,123)
    #     self.assertEqual(self.title,'python\'s sick')
    #     self.assertEqual(self.overview,"A series that'll left  you sick")
    #     self.assertEqual(self.poster,'https://image.tmdb.org/t/p/w500/khsjha27hbs')
    #     self.assertEqual(self.voter_average,123)
    #     self.assertEqual(self.voter_count,20)



    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie,Movie))

if __name__  == '__main__':
    unittest.main()