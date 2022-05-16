from flask import render_template
from market import app
from market.models import Item
from market.controller import home

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    print("Market Page has been hit")
    # add_item()
    items = Item.query.all()
    return render_template('market.html', items=items)

