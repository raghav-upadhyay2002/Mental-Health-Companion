from flask import Flask, render_template, request, redirect, url_for
import openai

app = Flask(__name__)
USER_CREDENTIALS = {
    'username': 'admin',
    'password': 'pass123'
}

@app.route('/')
def home():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method== 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username== USER_CREDENTIALS['username'] and password==USER_CREDENTIALS['password']:
            return redirect(url_for('personal'))
        else:
            return render_template('login.html', error="Invalid credentials. Please try again.")
    return render_template('login.html')

@app.route('/personal')
def personal():
    return render_template('personal.html')

if __name__ == '__main__':
    app.run(debug=True)