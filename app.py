from flask import Flask,render_template,request,jsonify
from wtforms import SelectField
from flask_wtf import FlaskForm 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY']= 'sercets'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testvcampus.db'
db=SQLAlchemy(app)

class Form(FlaskForm):
    schools = SelectField('Schools', choices=[])

class Schools(db.Model):
    __tablename__ = 'schools'
   
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
   
class Departments(db.Model):
    __tablename__ = 'department'
   
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    school_id = db.Column(db.Integer)
   

class Form(FlaskForm):
    Schools = SelectField('schools', choices=[])
    Departments = SelectField('departments', choices=[])
   
          
@app.route('/', methods=['GET', 'POST'])
def index():
    form = Form()
    form.Schools.choices = [(school.id, school.name) for school in Schools.query.all()]
   
    if request.method == 'POST':
       
        school = Schools.query.filter_by(id=form.country.data).first()
        Departments = Departments.query.filter_by(id=form.state.data).first()
        return '<h1>Schools : {}, Departments : {}</h1>'.format(school.name, Departments.name)
    return render_template('index.html', form=form)
  
@app.route('/department/<get_department>')
def statebyschool(get_department):
    departments = Departments.query.filter_by(school_id=get_department).all()
    departmentsArray = []
    for city in state:
        stateObj = {}
        stateObj['id'] = city.id
        stateObj['name'] = city.name
        stateArray.append(stateObj)
    return jsonify({'statecountry' : stateArray})
   




if __name__ == '__main__':
    app.run(debug=True)