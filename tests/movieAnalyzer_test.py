import pytest
import sys, os
sys.path.insert(1, os.getcwd())
from src.movieAnalyzer import pd, get_movies_interval, get_rating_popularity_stats, get_actor_movies_release_year_range, get_actor_median_rating, get_directors_median_reviews

class TestMovieAnalyzer:
    def test_get_movies_interval(self):
        movies = get_movies_interval(1992, 1993)
        assert movies[88] == 'Reservoir Dogs'
        assert movies[131] == 'Unforgiven'
        assert movies[5] == 'Schindler\'s List'
        assert movies.count() == 6

    def test_get_movies_interval_error(self):
        with pytest.raises(ValueError):
            movies = get_movies_interval(2092, 1993)

    def test_get_rating_popularity_stats_error(self):
        assert get_rating_popularity_stats('Name', 'mean') == 'Invalid index or type'

    def test_get_rating_popularity_median_1(self):
        assert get_rating_popularity_stats('Rating', 'median') == '8.30'

    def test_get_rating_popularity_median_2(self):
        assert get_rating_popularity_stats('Popularity Index', 'median') == '673.00'

    def test_get_rating_popularity_count_1(self):
        assert get_rating_popularity_stats('Rating', 'count') == '207.00'

    def test_get_rating_popularity_count_2(self):
        assert get_rating_popularity_stats('Popularity Index', 'count') == '207.00'

    def test_get_rating_popularity_mean_1(self):
        assert get_rating_popularity_stats('Rating', 'mean') == '8.34'

    def test_get_rating_popularity_mean_2(self):
        assert get_rating_popularity_stats('Popularity Index', 'mean') == '1091.92'

    def test_get_rating_popularity_min_1(self):
        assert get_rating_popularity_stats('Rating', 'min') == '8.10'

    def test_get_rating_popularity_min_2(self):
        assert get_rating_popularity_stats('Popularity Index', 'min') == '3.00'

    def test_get_rating_popularity_max_1(self):
        assert get_rating_popularity_stats('Rating', 'max') == '9.30'

    def test_get_rating_popularity_max_2(self):
        assert get_rating_popularity_stats('Popularity Index', 'max') == '4940.00'

    def test_get_actor_movies_release_year_range(self):
        assert get_actor_movies_release_year_range('Brad Pitt', 2010, 1990).count() == 4
        assert get_actor_movies_release_year_range('Brad Pitt', 2010, 1990)['Fight Club'] == 1999
        assert get_actor_movies_release_year_range('Brad Pitt', 2010, 1990)['Se7en'] == 1995
        assert get_actor_movies_release_year_range('Brad Pitt', 2010, 1990)['Se7en'] == 1995
        assert get_actor_movies_release_year_range('Brad Pitt', 2010, 1990)['Inglourious Basterds'] == 2009

    def test_get_actor_movies_release_year_bad_range(self):
        with pytest.raises(ValueError):
            get_actor_movies_release_year_range('Brad Pitt', 1990, 2010)

    def test_get_actor_movies_release_year_non_actor(self):
        assert get_actor_movies_release_year_range('Koe Kiden', 1990, 1980).empty

    def test_get_actor_movies_release_year_empty_actor(self):
        assert get_actor_movies_release_year_range('', 2000, 1980).empty

    def test_get_actor_median_rating_1(self):
        assert get_actor_median_rating('Al Pacino') == 8.65

    def test_get_actor_median_rating_2(self):
        assert get_actor_median_rating('Marlon Brando') == 8.5

    def test_get_actor_median_rating_None(self):
        assert get_actor_median_rating('Jojo Hatter') == None

    def test_get_actor_median_rating_empty(self):
        with pytest.raises(ValueError):
            get_actor_median_rating('')

    def test_get_actor_median_rating_non_string(self):
        with pytest.raises(TypeError):
            get_actor_median_rating(['Al Pacino'])

    def test_get_directors_median_reviews_1(self):
        assert "{:.2f}".format(get_directors_median_reviews()['Alfred Hitchcock']) == '0.40'

    def test_get_directors_median_reviews_2(self):
        assert "{:.2f}".format(get_directors_median_reviews()['Stanley Kubrick']) == '0.66'

    def test_get_directors_median_reviews_3(self):
        assert "{:.2f}".format(get_directors_median_reviews().mean()) == '0.62'

    def test_get_directors_median_reviews_4(self):
        assert "{:.2f}".format(get_directors_median_reviews().sum()) == '79.67'
