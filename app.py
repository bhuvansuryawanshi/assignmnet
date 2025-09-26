from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import os

app = Flask(__name__)

# Database Connection
def get_connection():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST"),
        database=os.environ.get("DB_NAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASS")
    )

#Routes

@app.route('/')
def index():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users ORDER BY id")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    if name and email:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()
        cursor.close()
        conn.close()
    return redirect(url_for('index'))

@app.route('/update/<int:user_id>', methods=['POST'])
def update_user(user_id):
    name = request.form['name']
    email = request.form['email']
    if name and email:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET name=%s, email=%s WHERE id=%s", (name, email, user_id))
        conn.commit()
        cursor.close()
        conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
