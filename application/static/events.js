room_socket.on('message', (data) => {
  const username = data["username"];
  const message = data["data"];
  document.getElementById("main_chat_box").innerHTML += `${username} says: ${message}<br>`;
});


room_socket.on('active_users_update', (data) => {
  active_users = data['active_users'];
  renderActiveUsers();
});


room_socket.on('room_name_update', (data) => {
  room_name = data['room_name'];
  renderRoomName();
});