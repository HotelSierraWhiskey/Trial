room_socket.on('message', (data) => {
  const username = data["username"];
  const message = data["data"];
  document.getElementById("main_chat_box").innerHTML += `${username} says: ${message}<br>`;
  console.log('(ROOM ' + data['room_id'] + ') ', data);
});


// room_socket.on('notification', (data) => {
//   const notification_type = data['type']
//   if (notification_type == 'user_joined') {
//       // room_socket.emit('active_users_request', {'room_id': room_id});
//       // document.getElementById("main_chat_box").innerHTML += `${username} has joined the chat<br>`;
//   }
//   if (notification_type == 'user_left') {
//       // room_socket.emit('active_users_request', {'room_id': room_id});
//       // document.getElementById("main_chat_box").innerHTML += `${username} has left the chat<br>`;
//   }
//   console.log('(ROOM ' + room_id + ') ', data);
// });


room_socket.on('active_users_update', (data) => {
  active_users = data['active_users'];
  console.log(`active_users_update(): ${active_users}`);
  rerenderActiveUsers();
});