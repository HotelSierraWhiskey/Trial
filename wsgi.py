from application import app, socketio
from application import events


if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000)