const room_id = window.location.href.split('/').pop();

const username = document.getElementById('username').textContent;

const room_socket = io();

var active_users = []


function setRoomID() {
    document.getElementById('room_id').textContent = room_id;
}


function setButtons() {
    document.getElementById('chat_send_button').onclick = handleSend;
    document.getElementById('base_login').onclick = handleNavigateAway;
    document.getElementById('base_register').onclick = handleNavigateAway;
    document.getElementById('base_home').onclick = handleNavigateAway;
    document.getElementById('base_chat').onclick = handleNavigateAway;
}


room_socket.on('message', (data) => {
    const username = data["username"];
    const message = data["data"];
    document.getElementById("main_chat_box").innerHTML += (username + ' says: ' + message + "<br>");
    console.log('(ROOM ' + data['room_id'] + ') ', data);
});


room_socket.on('notification', (data) => {
    const notification_type = data['type']
    if (notification_type == 'join') {
        active_users.push(username);
        document.getElementById("main_chat_box").innerHTML += (username + " has joined the chat<br>");
    }
    if (notification_type == 'leave') {
        active_users.push(username);
        document.getElementById("main_chat_box").innerHTML += (username + " has left the chat<br>");
    }
    console.log('(ROOM ' + room_id + ') ', data);
});


room_socket.on('active_users_response', (data) => {
    active_users = data['active_users']
});


function requestJoinRoom() {
    const payload = {'username': username, "room_id": room_id};
    room_socket.emit('join_room_request', payload);
}


function rerenderActiveUsers() {
    for (var i = 0; i < active_users.length; i++) {
        document.getElementById('users_in_room_list').innerHTML += (active_users[i] + '<br>');
    }
}


function handleSend() {
    const message = document.getElementById('chat_message_text_area').value;
    if (message) {
        const payload = {'username': username, 'data': message, 'room_id': room_id};
        room_socket.emit('message', payload);
    }
    document.getElementById('chat_message_text_area').value = '';
}


function handleNavigateAway() {
    // room_socket.emit('leave_room_request', {'room': room_id});
    // room_socket.emit('active_users_request', {'room': room_id});
    // document.getElementById("main_chat_box").innerHTML += (username + " has left the chat<br>");
    // rerenderActiveUsers();
}


window.onload = function() {
    setRoomID();
    setButtons();
    requestJoinRoom();

    document.getElementById("chat_message_text_area").addEventListener("keydown", (e) => {
        if (e.key === "Enter") {
            e.preventDefault();
            chat_send_button.click();
        }
    });
}