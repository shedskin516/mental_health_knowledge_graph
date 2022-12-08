from datetime import timedelta
from email import policy
import os

from flask import Flask
from flask.helpers import send_from_directory

from flask_jwt_extended import JWTManager
from flask_cors import CORS

from api.exceptions.notfound import NotFoundException

from .exceptions.badrequest import BadRequestException
from .exceptions.validation import ValidationException

from .neo4j import init_driver

from .routes.disease import disease_routes
from .routes.therapist import therapist_routes
from .routes.analysis import analysis_routes

def create_app(test_config=None):
    # Create and configure app
    static_folder = os.path.join(os.path.dirname(__file__), '..', 'page/build')
    app = Flask(__name__, static_url_path='/', static_folder=static_folder)

    app.config.from_mapping(
        NEO4J_URI=os.getenv('NEO4J_URI'),
        NEO4J_USERNAME=os.getenv('NEO4J_USERNAME'),
        NEO4J_PASSWORD=os.getenv('NEO4J_PASSWORD'),
        NEO4J_DATABASE=os.getenv('NEO4J_DATABASE'),
        JWT_SECRET_KEY=os.getenv('JWT_SECRET'),
        JWT_AUTH_HEADER_PREFIX="Bearer",
        JWT_VERIFY_CLAIMS="signature",
        JWT_EXPIRATION_DELTA=timedelta(360)
    )

    # Apply Test Config
    if test_config is not None:
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    with app.app_context():
        init_driver(
            app.config.get('NEO4J_URI'),
            app.config.get('NEO4J_USERNAME'),
            app.config.get('NEO4J_PASSWORD'),
        )

    # JWT
    jwt = JWTManager(app)

    CORS(app, 
        resources={r"/*": {"origins": ["http://localhost:3000", "http://127.0.0.1:3000"]}}
    )
    
    # Register Routes
    app.register_blueprint(disease_routes)
    app.register_blueprint(therapist_routes)
    app.register_blueprint(analysis_routes)

    # Serve all other routes as static
    @app.route('/', methods=['GET'])
    def index():
        return send_from_directory(static_folder, 'index.html')

    @app.errorhandler(404)
    def handle_other(err):
        return send_from_directory(static_folder, 'index.html')

    @app.errorhandler(BadRequestException)
    def handle_bad_request(err):
        return {"message": str(err)}, 400

    @app.errorhandler(ValidationException)
    def handle_validation_exception(err):
        return {"message": str(err)}, 422

    @app.errorhandler(NotFoundException)
    def handle_not_found_exception(err):
        return {"message": str(err)}, 404



    return app
