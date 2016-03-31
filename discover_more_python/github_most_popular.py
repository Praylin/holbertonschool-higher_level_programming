import urllib2

request_headers = {
  'User-Agent': 'Holberton_School',
  'Authorization': 'token 6be002d3b7968b5ef3fbbb318e97afe71225afe5'
}  

# req = urllib2.Request('https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc')
# response = urllib2.urlopen(req)
# the_page = response.read()
# data = {}

# response = urllib2.urlopen('https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc')
req = urllib2.Request('https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc',  None, request_headers)
response = urllib2.urlopen(req)
the_page = response.read()
print (req)