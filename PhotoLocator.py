import requests
 
r = requests.get('http://www.google.com', auth=('user', 'pass'))
 
print r.status_code
print r.headers
print r.content


#Alternate Library
'''
import urllib.requests
urlllib.request.urlopen('http://www.google.com').read()
'''