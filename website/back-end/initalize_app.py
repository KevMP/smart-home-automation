from flask import Flask
from initialize_socket import socketio
from developer_routes import developer_bp
import logging
from logging.handlers import RotatingFileHandler
from flask_cors import CORS
from database.database import Database

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    socketio.init_app(app)

    @app.teardown_appcontext
    def close_db(exception):
        if exception:
            app.logger.error(exception)
        Database.close_connection()

    @app.after_request
    def add_no_cache_headers(response):
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response
    
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

    app.register_blueprint(developer_bp)

    return app
