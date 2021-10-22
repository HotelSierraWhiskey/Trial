from application import app, socketio


if __name__ == "__main__":
    app = socketio.run(app, debug=True)