"""
_summary_
"""
from flask import Flask, jsonify, current_app
from database.database import SMAH
from flask_cors import CORS
from modules import SmartACEnvironment
from modules import OccupancySensor, TemperatureSensor, HumiditySensor

app = Flask(__name__)
CORS(app)

ON = "TURN_ON_AC"
OFF = "TURN_OFF_AC"
SET_TEMP = "SET_TEMP_"

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

    data = SMAH().get_system_data(database_connection, cursor_object)
    
    SMAH().close_connection()
    return data

@app.route('/api/v1/', methods=['GET'])
def root():
    """
    Endpoint to fetch all the data from the database.
    """
    ac_1 = SmartACEnvironment()

    ac_1.step(ON)

    return jsonify(ac_1.get_ac_status())

if __name__ == "__main__":
    app.run(threaded=False, port=3001, debug=True)
