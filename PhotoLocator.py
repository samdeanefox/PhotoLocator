import sys
import requests
import json

#Check for correct number of arguments
if len(sys.argv) != 2:
	print 'usage: python PhotoLocator.py [address-string]'
	sys.exit()

#Some initial variables
#Google
g_querystring = 'https://maps.googleapis.com/maps/api/geocode/json?address='
g_api_key = 'AIzaSyBLD1wSgxXTBzab5wRhEHB1pCDjN1jMU0w'
#Instagram
i_querystring = 'https://api.instagram.com/v1/media/search?lat=48.858844&lng=2.294351&access_token=ACCESS-TOKEN'
i_client_id = 'c8d5084deb084eab96bc783ec7ab1147'

#Construct query string
address = sys.argv[1].split()
for word in address:
	g_querystring += word + '+'
g_querystring = g_querystring[:-1]
g_querystring += '&key=' + g_api_key


#Query geocode
g_response = requests.get(g_querystring) #json response
g_data_dict = json.loads(g_response.content) #dictionary for referencing fields
g_data_string = json.dumps(g_response.content) #string for easy detection of ZERO_RESULTS flag

#Handle if no match
if 'ZERO_RESULTS' in g_data_string:
	print 'Sorry, can\'t find that location'
	sys.exit()

#Extract lat and lng
lat = g_data_dict['results'][0]['geometry']['location']['lat']
lng = g_data_dict['results'][0]['geometry']['location']['lng']
print 'lat value:', lat
print 'lng value:', lng


