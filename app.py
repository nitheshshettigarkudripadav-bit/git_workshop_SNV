from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
# A secret key is required to use Flask sessions securely
app.secret_key = 'your_secret_key_here'

# Hardcoded credentials
USERNAME = "admin"
PASSWORD = "password123"

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        entered_username = request.form['username']
        entered_password = request.form['password']
        
        if entered_username == USERNAME and entered_password == PASSWORD:
            session['user'] = entered_username
            return redirect(url_for('dashboard'))
        else:
            error = 'Invalid username or password. Please try again.'
            
    return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', user=session['user'])

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)