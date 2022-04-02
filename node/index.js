var config=require('config')
var express = require('express')
var app = express()

var http=require("http");
var data=require("./widgets.json");
var mylink="/api"

app.set('port', (process.env.PORT || 3000))
app.use(express.static(__dirname + '/public'))
app.get('/env', function(request, response)
{
        response.send('<b>Hello World! My name is = <em>' + process.env.MYNAME + '</em <br />  <br> My Node Environment is :' + config.util.getEnv('NODE_ENV') + '</br></em></b>'+'<br> <a href='+mylink+'> API Link </a></br>')
})

app.get('/api', function(request, response)
{
        response.writeHead(200,{"Content-Type":"text/json"});
        response.end(JSON.stringify(data));

})

app.listen(app.get('port'), function() {
  console.log("Node app is running at localhost:" + app.get('port'))
})
