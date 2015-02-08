import sys
import requests
import json

#Check for correct number of arguments
if len(sys.argv) != 2:
	print 'usage: python PhotoLocator.py [address-string]'
	sys.exit()

#Create query string
gquerystring = 'https://maps.googleapis.com/maps/api/geocode/json?address='
api_key = 'AIzaSyBLD1wSgxXTBzab5wRhEHB1pCDjN1jMU0w'
address = sys.argv[1].split()
for word in address:
	gquerystring += word + '+'
gquerystring = gquerystring[:-1]
gquerystring += '&key=' + api_key


#Query geocode
r = requests.get(gquerystring, auth=('user', 'pass'))
 
print r.status_code
print r.headers
print r.content

#Parse 
