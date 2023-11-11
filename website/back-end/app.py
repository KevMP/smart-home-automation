import sys
from pathlib import Path
root_path = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(root_path))

from flask import Flask, jsonify
from flask_cors import CORS
from developer_routes import developer_bp
from database.database import Database
import logging
from logging.handlers import RotatingFileHandler
import os

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

file_handler = RotatingFileHandler('website/back-end/logs/app.log', maxBytes=10240,
                                   backupCount=10)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
))
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)

app.logger.addHandler(stream_handler)
app.logger.setLevel(logging.DEBUG)

# Routes
app.register_blueprint(developer_bp)

@app.teardown_appcontext
def close_db(exception):
    if exception:
        logging.error(exception)
    Database.close_connection()

@app.after_request
def add_no_cache_headers(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

if __name__ == "__main__":
    app.debug = True
    
    if app.debug:
        werkzeug_logger = logging.getLogger('werkzeug')
        werkzeug_logger.disabled = True

    app.run(threaded=False, port=3001, debug=True, use_reloader=False)
