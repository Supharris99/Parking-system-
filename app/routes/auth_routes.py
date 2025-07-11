from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.services.auth_service import AuthService
from functools import wraps

auth_bp = Blueprint('auth', __name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not AuthService.is_authenticated():
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        success, result = AuthService.login(username, password)
        
        if success:
            flash('Login berhasil!', 'success')
            return redirect(url_for('admin'))
        else:
            flash(result, 'danger')
            
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    AuthService.logout()
    flash('Anda telah berhasil logout', 'success')
    return redirect(url_for('index')) 