"""
_summary_
"""
from flask import Flask, jsonify
from database.access_table import Database

app = Flask(__name__)

@app.teardown_appcontext
def close_db(exception):
    Database.close_connection(exception)

@app.route('/api/v1/view-data', methods=['GET'])
def view_data():
    """
    Endpoint to fetch all the data from the database.
    """
    db = Database()
    data = db.select_all_data()
    return jsonify(data)

if __name__ == "__main__":
    app.run(threaded=False, port=3001, debug=True)

