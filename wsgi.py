from application import app, socketio
from application import events


if __name__ == "__main__":
    socketio.run(app, debug=True)