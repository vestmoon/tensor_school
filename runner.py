from flask import Flask, render_template, url_for, redirect, request, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:root@127.0.0.1:5432/tensorProject"
db = SQLAlchemy(app)
# "postgresql://postgres:root@127.0.0.1:5432/tensorProject"

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fio = db.Column(db.String, unique=False, nullable=False)
    city = db.Column(db.String, unique=False, nullable=False)
    number = db.Column(db.String, unique=False, nullable=False)
    mail = db.Column(db.String, unique=False, nullable=False)
    course = db.Column(db.String, unique=False, nullable=False)

    def __repr__(self):
        return f"<users {self.id}"


association_table = db.Table('association',
                             db.Column('course_id', db.Integer, db.ForeignKey('course.id'), primary_key=True),
                             db.Column('bonus_id', db.Integer, db.ForeignKey('bonus.id'), primary_key=True))


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # id
    name = db.Column(db.String, unique=True, nullable=False)  # Проектирование
    endpoint = db.Column(db.String, unique=True, nullable=False)  # design
    button_img = db.Column(db.String, unique=True, nullable=False)  # Путь до иконки
    description = db.Column(db.String, unique=False, nullable=False)  # Описание курса
    img_src = db.Column(db.String, unique=False, nullable=True)  # Картиинка справа
    bonuses = db.relationship('Bonus', secondary=association_table, lazy='subquery',
                              backref=db.backref('courses', lazy=True))


class Bonus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, unique=False, nullable=False)
    img_src = db.Column(db.String, unique=False, nullable=True)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("notFound.html")

@app.before_first_request
def setup():
    db.create_all()


@app.route('/', methods=['POST', 'GET'])
def main_page():
    if request.method == 'GET':
        courseList = Course.query.all()
        return render_template('mainPageRefactor.html', courseList=courseList)
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
    if href in [i.endpoint for i in Course.query.all()]:
        if request.method == 'GET':
            course = Course.query.filter_by(endpoint=href).first()
            return render_template("coursePage.html", course=course)
        else:
            try:  # Ловить конкретную ошибку
                u = Users(fio=request.form['user_fio'],
                          city=request.form['user_city'],
                          number=request.form['user_number'],
                          mail=request.form['user_mail'],
                          course="TODO")
                db.session.add(u)
                db.session.commit()
                return redirect(href)
            except:
                db.session.rollback()
                app.logger.error('Ошибка добавления в бд')
                return redirect('/')
    else:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
