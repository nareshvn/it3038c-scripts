var data=require("/home/uc-nareshvn/it3038c-scripts/node/widgets.json");

function listBlue(res){
        var colorBlue=data.filter(function(item){
                return item.color === "blue";
        });
        res.end(JSON.stringify(colorBlue));
}

function listCue(res, cue){
        var colorCue=data.filter(function(item){
                return item.color === cue;
        });
        res.end(JSON.stringify(colorCue));
}
var server= http.createServer(function(req,res){
        if (req.url==="/"){
                res.writeHead(200,{"Content-Type":"text/json"});
                res.end(JSON.stringify(data));
        }
        else if(req.url === "/blue") {
                listCue(res,"blue");
        }
        else if(req.url === "/green") {
                listCue(res,"green");
        }
        else if(req.url === "/black") {
                listCue(res,"black");
        }
        else {
                res.writeHead(404,{"Content-Type":"text/plain"});
                res.end("Data Not Found");
        }
});
server.listen(3000);
console.log("server is listening on port 3000");
