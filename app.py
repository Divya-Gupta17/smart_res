# from flask import Flask, render_template, request, redirect, url_for, session, jsonify
# import mysql.connector
# import os
# import re



# app = Flask(__name__)
# app.secret_key = 'supersecretkey'
# # Load model and encoders
# app.secret_key = os.urandom(24)
# # Database connection
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="smartes"
# )
# cursor = db.cursor()
# @app.route('/home')
# def home():
#     if 'user_id' in session:
#         return render_template('index.html')
#     else:
#         return redirect(url_for('login'))

# @app.route('/login_validation', methods=['POST'])
# def login_validation():
#     email = request.form.get('email')
#     password = request.form.get('password')

#     cursor.execute("SELECT * FROM `` WHERE `email` = %s AND `password` = %s", (email, password))
#     users = cursor.fetchall()

#     if len(users) > 0:
#         session['user_id'] = users[0][0]
#         session['firstname'] = users[0][1]  # Assuming the first name is stored at index 1
#         print(f"User ID: {session['user_id']}, Firstname: {session['firstname']}")  # Debugging session values
#         return redirect(url_for('home'))
#     else:
#         flash('Invalid Email or Password', 'danger')
#         return redirect(url_for('login'))

# @app.route('/add_user', methods=['POST'])
# def add_user():
#     firstname = request.form.get('ufirstName')
#     lastname = request.form.get('ulastName')
#     email = request.form.get('uemail')
#     password = request.form.get('upassword')

#     sql = "INSERT INTO `user` (`id`, `firstname`, `lastname`, `email`, `password`) VALUES (NULL, %s, %s, %s, %s)"
#     values = (firstname, lastname, email, password)

#     try:
#         cursor.execute(sql, values)
#         conn.commit()
#         flash('Registration Successful! Please login.', 'success')
#         return redirect(url_for('login'))
#     except mysql.connector.Error as err:
#         print(f"Database Error: {err}")
#         flash('Registration failed. Try again.', 'danger')
#         return redirect(url_for('register'))

# @app.route('/logout')
# def logout():
#     session.pop('user_id', None)
#     return redirect(url_for('index'))

# # @app.route('/', methods=['GET', 'POST'])
# # def login():
# #     msg = ''
# #     if request.method == 'POST':
# #         username = request.form['username']
# #         password = request.form['password']
# #         cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
# #         account = cursor.fetchone()
# #         if account:
# #             session['loggedin'] = True
# #             session['username'] = username
# #             return redirect(url_for('home'))
# #         else:
# #             msg = 'Incorrect username or password!'
# #     return render_template('login.html', msg=msg)

# @app.route('/home')
# def home():
#     if 'loggedin' in session:
#         return render_template('index.html')
#     return redirect(url_for('login'))

# @app.route('/menu')
# def menu():
#     cursor.execute("SELECT * FROM menu")
#     items = cursor.fetchall()
#     return render_template('menu.html', items=items)

# @app.route('/cart')
# def cart():
#     return render_template('cart.html')

# @app.route('/place_order', methods=['POST'])
# def place_order():
#     data = request.get_json()
#     items = data['items']
#     total = data['total']
#     cursor.execute("INSERT INTO orders (username, total, status) VALUES (%s, %s, %s)", (session['username'], total, 'Pending'))
#     db.commit()
#     return jsonify({'message': 'Order placed successfully!'})

# @app.route('/dashboard')
# def dashboard():
#     cursor.execute("SELECT * FROM orders")
#     orders = cursor.fetchall()
#     return render_template('dashboard.html', orders=orders)

# @app.route('/logout')
# def logout():
#     session.pop('loggedin', None)
#     session.pop('username', None)
#     return redirect(url_for('login'))

# if __name__ == "__main__":
#     app.run(debug=True)



from flask import Flask, render_template, url_for, redirect, session, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    """Renders the home/index page."""
    return render_template('index.html')

@app.route('/home')
def home():
    """Renders the home/index page."""
    return render_template('index.html')

@app.route('/owner')
def owner():
    """Renders the home/index page."""
    return render_template('owner.html')

@app.route('/login')
def login():
    """Renders the login page."""
    return render_template('login.html')

@app.route('/register')
def register():
    """Renders the registration page."""
    return render_template('register.html')

@app.route('/menu')
def menu():
    """Renders the menu page."""
    return render_template('menu.html')

@app.route('/cart')
def cart():
    """Renders the shopping cart page."""
    return render_template('cart.html')

@app.route('/dashboard')
def dashboard():
    """Renders the owner's dashboard page."""
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    """Handles user logout and redirects to the login page."""
    session.pop('user_id', None)
    session.pop('loggedin', None)
    session.pop('username', None)
    flash('Logged out successfully.', 'info')
    return redirect(url_for('login'))

# The following routes were previously interacting with the database.
# If you still need the validation and user creation logic, you'll need
# to implement that separately (e.g., in a different part of your application
# or connect to a database when these specific actions are needed).

# @app.route('/login_validation', methods=['POST'])
# def login_validation():
#     # ... (Database interaction removed)
#     return redirect(url_for('home'))

# @app.route('/add_user', methods=['POST'])
# def add_user():
#     # ... (Database interaction removed)
#     return redirect(url_for('login'))

# @app.route('/place_order', methods=['POST'])
# def place_order():
#     # ... (Database interaction removed)
#     return jsonify({'message': 'Order placed successfully!'})

if __name__ == "__main__":
    app.run(debug=True)