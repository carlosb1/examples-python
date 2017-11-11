import flask
import flask.ext.sqlalchemy
import flask.ext.restless
import datetime
import os

from flask import Response

app = flask.Flask(__name__, static_url_path='')

app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = flask.ext.sqlalchemy.SQLAlchemy(app)

@app.route('/')
def root():
    return app.send_static_file('index.html')



class News(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    link = db.Column(db.Unicode, unique= True)
    received_date = db.Column(db.DateTime(), default=datetime.datetime.now)
    analysed_date = db.Column(db.DateTime())
    status = db.Column(db.Unicode)
    info = db.Column(db.Unicode)


db.create_all()

manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(News,methods=['GET','POST','DELETE'])
app.run()



