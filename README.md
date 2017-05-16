# imdb-top-movies
Script creates csv file with top#100 movies from IMDB

### Part 1: 
Get data about top 100 movies from [IMDB](http://www.imdb.com/chart/top?ref=ft_250)  

Scrape movie's ID that is a part or URL, for  instance: 
```
<a  href="/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&amp;pf_rd_p=...  </a>
```
The ID of this movie is "tt0111161"   

### Part 2: 
Having a list of 100 movie IDs get each movie details from [OMDBAPI](http://www.omdbapi.com/?i=tt0111161) 


### Part 3: 
Put movies into CSV file sorted by year of production CSV will consists of only two columns:  title, year. 

### Part 4: 
100% test coverage is required (please use py.test) 