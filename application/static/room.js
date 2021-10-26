const room_id = window.location.href.split('/').pop();

var room_name = '';

const username = document.getElementById('username').textContent;

const room_socket = io();

var active_users = []


function handleNavigateAway() { room_socket.emit('leave_room_request', {'username': username,'room_id': room_id}); }


function renderJoinMessage() { document.getElementById("main_chat_box").innerHTML += `${username} has joined the chat<br>` }


function renderLeaveMessage() { document.getElementById("main_chat_box").innerHTML += `${username} has left the chat<br>` }


function setButtons() {
    document.getElementById('chat_send_button').onclick = handleSend;
    document.getElementById('chat_clear_chat_button').onclick = handleClearChat;
}


function requestJoinRoom() {
    const payload = {'username': username, "room_id": room_id};
    room_socket.emit('join_room_request', payload);
}


function requestRoomName() {
    room_socket.emit('room_name_request', {'room_id': room_id});
}


function renderActiveUsers() {
    document.getElementById('users_in_room_list').innerHTML = ''
    for (var i = 0; i < active_users.length; i++) {
        const entry = active_users[i]
        document.getElementById('users_in_room_list').innerHTML += `<li id=${entry}>${entry}</li>`;
    }
}


function renderRoomName() { document.getElementById('room_name').textContent = room_name; } 


function handleSend() {
    const message = document.getElementById('chat_message_text_area').value;
    if (message) {
        const payload = {'username': username, 'data': message, 'room_id': room_id};
        room_socket.emit('message', payload);
    }
    document.getElementById('chat_message_text_area').value = '';
}


function handleClearChat() {
    document.getElementById('main_chat_box').textContent = '';
}


window.onload = function() {
    setButtons();
    requestJoinRoom();
    requestRoomName();

    document.getElementById("chat_message_text_area").addEventListener("keydown", (e) => {
        if (e.key === "Enter") {
            e.preventDefault();
            chat_send_button.click();
        }
    });
}


window.onbeforeunload = function() {
    handleNavigateAway();
}