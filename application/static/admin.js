admin_socket = io();

var create_room_tools_items = [];

function showCreateRoomTools(operation) {
    if (document.getElementById('create_room_prompt_span')) {
        return;
    }
    var prompt_span = document.createElement('span');
    prompt_span.id = 'create_room_prompt_span';
    prompt_span.textContent = `enter name of room to ${operation}`;
    create_room_tools_items.push(prompt_span);

    var br = document.createElement('br');
    br.id = 'create_room_line_break';
    create_room_tools_items.push(br);

    var name_field = document.createElement('input');
    name_field.id = 'create_room_name_field';
    create_room_tools_items.push(name_field);

    var ok_button = document.createElement('button');
    ok_button.textContent = 'Ok';
    ok_button.id = 'ok_create_room_button';
    create_room_tools_items.push(ok_button);

    var cancel_button = document.createElement('button');
    cancel_button.textContent = 'Cancel';
    cancel_button.id = 'cancel_create_room_button';
    cancel_button.onclick = hideCreateRoomTools;
    create_room_tools_items.push(cancel_button);

    if (operation == 'create') {
        ok_button.onclick = createRoom;
    }
    if (operation == 'delete') {
        ok_button.onclick = deleteRoom;
    }

    for (const elem of create_room_tools_items) {
        document.getElementById('chat_admin_panel').append(elem);
    }
}


function hideCreateRoomTools() {
    for (const elem of create_room_tools_items) {
        document.getElementById(elem.id).remove();
    }
    create_room_tools_items = [];
}


function createRoom() {
    const name = document.getElementById('create_room_name_field').value;
    const id = name.split(' ').join('');
    const href = `rooms/${id}`;
    
    const room_entry = document.createElement('span')
    room_entry.id = `entry_${id}`
    room_entry.className = "room_entry"

    const room_anchor = document.createElement('a')
    room_anchor.id = id
    room_anchor.href = href
    room_anchor.onclick = 'null'
    room_anchor.textContent = `${name} (0)`;

    room_entry.append(room_anchor);

    document.getElementById('chat_rooms').append(room_entry);

    admin_socket.emit('create_room', {'name': name});
    
    hideCreateRoomTools();
}


function deleteRoom() {
    const id = document.getElementById('create_room_name_field').value;
    document.getElementById(`entry_${id}`).remove()
    admin_socket.emit('delete_room', {'name': id});
    hideCreateRoomTools();
}