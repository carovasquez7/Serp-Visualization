from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

#from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

# Database Configurations
app = Flask(__name__)
DATABASE = 'waynakay'
PASSWORD = 'citiaps2017'
USER = 'root'
HOSTNAME = 'mysqlserver'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@%s/%s' % (USER,
                                                                 PASSWORD,
                                                                 HOSTNAME,
                                                                 DATABASE)
db = SQLAlchemy(app)

# Database migration command line
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

participation = db.Table('participation',
                         db.Column(
                             'announcement_id',
                             db.Integer,
                             db.ForeignKey('announcement.id'),
                             primary_key=True),
                         db.Column(
                             'volunteer_id',
                             db.Integer,
                             db.ForeignKey('volunteer.id'),
                             primary_key=True))

template_have_attribute = db.Table('template_have_attribute',
                                   db.Column(
                                       'template_id',
                                       db.Integer,
                                       db.ForeignKey('template.id'),
                                       primary_key=True),
                                   db.Column(
                                       'attribute_id',
                                       db.Integer,
                                       db.ForeignKey('attribute.id'),
                                       primary_key=True))

# Temporary
criterion_have_attribute = db.Table('criterion_have_attribute',
                                    db.Column(
                                        'criterion_id',
                                        db.Integer,
                                        db.ForeignKey('criterion.id'),
                                        primary_key=True),
                                    db.Column(
                                        'attribute_id',
                                        db.Integer,
                                        db.ForeignKey('attribute.id'),
                                        primary_key=True))
"""
# Temporal: Por ahora asumir que no tienen valores
volunteer_have_attribute = db.Table('volunteer_have_attribute',
                         db.Column('volunteer_id', db.Integer, db.ForeignKey('volunteer.id'), primary_key=True),
                         db.Column('attribute_id', db.Integer, db.ForeignKey('attribute.id'), primary_key=True)
                         )
"""
"""
class Criterion_have_Attribute(db.Model):
    __tablename__ = 'criterion_have_attribute'
    criterion_id = db.Column(db.Integer, db.ForeignKey('criterion.id'), primary_key=True)
    attribute_id = db.Column(db.Integer, db.ForeignKey('attribute.id'), primary_key=True)
    value = db.Integer
    attribute = db.relationship("Attribute")
"""

Volunteer = db.Table('volunteer',
                     db.Column('id', db.Integer, primary_key=True),
                     db.Column('volunteer_id', db.Integer),
                     db.Column(
                         'attribute_id',
                         db.Integer,
                         db.ForeignKey('attribute.id'),
                         primary_key=True), db.Column('value', db.Integer))
""" # TODO
class Volunteer_Attribute(db.Model):
    __tablename__ = 'volunteer_attribute'
    id = db.Column(Integer, primary_key=True)
    volunteer_id = db.Column(db.Integer, db.ForeignKey('volunteer.id'), primary_key=True)
    attribute_id = db.Column(db.Integer, db.ForeignKey('attribute.id'), primary_key=True)
    value = db.Column(db.Integer)
"""


class Announcement(db.Model):
    __tablename__ = 'announcement'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(80))
    required = db.Column(db.Integer)
    selected = db.Column(db.Integer)
    createdAt = db.Column(db.Integer)
    description = db.Column(db.String(80))
    template_id = db.Column(
        db.Integer, db.ForeignKey('template.id'), nullable=False)

    def __init__(self, title, required, selected, createdAt, description,
                 template_id):
        self.title = title
        self.required = required
        self.selected = selected
        self.createdAt = createdAt
        self.description = description
        self.template_id = template_id

    def __repr__(self):
        return '<Announcement %r>' % (self.title)


class Template(db.Model):
    __tablename__ = 'template'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(80))
    criterions = db.relationship("Criterion", backref="template", lazy=True)
    announcements = db.relationship(
        "Announcement", backref="template", lazy=True)
    attributes = db.relationship(
        'Attribute',
        secondary=template_have_attribute,
        lazy='subquery',
        backref=db.backref('templates', lazy=True))

    def __init__(self, name):
        self.name = name

    def __init__(self, name, criterions=[]):
        self.name = name
        self.criterions = criterions

    def __repr__(self):
        return '<Template %r>' % (self.category)


class Criterion(db.Model):
    __tablename__ = 'criterion'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(80))
    value = db.Column(db.Integer)
    template_id = db.Column(
        db.Integer, db.ForeignKey('template.id'), nullable=False)
    attributes = db.relationship(
        'Attribute',
        secondary=criterion_have_attribute,
        lazy='subquery',
        backref=db.backref('criterion', lazy=True))

    def __init__(self, name, value, template_id):
        self.name = name
        self.value = value
        self.template_id = template_id

    def __repr__(self):
        return '<Criterion %r>' % (self.name)


class Attribute(db.Model):
    __tablename__ = 'attribute'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(80))
    originalattribute_id = db.Column(
        db.Integer, db.ForeignKey('originalattribute.id'), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Attribute %r>' % (self.name)


class Originalattribute(db.Model):
    __tablename__ = 'originalattribute'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(80))
    attributes = db.relationship(
        'Attribute', backref='originalattribute', lazy=True)


"""
# TODO
class Volunteer(db.Model):
    __tablename__ = 'volunteer'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    #name = db.Column(db.String(80))
    #attributes = db.relationship('Attribute', backref='originalattribute', lazy=True)
"""


# TODO: Very bad fix, but is temporal (CRITICAL)
class VolunteerTemp(db.Model):
    __tablename__ = 'volunteertemp'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(80))


class CreateDB():
    def __init__(self, hostname=None):
        if hostname != None:
            HOSTNAME = hostname
        import sqlalchemy
        engine = sqlalchemy.create_engine('mysql://%s:%s@%s' %
                                          (USER, PASSWORD,
                                           HOSTNAME))  # connect to server
        engine.execute("CREATE DATABASE IF NOT EXISTS %s " %
                       (DATABASE))  # create db
        # TODO: Automatize create tables
        #db.create_all()


if __name__ == '__main__':
    manager.run()
