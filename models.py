# from runner import db
#
#
# class Buttons(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     srs = db.Column(db.String, unique=True, nullable=False)
#     href = db.Column(db.String, unique=True, nullable=False)
#     name = db.Column(db.String, unique=True, nullable=False)
#
#
# class Course(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String, unique=True, nullable=False)
#     description = db.Column(db.String, unique=False, nullable=False)
#     bonuses = db.relationship('Bonuses', backref='crs')
#     imgSrc = db.Column(db.String, unique=False, nullable=True)
#
#
# class Bonuses(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     description = db.Column(db.String, unique=False, nullable=False)
#     imgSrc = db.Column(db.String, unique=False, nullable=True)
#     crs_id = db.Column(db.Integer, db.ForeignKey('course.id'))
