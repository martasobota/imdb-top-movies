from bs4 import BeautifulSoup
import requests

'''
Part 1: Get data about top 100 movies from http://www.imdb.com/chart/top?ref=ft_250.  
Check each movie link and scrape movie's ID that is a part or URL, 
for  instance: <a  href="/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&amp;pf_rd_p=...  </a> 
The ID of this movie is "tt0111161"   
'''


def imdb_crawler():
	imdb_url = 'http://www.imdb.com/chart/top?ref=ft_250'
	r_imdb = requests.get(imdb_url)
	imdb_content = r_imdb.text
	soup = BeautifulSoup(imdb_content, 'lxml')

	top_100_ids_list = []

	# getting id's of top 100 movies
	movies_ids = soup.find_all('td', {'class' : 'titleColumn'})[:100]

	for movie_id in movies_ids:
		links = movie_id.find_all('a')
		for link in links:
			href = link.get('href')
			movie_id = href.split('/')[2] #takes only id
		top_100_ids_list.append(movie_id)

	print(top_100_ids_list)
	print(len(top_100_ids_list))

	'''
	Part 2: Having a list of 100 movie IDs get each movie details from 
	http://www.omdbapi.com/?i=tt0111161 
	'''

	api = '5fc60de' #should be in os.environ or imported from separate file
	for movie_id in top_100_ids_list:
		omdb_url = 'http://www.omdbapi.com/' + '?i=' + movie_id + '&apikey=' + api
		r_omdb = requests.get(omdb_url)
		details = r_omdb.json()
		return details

	

imdb_crawler()





'''
Part 4: 100% test coverage is required (please use py.test) 
'''