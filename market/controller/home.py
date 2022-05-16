from flask import render_template

def homePage():
    print("home page api has been hit")
    return render_template('home.html')
