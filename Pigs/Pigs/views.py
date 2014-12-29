"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Pigs import app

my_pigs = [
    { "id" : 1,
     "name" : "Stud",
     "dob": "1.8.14",
     "sex" : "male"},
     {"id" : 2,
      "name" : "Minnie",
      "dob" : "24.8.14",
      "sex" : "female"},
     {"id" : 3,
      "name" : "Moo",
      "dob" : "24.8.14",
      "sex" : "female"},
    ]
list_of_pigs = ["Stud", "Minnie", "Moo"]

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    
    return render_template('welcomepage.html', welcome = "Welcome", to="to", my="my", guineapigs="Guinea Pigs!") 


@app.route('/pig/<id>')
def pig(id):
    
    for pig in my_pigs:        
        if id == str(pig["id"]):            
            return render_template('pigs.html', pigname = pig["name"], pigdob = pig["dob"], pigsex = pig["sex"])

    return "Pig not found"  
       
            
            
            
   
        
@app.route('/herd')
def herd_list():

    return render_template('listofpigs.html', pig = list_of_pigs)

  

    
    
   

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
