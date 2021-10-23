const sio = io();


sio.on('connect', () => {
  sio.emit('client_connection');
});


sio.on('disconnect', () => {
  sio.emit('client_disconnection');
});


window.onload = function() {

}