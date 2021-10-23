function setRoomID(id) {
    JSON.parse
    document.getElementById("room_id").textContent = id;
}


window.onload = function() {
    id = window.location.href.split("/").pop()
    setRoomID(id);
}