from flask import Flask
from .routes import api_blueprint
from .config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

# Database
db = SQLAlchemy(app)

# Register Blueprints
app.register_blueprint(api_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
