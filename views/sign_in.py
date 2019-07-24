
import flask

from models.user import User


blueprint = flask.Blueprint('sign_in', __name__)

@blueprint.route('/sign-in', methods=[ 'GET', 'POST' ])
def sign_in():

    context = {
        'email': '',
        'error_occurred': False,
    }

    if flask.request.method == 'POST':
        user = User.find_by_email(flask.request.form['email'])
        if not user:
            return flask.redirect('/sign-up')
        elif user.authenticate(flask.request.form['password']):
            flask.session['email'] = flask.request.form['email'] 
            return flask.redirect('/dashboard')
        else:
            context['email'] = flask.request.form['email']
            context['error_occurred'] = True
            
    return flask.render_template('sign-in.html', context=context)
    