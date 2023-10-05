"""
_summary_
"""
from flask import Flask, jsonify, current_app
from database.database import Database
from flask_cors import CORS
from modules import SmartACEnvironment
from agent import DQNAgent, train_dqn_agent
import numpy as np

app = Flask(__name__)
CORS(app)

global_agent = None

@app.teardown_appcontext
def close_db(exception):
    print(exception)
    Database.close_connection()

@app.after_request
def add_no_cache_headers(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

@app.route('/api/v1/view-data', methods=['GET'])
def view_data():
    database_connection, cursor_object = Database.get_connection()
    
    data = Database.get_all_table_data(database_connection, cursor_object)

    return jsonify(data)

@app.route('/api/v1/admin', methods=['POST'])
def train_agent():
    global global_agent
    global_agent = train_dqn_agent()
    return jsonify({"status": "Training completed"})

@app.route('/api/v1/dashboard', methods=['GET'])
def root():
    if not global_agent:
        return jsonify({"error": "Agent not trained!"}), 400

    environment = SmartACEnvironment()
    state = np.array([environment.get_current_state()])
    action = global_agent.choose_action(state)
    environment.step(action)

    return jsonify(environment.get_ac_status())

if __name__ == "__main__":
    app.run(threaded=False, port=3001, debug=True, use_reloader=False)
