var token = process.env.TOKEN;
var https = require('https');
var token = process.env.TOKEN;
var options = {
    hostname: 'api.github.com',
    path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
    headers: {
	'User-Agent': 'Holberton_School',
	'Authorization': 'token ' + token
    }
}
var req = https.request(options, function(res) {
    res.on('data', function(d) {
	process.stdout.write(d);
    });
});
req.end();

req.on('error', function(e) {
    console.error(e);
});
