var https = require('https');
var options = {
    hostname: 'api.github.com',
    path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
    headers: {
	'User-Agent': 'Holberton_School',
	'Authorization': 'token bbb4a413d9e0340cd47db2f9b6898aadd5ea2cdc'
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
