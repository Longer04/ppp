import functools
from typing import Callable
from flask import session, flash, redirect, url_for, current_app


def requires_login(f: Callable) -> Callable:
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('email'):
            flash('Trzeba się zalogować aby przejsć dalej.', 'danger')
            return redirect(url_for('users.login_user'))
        return f(*args, **kwargs)

    return decorated_function


def requires_admin(f: Callable) -> Callable:
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('email') != current_app.config.get('ADMIN', ''):
            flash('Trzeba być administatorem aby przejść dalej.', 'danger')
            return redirect(url_for('users.login_user'))
        return f(*args, **kwargs)

    return decorated_function
