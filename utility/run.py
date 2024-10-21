from flask import Flask
from flasgger import Swagger # Only required if you want to use Swagger UI
import yaml
from api.routes import api_bp
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))

# Using Blueprints to organize routes in a Flask application
# https://flask.palletsprojects.com/en/2.0.x/blueprints/
# We are using Blueprints to organize our routes in our Flask application.  This
#  allows us to separate the routes into different files, which can help keep our
#  code organized and easier to maintain.  In this case, we have a single blueprint
#  that is defined in the api/routes.py file.  We import that blueprint here and
#  register it with our Flask application.  The blueprint is registered with a
#  prefix of "/api", which means that all routes defined in the blueprint will
#  be prefixed with "/api".  For example, a route defined in the blueprint as
#  "/users" will be accessible at "/api/users" in the application.


def create_app():
    app = Flask(__name__)

    # If you have provided an openapi.yaml file in the docs folder, load it
    # This will allow you to use Swagger UI to view and test your API endpoints
    #  Run the app and go to http://localhost:5000/apidocs to view the Swagger UI
    # Load OpenAPI specification from YAML file
    if Path.exists(Path("docs/openapi.yaml")):
        with open("docs/openapi.yaml", "r") as file:
            openapi_spec = yaml.safe_load(file)

        # Initialize Swagger with the OpenAPI spec
        swagger = Swagger(app, template=openapi_spec)

    # Register Blueprints
    app.register_blueprint(api_bp, url_prefix="/api")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)