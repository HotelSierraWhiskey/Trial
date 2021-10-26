admin_socket = io();



function showCreateRoomTools(operation) {
    if (document.getElementById('create_room_name_field')) {
        hideCreateRoomTools();
    }

    var field = document.createElement('input')
    field.id = 'create_room_name_field'

    var button = document.createElement('button')
    button.textContent = 'Ok';
    button.id = 'create_room_name_button';

    if (operation == 'create') {
        button.onclick = createRoom;
    }
    if (operation == 'delete') {
        button.onclick = deleteRoom;
    }
    document.getElementById('chat_admin_panel').append(field);
    document.getElementById('chat_admin_panel').append(button);
}


function hideCreateRoomTools() {
    document.getElementById('create_room_name_field').remove();
    document.getElementById('create_room_name_button').remove();
}



function createRoom() {
    const name = document.getElementById('create_room_name_field').value;
    admin_socket.emit('create_room', {'name': name});
    hideCreateRoomTools();
}


function deleteRoom() {
    const name = document.getElementById('create_room_name_field').value;
    admin_socket.emit('delete_room', {'name': name});
}