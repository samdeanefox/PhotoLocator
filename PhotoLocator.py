import requests
 
r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=344+Boylston+Street,+Boston,+MA&key=AIzaSyBLD1wSgxXTBzab5wRhEHB1pCDjN1jMU0w', auth=('user', 'pass'))
 
print r.status_code
print r.headers
print r.content


#Alternate Library
'''
import urllib.requests
urlllib.request.urlopen('http://www.google.com').read()
'''