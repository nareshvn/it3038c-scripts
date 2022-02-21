var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require("ip");
 
http.createServer(function(req, res){

        if (req.url === "/"){

                fs.readFile("./Public/index.html","UTF-8",function(err,body){
                res.writeHead(200, {"Content-Type": "text/html"});
                res.end(body);
                });
}
        else
 if (req.url.match("/sysinfo")) {
                myHostName=os.hostname();
                uptime=os.uptime();
                var dy=Math.floor(uptime/(3600*24));
                var hr=Math.floor(uptime%(3600*24)/3600);
                var mi=Math.floor(uptime%3600/60);
                var ss=Math.floor(uptime%60);
                cpus=os.cpus().length;
                freem=os.freemem()/1000000;
                totm=os.totalmem()/1000000;
                html=`
        <!DOCTYPE html>
        <html>
        <head>
        <title>
        Node JS Response
        </title>
        </head>
        <body>
        <p> Hostname: ${myHostName}</p>
        <p> IP: ${ip.address()}</p>
        <p> Server Uptime: Days:  ${parseInt(dy)}
                Hours: ${parseInt(hr)}
 		Minutes: ${parseInt(mi)}
                Seconds: ${parseInt(ss)}
        </p>
        <p> Total Memory:  ${parseFlo	at(totm).toFixed(2)} MB</p>
        <p> Free Memory: ${parseFloat(freem).toFixed(2)} MB</p>
        <p> Number of CPUs: ${cpus} </p>
        </body>
        </html>`
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(html);
}
else
{
        res.writeHead(404, {"Conent-Type": "text/plain"});
        res.end(`404 File Not Found at ${req.url}`);
}
}).listen(3000);

console.log("Server listening on port 3000");
