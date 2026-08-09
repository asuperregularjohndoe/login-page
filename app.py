from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Change these to your real credentials
REAL_USERNAME = "admin"
REAL_PASSWORD = "Astrongpassword123?"

last_login = {"success": False, "username": ""}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    last_login['username'] = username

    if username == REAL_USERNAME and password == REAL_PASSWORD:
        last_login['success'] = True
        return redirect(url_for('dashboard'))
    else:
        last_login['success'] = False
        return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', success=last_login['success'], username=last_login['username'])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
