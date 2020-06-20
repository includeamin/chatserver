const express = require('express');
const {ExpressPeerServer} = require('peer');

const app = express();


let client_key = process.env.CLIENTKEY
if (client_key === undefined) {
    client_key = "clientkey"
}
let path_name = process.env.PATHNAME
if (path_name === undefined) {
    path_name = "/chat"
}

const config = {
    path: path_name,
    proxied: true,
    key: client_key,
    allow_discovery: true
}
console.log("server starting ...")
console.log(config)


app.get('/', (req, res, next) => res.send('signaling server based on peerjs server'));
//temporary
app.get('/key', (req, res) => {
    res.send({"key": client_key})
})

const server = app.listen(9002, "0.0.0.0");

const peerServer = ExpressPeerServer(server, config);


peerServer.on('connection', client => {
    console.log("client id" + client.id + " token " + client.token)
})

peerServer.on('disconnect', client => {
    console.log("client id " + client.id + " token " + client.token)
})

app.use('/peerjs', peerServer);
