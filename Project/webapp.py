from flask import Flask, render_template

webapp = Flask(__name__)
webapp.secret_key = 'supersecretmre'

@webapp.route('/')
def index():
    return render_template('landing.html')

@webapp.route('/register')
def register():
    return render_template('register.html')

@webapp.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    webapp.run(host = '0.0.0.0', port = 5000, debug=True)