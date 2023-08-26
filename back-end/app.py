"""
_summary_
"""
from flask import Flask, jsonify
from database.access_table import Database

app = Flask(__name__)

data_base = Database()

@app.route('/view_data', methods=['GET'])
def view_data():
    """
    Endpoint to fetch all the data from the database.
    """
    data = data_base.select_all_data()
    return jsonify(data)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    """
    Endpoint to manage the settings of the app
    """
    return

if __name__ == "__main__":
    app.run(port=3001)
    app.run(debug=True)
