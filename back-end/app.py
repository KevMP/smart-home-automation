"""
_summary_
"""
from flask import Flask, jsonify
from database.database import SMAH
from flask_cors import CORS
from modules import SmartACEnvironment
from modules import OccupancySensor, TemperatureSensor, HumiditySensor

app = Flask(__name__)
CORS(app)

@app.teardown_appcontext
def close_db(exception):
    print(exception)
    SMAH.close_connection()

@app.route('/api/v1/', methods=['GET'])
def root():
    """
    Endpoint to fetch all the data from the database.
    """
    ac_1 = SmartACEnvironment()
    print(ac_1.get_current_state())
    on = "TURN_ON_AC"
    off = "TURN_OFF_AC"
    set_temp = "SET_TEMP_"

    ac_1.step(off)
    
    print(ac_1.get_current_state())
    print("TEST")
    return jsonify(False)

if __name__ == "__main__":
    app.run(threaded=False, port=3001, debug=True)
