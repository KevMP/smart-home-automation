from flask_socketio import SocketIO
import logging

logging.basicConfig(level=logging.INFO)
socketio = SocketIO(cors_allowed_origins='*')

@socketio.on('connect')
def handle_connect():
    logging.info("Socket Connected...")
    