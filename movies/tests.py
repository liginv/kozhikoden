from django.test import TestCase
from movies.models import Movie
# Create your tests here.


class MovieTests(TestCase):
    """ Movie Model Tests."""

    def test_str(self):
        mov_name = Movie(movie_name='The Jungle Book')

        self.assertEquals(
                          str(mov_name),
                          'The Jungle Book'
                          )
