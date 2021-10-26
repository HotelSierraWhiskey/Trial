room_socket.on('message', (data) => {
  const username = data["username"];
  const message = data["data"];
  document.getElementById("main_chat_box").innerHTML += `${username} says: ${message}<br>`;
  console.log('(ROOM ' + data['room_id'] + ') ', data);
});


room_socket.on('active_users_update', (data) => {
  active_users = data['active_users'];
  console.log(`active_users_update(): ${active_users}`);
  renderActiveUsers();
});