const room_id = window.location.href.split('/').pop();

const username = document.getElementById('username').textContent;

const room_socket = io();


function setRoomID(room_id) {
    document.getElementById('room_id').textContent = room_id;
}


room_socket.on('message', (data) => {
    console.log('(ROOM ' + room_id + ') ', data);
});


room_socket.on('notification', (data) => {
    console.log('(ROOM ' + room_id + ') ', data);
});



function requestJoinRoom(room_id) {
    data = {'username': username, "room_id": room_id};
    room_socket.emit('join_room_request', data);
}




window.onload = function() {
    setRoomID(room_id);
    requestJoinRoom(room_id);
    sio.emit('message', {'data': 'hello', 'room_id': room_id})
}