# from flask import Flask, render_template, request
from soil_crop_data import get_crops_by_soil
from weather_module import get_weather_info



from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from models import db, User
from werkzeug.security import generate_password_hash, check_password_hash




app = Flask(__name__)




app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agri.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with app
db.init_app(app)

# Create tables manually with app context
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    if 'user' in session:
        return render_template('home.html', user=session['user'])
    return redirect(url_for('login'))




@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])

        if User.query.filter_by(username=username).first():
            flash('Username already exists!')
            return redirect(url_for('register'))

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registered successfully! Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html')





@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password_input = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password_input):
            session['user'] = user.username
            flash('Login successful!')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged out successfully!')
    return redirect(url_for('login'))






@app.route('/dashboard')
def dashboard():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    soil_type = request.form['soil_type']
    location = request.form['location']
    crops = get_crops_by_soil(soil_type)
    weather = get_weather_info(location)
  

    return render_template('result.html', soil=soil_type, location=location, crops=crops, weather=weather)

if __name__ == '__main__':
    app.run(debug=True)







# app = Flask(__name__)

# if __name__ == '__main__':
#     app.run(debug=True)
