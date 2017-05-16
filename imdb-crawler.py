import csv
import json
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

	'''
	Part 2: Having a list of 100 movie IDs get each movie details from 
	http://www.omdbapi.com/?i=tt0111161 
	'''

	api = '5fc60de' #should be in os.environ or imported from separate file
	movies_details = dict()

	for movie_id in top_100_ids_list:
		omdb_url = 'http://www.omdbapi.com/' + '?i=' + movie_id + '&apikey=' + api
		r_omdb = requests.get(omdb_url)
		details = r_omdb.json()
		movies_details[details['Title']] = details['Year']

	# sorted_movies = sorted(movies_details.items(), key=lambda x: x[1])
	# print(sorted_movies)

	'''
	Part 3: Having details of those 100 movies put movies into CSV file  
	sorted by year of production CSV will consists of only two columns:  
	title, year. 
	'''

	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
	

    # with open(self.output_file_name, 'w') as f:
    #     w = csv.writer(f)
    #     w.writerows(sorted(self.movies_details.items(), key=lambda x: x[1]))  # Sort by year, ascending

	# imdb_top_movies = open('/users/marta/git/imdb-top-movies/ImdbTopMovies.csv', 'w')
	# csvwriter = csv.writer(imdb_top_movies)

	# csvwriter.writerows(sorted_movies)



	# count = 0
	# for mov in movies_details:
	# 	if count == 0:
	# 		for keys in movies_details.items():
	# 			# header = mov.keys()
	# 			header = keys
	# 		# header = mov.keys()
	# 		# header = mov.items()
	# 		# header = mov[0][1]
	# 		csvwriter.writerow(header)
	# 		count += 1
	# 	# csvwriter.writerow(mov.values())
	# 	csvwriter.writerows(movies_details)
	# 	# csvwriter.writerow(mov)

	# imdb_top_movies.close()
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

	# with open(self.output_file_name, 'w') as f:
 #            w = csv.writer(f)
 #            w.writerows(sorted(self.movies_details.items(), key=lambda x: x[1]))  # Sort by year, ascending

	with open('/users/marta/git/imdb-top-movies/ImdbTopMovies.csv', 'w') as f:
		writer = csv.writer(f)
		writer.writerows(sorted(movies_details.items(), key=lambda x: x[1]))
	    # w.writerows(sorted(self.movies_details.items(), key=lambda x: x[1])) 


	# with open('/users/marta/git/imdb-top-movies/imdb-top-movies.csv', 'wb') as f:
	# 	writer = csv.writer(f, delimiter=';')
	# 	writer.writerows(records)

imdb_crawler()


# '''
# Part 4: 100% test coverage is required (please use py.test) 
# '''