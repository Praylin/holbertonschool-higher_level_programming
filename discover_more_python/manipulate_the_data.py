import urllib2
import urllib
import json

request_headers = {
  'User-Agent': 'Holberton_School',
  'Authorization': 'token 6be002d3b7968b5ef3fbbb318e97afe71225afe5'
}  

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc'
req = urllib2.Request(url, None, request_headers)
response = urllib2.urlopen(req)
the_page = response.read()
parsed_json = json.loads(the_page)

for i in parsed_json['items']:
    print i['full_name']