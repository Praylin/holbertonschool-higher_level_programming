require 'HTTPClient'

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 39fed9cadb8579194e82b4bc4aefa34b8fab30b7'
}


clnt = HTTPClient.new
res = clnt.get_content('https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc', query = nil, extheaders = {})

output = File.open("/tmp/36","w")
output << res
output.close
puts('The file was saved!')