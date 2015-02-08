import sys
import requests
import json

#Some initial variables
#Google
g_querystring = 'https://maps.googleapis.com/maps/api/geocode/json?address=' #incomplete
g_api_key = 'AIzaSyBLD1wSgxXTBzab5wRhEHB1pCDjN1jMU0w'
#Instagram
i_querystring = 'https://api.instagram.com/v1/media/search?lat=' #incomplete
i_client_id = 'c8d5084deb084eab96bc783ec7ab1147'
i_access_token = '1697175721.c8d5084.47464f0e27ed49a084a8c3817f2c6c94'

#Check for correct number of arguments
if len(sys.argv) != 2:
	print 'usage: python PhotoLocator.py [address-string]'
	sys.exit()

#Construct Google query string
address = sys.argv[1].split()
for word in address:
	g_querystring += word + '+'
g_querystring = g_querystring[:-1]
g_querystring += '&key=' + g_api_key

#Query Google
g_response = requests.get(g_querystring) #json response
g_data_dict = json.loads(g_response.content) #dictionary to reference fields
g_data_string = json.dumps(g_response.content) #string representation for easy detection of ZERO_RESULTS flag

#Handle if no match
if 'ZERO_RESULTS' in g_data_string:
	print 'Sorry, can\'t find that location'
	sys.exit()

#Extract lat and lng
lat = str(g_data_dict['results'][0]['geometry']['location']['lat'])
lng = str(g_data_dict['results'][0]['geometry']['location']['lng'])

#Construct Instagram query string
i_querystring += lat + '&lng=' + lng + '&access_token=' + i_access_token

#Query Instagram
i_response = requests.get(i_querystring) #json reponse
i_data_dict = json.loads(i_response.content) #dictionary to reference fields
i_data_string = json.dumps(i_response.content) #string representation for easy detection of error_message

#Handle if something goes wrong
if 'error_message' in i_data_string:
	print 'Instagram query failed, error message:', i_data_dict['meta']['error_message']
	sys.exit()

#Unique message if there are no images
if len(i_data_dict['data']) < 1:
	print 'Found zero images nearby :('
	sys.exit()

#Print information to console
i = 1
print 'Found ' + str(len(i_data_dict['data'])) + ' recent images nearby!' + '\n\n'
for entry in i_data_dict['data']:
	print str(i) + ':'
	print entry['images']['standard_resolution']['url']
	print 'Latitude:', entry['location']['latitude']
	print 'Longitude:', entry['location']['longitude']
	print '\n\n\n'
	i += 1