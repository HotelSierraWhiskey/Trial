room_socket.on('message', (data) => {
  const username = data["username"];
  const message = data["data"];

  const link_to_user_profile = document.createElement('a');
  link_to_user_profile.className = 'link_to_user_profile';
  link_to_user_profile.href = `/profile/${username}`;
  link_to_user_profile.textContent = username;

  const message_content = document.createElement('span');
  message_content.className = 'message_content';
  message_content.textContent = `: ${message}`;

  const bold = document.createElement('b');
  bold.append(link_to_user_profile);

  const whole_item = document.createElement('span');
  whole_item.className = 'message_item'
  whole_item.append(bold);
  whole_item.append(message_content);

  document.getElementById("main_chat_box").append(whole_item)
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