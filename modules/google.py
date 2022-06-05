import bs4 
import requests
def google(q):
	# Taking thecity name as an input from the user
	query = q
	# Generating the url  
	url = "https://google.com/search?q=" + query
	
	# Sending HTTP request 
	request_result = requests.get( url )
	
	# Pulling HTTP data from internet 
	soup = bs4.BeautifulSoup( request_result.text, "html.parser" )
	
	result = soup.find( "div" , class_='BNeawe' ) 
		
	return result
