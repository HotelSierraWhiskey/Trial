const sio = io();


sio.on('connect', () => {
  console.log("connected");
  sio.emit('client_connection');
});


sio.on('disconnect', () => {
  console.log("disconnected");
  sio.emit('client_disconnection');
});


sio.on('message', (data) => {
  console.log('(GLOBAL) ', data);
});



window.onload = function() {
  

}