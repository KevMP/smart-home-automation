import sys
from pathlib import Path
root_path = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(root_path))

from flask import Flask, jsonify
from flask_cors import CORS
from developer_routes import developer_bp
from database.database import Database
import logging
import os

if not os.path.exists('website/back-end/logs'):
    os.makedirs('website/back-end/logs')

logging.basicConfig(filename='website/back-end/logs/app.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

app = Flask(__name__)
CORS(app)

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
    app.run(threaded=False, port=3001, debug=True, use_reloader=False)
