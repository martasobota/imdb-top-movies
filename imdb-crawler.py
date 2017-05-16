from bs4 import BeautifulSoup
import requests

'''
Part 1: Get data about top 100 movies from http://www.imdb.com/chart/top?ref=ft_250.  
Check each movie link and scrape movie's ID that is a part or URL, 
for  instance: <a  href="/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&amp;pf_rd_p=...  </a> 
The ID of this movie is "tt0111161"   

Part 2: Having a list of 100 movie IDs get each movie details from 
http://www.omdbapi.com/?i=tt0111161 

Part 3: Having details of those 100 movies put movies into CSV file  
sorted by year of production CSV will consists of only two columns:  title, year. 

Part 4: 100% test coverage is required (please use py.test) 
'''


def get_100_ids():
	url = 'http://www.imdb.com/chart/top?ref=ft_250'
	r = requests.get(url)
	imdb_content = r.text
	soup = BeautifulSoup(imdb_content, 'lxml')

	top_100_ids_list = []

	movies_ids = soup.find_all('td', {'class' : 'titleColumn'})

	for movie_id in movies_ids:
	    number = movie_id.text.split('.')[0]
	    links = movie_id.find_all('a')
	    for link in links:
	        href = link.get('href')
	        movie_id = href.split('/')[2]

	    if int(number) <= 100:
	        top_100_ids_list.append(movie_id)

	print(top_100_ids_list)

get_100_ids()