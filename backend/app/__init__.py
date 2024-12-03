from flask import Flask
from flask_cors import CORS
from app.config import Config
from app.database import db
from app.routes import api
from flask_migrate import Migrate
# from dotenv import load_dotenv

# load_dotenv()

migrate = Migrate()

def init_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    with app.app_context():
         db.init_app(app)
         db.create_all()
    # migrate.init_app(app, db)
    return app

app = init_app()
CORS(app)


app.register_blueprint(api, url_prefix="/api")

if __name__ == '__main__':
    app.run()
