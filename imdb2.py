from bs4 import BeautifulSoup as SOUP
import re
import requests as HTTP
import csv

# Main Function for scraping

def movies(emotion):

	# IMDb Url for Drama genre of movie against emotion Sad
	if(emotion == "Sad"):
		urlhere = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'

	# IMDb Url for Musical genre of movie against emotion Disgust
	elif(emotion == "Disgust"):
		urlhere = 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc'

	# IMDb Url for Family genre of movie against emotion Anger
	elif(emotion == "Angry"):
		urlhere = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'

	# IMDb Url for Thriller genre of
	# movie against emotion Anticipation
	elif(emotion == "Surprise"):
		urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'

	# IMDb Url for Sport genre of
	# movie against emotion Fear
	elif(emotion == "Fear"):
		urlhere = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'

	# IMDb Url for Thriller genre of
	# movie against emotion Enjoyment
	elif(emotion == "Happy"):
		urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'

	# IMDb Url for Western genre of
	# movie against emotion Trust
	elif(emotion == "Neutral"):
		urlhere = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'

	# IMDb Url for Film_noir genre of
	# movie against emotion Surprise
	elif(emotion == "Surprise"):
		urlhere = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc'

	# HTTP request to get the data of
	# the whole page
	response = HTTP.get(urlhere)
	data = response.text

	# Parsing the data using
	# BeautifulSoup
	soup = SOUP(data, "html.parser")
	results =  soup.find_all('div', class_='lister-item-content')
	with open('movie_ratings.csv', 'w', newline='') as csv_file:
		csv_writer = csv.writer(csv_file)
		csv_writer.writerow(['Title', 'Rating'])
		for idx, result in enumerate(results, 1):
			title = result.h3.a.text
			rating_element = result.find('div', class_='inline-block ratings-imdb-rating')
			rating = rating_element.strong.text if rating_element else "N/A"
			csv_writer.writerow([title, rating])
			print(f"{idx}. Title: {title} ({rating})")
	

# if __name__ == '__main__':
#     emotion = input("Enter the emotion: ")
#     main(emotion)