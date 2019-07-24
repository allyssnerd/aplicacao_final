
import flask

from models.user import User


blueprint = flask.Blueprint('sign_up', __name__)

@blueprint.route('/sign-up', methods=[ 'GET', 'POST' ])
def sign_up():
    
    context = {

    }
    
    if flask.request.method == 'POST':

        user = User.find_by_email(flask.request.form['email'])

        if not user:
            user = User(**flask.request.form)

        user.name = flask.request.form['name']
        user.password = flask.request.form['password']
        
        user.save()
        
        return flask.redirect('/sign-in')

    return flask.render_template('sign-up.html', context=context)