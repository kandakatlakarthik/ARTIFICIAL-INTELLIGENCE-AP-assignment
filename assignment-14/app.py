from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'a_very_secret_key_for_sessions' # Needed for sessions and flashing

@app.route('/')
def index():
    """Serves the login page."""
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    """Handles the login form submission."""
    username = request.form.get('username')
    password = request.form.get('password')

    # Basic server-side validation
    if not username or not password:
        flash('Username and password are required!', 'error')
        return redirect(url_for('index'))

    # On successful login, print username and store it in the session
    print(f"Successful login for username: {username}")
    session['username'] = username # Store username in the session

    # Redirect to a success page or dashboard
    return redirect(url_for('success'))

@app.route('/success')
def success():
    """Displays the success page after login."""
    # Check if user is logged in (i.e., username is in session)
    if 'username' in session:
        username = session['username']
        return render_template('success.html', username=username)
    # If user is not logged in, redirect to login page
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Use debug=True for development, which provides auto-reloading
    # and a debugger. Turn it off for production.
    app.run(debug=True)