room_socket.on('message', (data) => {
  const username = data["username"];
  const message = data["data"];
  const item = `<span><b class="message_username">${username}:</b><span class=message_content> ${message}</span></span><br>`;
  document.getElementById("main_chat_box").innerHTML += item;
  document.getElementById('main_chat_box').lastChild.scrollIntoView();
});


room_socket.on('active_users_update', (data) => {
  active_users = data['active_users'];
  renderActiveUsers();
});


room_socket.on('room_name_update', (data) => {
  room_name = data['room_name'];
  renderRoomName();
});