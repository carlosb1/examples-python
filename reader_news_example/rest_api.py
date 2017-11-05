import flask
import flask.ext.sqlalchemy
import flask.ext.restless

app = flask.Flask(__name__)

app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = flask.ext.sqlalchemy.SQLAlchemy(app)

class News(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    link = db.Column(db.Unicode, unique= True)
    #received_date = db.Column(db.Date)
    #analysed_date = db.Column(db.Date)
    status = db.Column(db.Unicode)
    info = db.Column(db.Unicode)


db.create_all()

manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(News,methods=['GET','POST','DELETE'])
app.run()



