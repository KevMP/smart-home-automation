"""
_summary_
"""
from flask import Flask, jsonify
from database.database import SMAH
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.teardown_appcontext
def close_db(exception):
    print(exception)
    SMAH.close_connection()

@app.route('/api/v1/view-data', methods=['GET'])
def view_data():
    """
    Endpoint to fetch all the data from the database.
    """
    db = SMAH()
    data = db.select_all_data()
    return jsonify(data)

@app.route('/api/v1/admin', methods=['GET', 'POST'])
def admin():
    """
    Endpoint to fetch all the data from the database.
    """
    pass

if __name__ == "__main__":
    app.run(threaded=False, port=3001, debug=True)
