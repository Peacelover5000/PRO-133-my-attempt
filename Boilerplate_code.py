#Importing flask module in the project
from flask import Flask, render_template 
#Create an object of the Flask class
app = Flask(__name__)
#The route() function of the Flask class 

@app.route("/student_activity.no.2")

#‘/’ URL is bound with first_flask function.
def student_webpage(): 
    name = 'Nobody knwos' 
    return render_template('index.html',student_name=name)
app.run(debug=True)
