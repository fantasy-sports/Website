from flask import render_template, url_for, flash, redirect
from fancyoptimizer import app
from fancyoptimizer.forms import RegistrationForm, LoginForm
from fancyoptimizer.models import User, Post

posts = [
    {
        'author': 'Michael Muchane',
        'title': 'Hot Picks: March 3rd',
        'content': 'First post content',
        'date_posted': '9:46am, 03/03/19'
    },
    {
        'author': 'Sam Lubell',
        'title': 'Hot Picks: March 4th',
        'content': 'Second post content',
        'date_posted': '10:01am, 03/04/19'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@optimizer.com' and form.password.data == 'password': # temporary login credentials - https://youtu.be/UIJKdCIEXUQ (42:15)
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
