var http=require("http");
var fs=require("fs");
var os=require("os");
var ip=require("ip");

http.createServer(function(req,res){
        fs.readFile('covid.csv', function(err,data){
                res.writeHead(200, {'Content-Type':'text/csv'});
                res.write(data);
                return res.end();
        });
}).listen(8080);
console.log("server listening at port 8080");