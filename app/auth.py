from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
from app.models import User
from app import db, bcrypt

auth_bp = Blueprint('auth', __name__)

class RegisterForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[InputRequired(), Length(min=4, max=100)])
    password = PasswordField('Пароль', validators=[InputRequired(), Length(min=8, max=80)])
    confirm_password = PasswordField('Подтвердите пароль', validators=[InputRequired(), EqualTo('password', message='Пароли должны совпадать')])
    submit = SubmitField('Зарегистрироваться')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Это имя пользователя уже занято.')

class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[InputRequired(), Length(min=4, max=100)])
    password = PasswordField('Пароль', validators=[InputRequired(), Length(min=8, max=80)])
    submit = SubmitField('Войти')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Регистрация успешна!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            flash('Вход выполнен успешно!', 'success')
            return redirect(url_for('smm.dashboard'))
        else:
            flash('Неверные учетные данные', 'danger')
    return render_template('login.html', form=form)

@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Выход выполнен успешно.', 'success')
    return redirect(url_for('auth.login'))
