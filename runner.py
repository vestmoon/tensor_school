from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy


# Костыльно ориентированное программирование, нужно подумать как это можно сделать нормально
def eng_to_rus(s):
    if s == "design":
        return 'Проектирование'
    elif s == "backend":
        return 'Backend'
    elif s == "frontend":
        return 'Frontend'
    elif s == "CICD":
        return 'CI/CD'
    elif s == "testing":
        return 'Тестирование'
    else:
        return 'Базы данных'


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:admin@127.0.0.1:5432/tensorproject"
db = SQLAlchemy(app)
# "postgresql://postgres:root@127.0.0.1:5432/tensorProject"

# Добавлять в бд на КАКОЙ курс зареган чел
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fio = db.Column(db.String, unique=False, nullable=False)
    city = db.Column(db.String, unique=False, nullable=False)
    number = db.Column(db.String, unique=False, nullable=False)
    mail = db.Column(db.String, unique=False, nullable=False)

    def __repr__(self):
        return f"<users {self.id}"


class Buttons(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    src = db.Column(db.String, unique=True, nullable=False)
    href = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, unique=True, nullable=False)


association_table = db.Table('association',
                             db.Column('course_id', db.Integer, db.ForeignKey('course.id'), primary_key=True),
                             db.Column('bonus_id', db.Integer, db.ForeignKey('bonus.id'), primary_key=True))


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, unique=False, nullable=False)
    img_src = db.Column(db.String, unique=False, nullable=True)
    bonuses = db.relationship('Bonus', secondary=association_table, lazy='subquery',
                              backref=db.backref('courses', lazy=True))


class Bonus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, unique=False, nullable=False)
    img_src = db.Column(db.String, unique=False, nullable=True)


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


@app.route('/<href>', methods=['POST', 'GET'])
def controller(href):
    if request.method == 'GET':
        course = Course.query.filter_by(name=eng_to_rus(href)).first()
        return render_template("coursePage.html", course=course)
    else:
        try:  # Ловить конкретную ошибку
            u = Users(fio=request.form['user_fio'],
                      city=request.form['user_city'],
                      number=request.form['user_number'],
                      mail=request.form['user_mail'])
            db.session.add(u)
            db.session.commit()
            return redirect(href)
        except:
            db.session.rollback()
            print("Ошибка добавления в бд")  # Добавить логированние нормальное
            return redirect('/design')


if __name__ == '__main__':
    app.run(debug=True, port=8080)
