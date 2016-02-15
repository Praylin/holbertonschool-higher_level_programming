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
    streamToString(res,output);
});
req.end();

req.on('error', function(e) {
    console.error(e);
});

function streamToString(stream, cb) {
    const chunks = [];
    stream.on('data', (chunk) => {
	chunks.push(chunk);
    });
    stream.on('end', () => {
	cb(chunks.join(''));
    });
};

var output = function (jsonString)
{
   /* console.log(typeof jsonString);
    console.log(jsonString);*/
    const fs = require('fs');
    fs.writeFile("/tmp/36", jsonString, function(err) {
	if (err) {
	    return console.log(err);
	}
	console.log("successfully saved");
    });
}
