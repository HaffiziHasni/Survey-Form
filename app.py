from datetime import timedelta
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#model for database
app.secret_key="hello"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///survey.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.permanent_session_lifetime=timedelta(minutes=5)
db=SQLAlchemy(app)

class survey(db.Model):
    _id =db.Column("id", db.Integer, primary_key=True)
    name=db.Column("Name",db.String(100))
    email=db.Column("email",db.String(100))
    number=db.Column("Age", db.String(100))
    dropdown=db.Column("Position", db.String(100))
    know=db.Column("Recruiter's Knowledge", db.String(100))
    interest=db.Column("Other positions", db.String(100))
    comment=db.Column("Comment", db.String(1000))
#end here for database
    
   


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html") #shows this first, no need to put anything

@app.route('/submission', methods=['GET', 'POST']) #.submission will be show after form is submitted, i.e. this is the one you need to edit because it is the one that will do the work.
def submit():
    


    name=request.form.get("name")
    email=request.form.get("email")
    number=request.form.get("number")
    dropdown=request.form.get("dropdown")
    know=request.form.get("know")
    interest=request.form.getlist("interest") #getlist for multiple checkbox
    comment=request.form.get("comment")
    print("name: ",name)
    print("email: ", email)
    print("Age: ",number)
    print("Position interviewed: ",dropdown)
    print("Knowledge: ",know)
    print("Other interest:",interest)
    print("Comment: ",comment)

   
    return render_template("submission.html")

db.create_all() #create db
app.run(host='0.0.0.0', port=81)