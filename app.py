
import sys
import os

import flask
import sqlalchemy
import dotenv

from views.sign_in import blueprint as sign_in 
from views.sign_up import blueprint as sign_up
from views.dashboard import blueprint as dashboard

from models.user import User


app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.redirect('/sign-in')

if __name__ == "__main__":
    
    current_module = os.path.abspath(os.path.curdir)
    sys.path.append(current_module)

    dotenv.load_dotenv()

    engine = sqlalchemy.create_engine(os.getenv('DATABASE'))
    metadata = sqlalchemy.MetaData(bind=engine)

    User.initialize(metadata)

    metadata.create_all(engine)

    app.secret_key = 'secret'
    
    app.register_blueprint(sign_in)
    app.register_blueprint(sign_up)
    app.register_blueprint(dashboard)
    
    app.run(debug=True)