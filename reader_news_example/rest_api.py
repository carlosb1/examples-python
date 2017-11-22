import flask
import flask.ext.sqlalchemy
import flask.ext.restless
import datetime
import os

from flask import Response

app = flask.Flask(__name__, static_url_path='')

DATABASE_URL = os.environ.get('DATABASE_URL','sqlite:///test.db')
app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL 
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
    publish_date = db.Column(db.DateTime())
    text = db.Column(db.Unicode)
    link_image = db.Column(db.Unicode)
    keywords = db.Column(db.Unicode)
    videos  = db.Column(db.Unicode)
    summary = db.Column(db.Unicode)
    title = db.Column(db.Unicode)
    




if __name__ == '__main__':
    db.create_all()
    port = int(os.environ.get('PORT',5000))
    manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)
    manager.create_api(News,methods=['GET','POST','DELETE'])
    app.run(host='0.0.0.0', port = port)



