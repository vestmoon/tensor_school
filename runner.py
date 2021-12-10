from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy

from models import *

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:root@127.0.0.1:5432/tensorproject"
db = SQLAlchemy(app)

class Buttons(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    srs = db.Column(db.String, unique=True, nullable=False)
    href = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, unique=True, nullable=False)


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, unique=False, nullable=False)
    bonuses = db.relationship('Bonuses', backref='crs')
    imgSrc = db.Column(db.String, unique=False, nullable=True)


class Bonuses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, unique=False, nullable=False)
    imgSrc = db.Column(db.String, unique=False, nullable=True)
    crs_id = db.Column(db.Integer, db.ForeignKey('course.id'))

db.create_all()



@app.route('/', methods=['POST', 'GET'])
def main_page():
    if request.method == 'GET':
        # добавить тру экзепт
        buttonsList = Buttons.query.all()
        return render_template('mainPageRefactor.html', buttonsList=buttonsList)
    else:
        pass


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/activity')
def activity():
    return "тут что то про наши движухи"

class Course:
    name = ""
    description = ""
    bonuses = []    
    img = ""

    def __init__(self, name, description, bonuses, img):
        Course.name = name        
        Course.description = description
        Course.bonuses=bonuses
        Course.img = img
   
@app.route('/design')
def disign():
    # course = Course.query.filter_by(name='Проектирование').first()
    name = "Проектирование"
    description = "Этот курс посвящен тому, чтобы ты научился планировать и оценивать свои задумки, составлять требования к будующим проектам, научился строить макеты и прототипы, а также их тестировать!"
    img = "static/computer.png"
    bonuses = []  
    bonuses.append(('static/icons/Circled 10.png',"10 подробных лекций  с материалами"))
    bonuses.append(('static/icons/Diploma.png',"Сертификат о прохождении курса"))
    bonuses.append(('static/icons/Resume.png',"Коллекцию новых работ в свое портфолио"))   
    course = Course(name, description, bonuses, img)    
    return render_template("coursePage.html", course=course)


@app.route('/frontend')
def frontend():
    # course = Course.query.filter_by(name='Проектирование').first()
    name = "Frontend"
    description = "Что-нибудь про front!"
    img = "static/computer.png"
    bonuses = []  
    bonuses.append(('static/icons/Circled 10.png',"10 подробных лекций  с материалами"))
    bonuses.append(('static/icons/Diploma.png',"Сертификат о прохождении курса"))
    bonuses.append(('static/icons/Resume.png',"Коллекцию новых работ в свое портфолио"))   
    course = Course(name, description, bonuses, img)    
    return render_template("coursePage.html", course=course)


@app.route('/backend')
def backend():
    # course = Course.query.filter_by(name='Проектирование').first()
    name = "Backend"
    description = "Что-нибудь про back!"
    img = "static/computer.png"
    bonuses = []  
    bonuses.append(('static/icons/Circled 10.png',"10 подробных лекций  с материалами"))
    bonuses.append(('static/icons/Diploma.png',"Сертификат о прохождении курса"))
    bonuses.append(('static/icons/Resume.png',"Коллекцию новых работ в свое портфолио"))   
    course = Course(name, description, bonuses, img)    
    return render_template("coursePage.html", course=course)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
