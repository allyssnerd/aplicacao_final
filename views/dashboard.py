
import flask

from models.user import User


blueprint = flask.Blueprint('dashboard', __name__)

@blueprint.route('/dashboard')
def get_home():
    def to_dict(u):
        return {
            'name': u.name,
            'email': u.email,
            'password': u.password
        }

    users = User.get_all_users()
    context = {
        'users': [ to_dict(u) for u in users ]
    }

    return flask.render_template('dashboard.html', context=context)
