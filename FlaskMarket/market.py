from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# URI -> uniform resource identifier
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'  # database location
db = SQLAlchemy(app)    # create the database and pass in the app 

# Model for stirage in the database 
class Item(db.Model): 
    id = db.Column(db.Integer(), primary_key=True)
    # columns, type, constraints,     don't have null value and are unique
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

# @app.route('/')  # decorator 
# def hello_world():
#     return 'Hello, World!'

# @app.route('/about/<username>') 
# def about_page(username):
#     return f'About {username}'

@app.route('/')  
@app.route("/home")    # you can also add double routing
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = [
    {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
]
    return render_template('market.html', items = items)   # sending data to the html page