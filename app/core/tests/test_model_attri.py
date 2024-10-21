"""
This Module contains all test for models.
"""

from core.models import Movie, UserCollection
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """
    This class contains all tests for models.
    """

    def test_create_movie(self):
        """
        Test creating a new movie.
        """

        movie = Movie.objects.create(
              movie_id=1,
              title="Toy Story",
              genres="Animation|Children's|Comedy"
          )

        self.assertEqual(movie.movie_id, 1)
        self.assertEqual(movie.title, "Toy Story")
        self.assertEqual(movie.genres, "Animation|Children's|Comedy")
        self.assertEqual(movie.__str__(), movie.title)
        self.assertEqual(Movie.objects.count(), 1)

    def test_create_movie_collection(self):
        """
        Test creating a new movie collection.
        (e,g, My Favorites, whatlist, etc.)
        """

        user = get_user_model().objects.create_user(
            email="user4@example.com",
            password="testpass123"
        )

        movie1 = Movie.objects.create(
            movie_id=1,
            title="Toy Story",
            genres="Animation|Children's|Comedy"
        )

        movie2 = Movie.objects.create(
            movie_id=2,
            title="Toy Story 2",
            genres="Animation|Children's|Comedy"
        )

        collection = UserCollection.objects.create(
            user=user,
            name="My Favorites"
        )
        collection.movies.add(movie1, movie2)

        self.assertEqual(collection.name, "My Favorites")
        self.assertIn(movie1, collection.movies.all())
        self.assertIn(movie2, collection.movies.all())
        self.assertEqual(collection.movies.count(), 2)
