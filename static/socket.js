// 192.168.1.135
const socket = new WebSocket('ws://' + location.hostname +'/ws');

socket.addEventListener('open', function (event) {
    socket.onclose = function(){
        setTimeout(function(){start(websocketServerLocation)}, 5000);
    };
});

socket.addEventListener('message', function (event) {
    var msg = event.data;
    if (msg.startsWith("data")){
        document.getElementById('data').value = msg;
    }
    else {
        var link = document.createElement('a');
        link.setAttribute('href', "?/" + encodeURI(msg));
        link.appendChild(document.createTextNode(msg))
        document.getElementsByTagName("songs")[0].appendChild(link); 
    }

});

function addMessage() {
    socket.send(document.getElementById('message').value);
    document.getElementById('message').value = '';
}; 

