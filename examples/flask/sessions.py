from flask import Flask, flash, redirect, render_template, request, url_for, session

app = Flask(__name__)
app.secret_key = 'zzA0Zr98j/3yX R~XHH!jmN]LWX/,?RT12'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])

def login():
    error = None
    if request.method == 'POST':
        if session['username'] != request.form['username']:
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    # Start flask application on port 5678 - http://localhost:5678
    app.run(host="0.0.0.0", port=5678)
