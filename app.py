from flask import Flask, render_template, request, redirect, session
import psycopg2
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Database connection settings
db_host = 'db'
db_port = '5432'
db_name = 'postgres'
db_user = 'myuser'
db_password = 'postgres'


def create_table():
    conn = psycopg2.connect(
        host=db_host,
        port=db_port,
        dbname=db_name,
        user=db_user,
        password=db_password
    )
    cur = conn.cursor()

    # Check if the table already exists
    cur.execute("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'users')")
    if not cur.fetchone()[0]:
        # Create the table if it doesn't exist
        cur.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, username VARCHAR(255), password VARCHAR(255))")
        conn.commit()

    cur.close()
    conn.close()


def create_user(username, password):
    conn = psycopg2.connect(
        host=db_host,
        port=db_port,
        dbname=db_name,
        user=db_user,
        password=db_password
    )
    cur = conn.cursor()

    # Check if the username already exists
    cur.execute("SELECT * FROM users WHERE username = %s", (username,))
    if cur.fetchone():
        cur.close()
        conn.close()
        return False

    # Insert new user into the table
    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()

    cur.close()
    conn.close()
    return True


def authenticate_user(username, password):
    conn = psycopg2.connect(
        host=db_host,
        port=db_port,
        dbname=db_name,
        user=db_user,
        password=db_password
    )
    cur = conn.cursor()

    # Check if the username and password match
    cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cur.fetchone()

    cur.close()
    conn.close()

    if user:
        return True
    else:
        return False


@app.route('/')
def index():
    if 'username' in session:
        return f'Welcome, {session["username"]}! <a href="/logout">Logout</a>'
    else:
        return 'You are not logged in. <a href="/login">Login</a> or <a href="/register">Register</a>'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if authenticate_user(username, password):
            session['username'] = username
            return redirect('/')
        else:
            return 'Invalid username or password. <a href="/login">Try again</a>'

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if create_user(username, password):
            return redirect('/login')
        else:
            return 'Username already exists. <a href="/register">Try again</a>'

    return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')


if __name__ == '__main__':
    create_table()  # Create the table before running the application
    app.run(host='0.0.0.0')
