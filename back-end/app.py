"""
_summary_
"""
from flask import Flask, jsonify, current_app
from database.database import SMAH
from flask_cors import CORS
from modules import SmartACEnvironment
from model import DQNAgent
import numpy as np

app = Flask(__name__)
CORS(app)

global_agent = None
ON = 1
OFF = 2
SET_TEMP = 3

@app.teardown_appcontext
def close_db(exception):
    print(exception)
    SMAH.close_connection()

@app.after_request
def add_no_cache_headers(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

@app.route('/api/v1/view-data', methods=['GET'])
def view_data():
    """
    Endpoint to fetch all the data from the database.
    """
    database_connection = SMAH().create_connection()
    cursor_object = database_connection.cursor()

    data = SMAH().get_all_table_data(database_connection, cursor_object)

    SMAH().close_connection()
    return jsonify(data)

@app.route('/api/v1/admin', methods=['POST'])
def train_agent():
    global global_agent
    global_agent = train_dqn_agent()
    return jsonify({"status": "Training completed"})

@app.route('/api/v1/', methods=['GET'])
def root():
    if not global_agent:
        return jsonify({"error": "Agent not trained!"}), 400

    environment = SmartACEnvironment()
    state = np.array([environment.get_current_state()])
    action = global_agent.choose_action(state)
    environment.step(action)

    return jsonify(environment.get_ac_status())

def train_dqn_agent():
    state_size = 3  # occupancy, temperature, humidity
    action_size = 3  # TURN_ON_AC, TURN_OFF_AC, SET_TEMP
    agent = DQNAgent(state_size, action_size)
    environment = SmartACEnvironment()

    episodes = 10
    max_steps = 10

    for episode in range(episodes):
        state = np.array([environment.get_current_state()])
        total_reward = 0
        
        for step in range(max_steps):
            action = agent.choose_action(state)
            next_state, reward, done = environment.step(action)
            next_state = np.array([next_state])
            agent.remember(state, action, reward, next_state, done)
            agent.replay()
            state = next_state
            total_reward += reward
            if done:
                break

    return agent

if __name__ == "__main__":
    app.run(threaded=False, port=3001, debug=True, use_reloader=False)
