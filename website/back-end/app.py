import sys
from pathlib import Path
root_path = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(root_path))

from initalize_app import create_app, socketio

app = create_app()

app.app_context().push()

if __name__ == '__main__':
    socketio.run(app, port=3001, debug=True, use_reloader=False, allow_unsafe_werkzeug=True)
