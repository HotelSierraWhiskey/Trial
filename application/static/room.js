const room_id = window.location.href.split('/').pop();

const username = document.getElementById('username').textContent;

const room_socket = io();

var active_users = []



function setRoomID() { document.getElementById('room_id').textContent = room_id; }


function handleNavigateAway() { room_socket.emit('leave_room_request', {'username': username,'room_id': room_id}); }


function renderJoinMessage() { document.getElementById("main_chat_box").innerHTML += `${username} has joined the chat<br>` }


function renderLeaveMessage() { document.getElementById("main_chat_box").innerHTML += `${username} has left the chat<br>` }


function setButtons() {
    document.getElementById('chat_send_button').onclick = handleSend;
    document.getElementById('base_login').onclick = handleNavigateAway;
    document.getElementById('base_register').onclick = handleNavigateAway;
    document.getElementById('base_home').onclick = handleNavigateAway;
    document.getElementById('base_chat').onclick = handleNavigateAway;
}


function requestJoinRoom() {
    const payload = {'username': username, "room_id": room_id};
    room_socket.emit('join_room_request', payload);
}


function rerenderActiveUsers() {
    document.getElementById('users_in_room_list').innerHTML = ''
    for (var i = 0; i < active_users.length; i++) {
        const entry = active_users[i]
        document.getElementById('users_in_room_list').innerHTML += `<li id=${entry}>${entry}</li>`;
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