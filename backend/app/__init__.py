from flask import Flask
from flask_cors import CORS
from app.config import Config
from app.database import db
from app.routes import api


app = Flask(__name__)

app.config.from_object(Config)

CORS(app)


with app.app_context():
    db.init_app(app)
    db.create_all()

app.register_blueprint(api, url_prefix="/api")

if __name__ == '__main__':
    app.run()
