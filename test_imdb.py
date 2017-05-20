from imdb_crawler import IMDB_top_movies
import pytest
import requests

class test_IMDB_top_movies:

	tester = IMDB_top_movies('5fc60de', 'ImdbTopMovies.csv', 'http://www.imdb.com/chart/top?ref=ft_250')

	def test_imdb_id_crawler():
		self.tester.imdb_id_crawler()

	def test_imdb_id_crawler_failure():
		assert self.tester.imdb_id_crawler() == ['tt0111161']

	def test_api_correct():
		api = self.tester.omdb_api_details()
		assert api == '5fc60de'

	def test_api_failure():
		api = self.tester.omdb_api_details()
		assert api == 'abs178'

	def test_api_failure_raises_exception():
	    with pytest.raises(TypeError):
	    	self.tester.omdb_api_details(5.5)