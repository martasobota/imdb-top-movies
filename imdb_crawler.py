from bs4 import BeautifulSoup
import csv
import json
import requests

class IMDB_top_movies:

	api = '5fc60de' #should be exported to os.environ or imported from separate file
	csv_file_name = 'ImdbTopMovies.csv'
	imdb_url = 'http://www.imdb.com/chart/top?ref=ft_250'

	def __init__(self, api, csv_file_name, imdb_url):
		self.api = api
		self.csv_file_name = csv_file_name
		self.imdb_url = imdb_url

	'''
	Part 1: Get data about top 100 movies from http://www.imdb.com/chart/top?ref=ft_250.  
	Check each movie link and scrape movie's ID that is a part or URL, 
	for  instance: <a  href="/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&amp;pf_rd_p=...  </a> 
	The ID of this movie is "tt0111161"   
	'''

	def imdb_id_crawler(self):
		# imdb_url = 'http://www.imdb.com/chart/top?ref=ft_250'
		r_imdb = requests.get(self.imdb_url)
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

	def omdb_api_details(self):
		
		api = self.api
		movies_details = dict()
		top_100_ids_list = self.imdb_id_crawler()

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

	def generate_csv(self):
		sorted_movies = self.omdb_api_details()
		csv_file_name = self.csv_file_name
		with open(csv_file_name, 'w') as f:
			columns = ['Title', 'Year']
			writer = csv.writer(f, dialect='excel')
			writer.writerow(columns)
			for data in sorted_movies:
				writer.writerow(data)

if __name__ == "__main__":
    Top100 = IMDB_top_movies('5fc60de', 'ImdbTopMovies.csv', 'http://www.imdb.com/chart/top?ref=ft_250')
    Top100.imdb_id_crawler()
    print("List of top 100 id's: {}.\nThere are {} movies on the list.".format(Top100.imdb_id_crawler(), len(Top100.imdb_id_crawler())))
    Top100.omdb_api_details()
    print("Sorted movies: {}".format(Top100.omdb_api_details()))
    Top100.generate_csv()
    print("CSV file generated. Enjoy watching 🎦")