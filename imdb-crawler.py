from bs4 import BeautifulSoup
import csv
import json
import requests

'''
Part 1: Get data about top 100 movies from http://www.imdb.com/chart/top?ref=ft_250.  
Check each movie link and scrape movie's ID that is a part or URL, 
for  instance: <a  href="/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&amp;pf_rd_p=...  </a> 
The ID of this movie is "tt0111161"   
'''

def imdb_id_crawler():
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

	return top_100_ids_list

	'''
	Part 2: Having a list of 100 movie IDs get each movie details from 
	http://www.omdbapi.com/?i=tt0111161 
	'''

def omdb_api_details():
	api = '5fc60de' #should be in os.environ or imported from separate file
	movies_details = dict()
	top_100_ids_list = imdb_id_crawler()

	for movie_id in top_100_ids_list:
		omdb_url = 'http://www.omdbapi.com/' + '?i=' + movie_id + '&apikey=' + api
		r_omdb = requests.get(omdb_url)
		details = r_omdb.json()
		movies_details[details['Title']] = details['Year']

	sorted_movies = sorted(movies_details.items(), key=lambda x: x[1])
	return sorted_movies

	'''
	Part 3: Having details of those 100 movies put movies into CSV file  
	sorted by year of production CSV will consists of only two columns:  
	title, year. 
	'''

	#enter your file path below
def main_csv():
	sorted_movies = omdb_api_details()
	with open('/users/marta/git/imdb-top-movies/ImdbTopMovies.csv', 'w') as f:
		columns = ['Title', 'Year']
		writer = csv.writer(f, dialect='excel')
		writer.writerow(columns)
		for data in sorted_movies:
			writer.writerow(data)


main_csv()