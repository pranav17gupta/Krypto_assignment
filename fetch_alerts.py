from flask import Flask, request, jsonify 
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
from flask_restful import Resource, Api

app = Flask(__name__) 
api = Api(app) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///Alerts.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) 
ma = Marshmallow(app)

/*fetching all the alerts with status if no alertid is appended at URL but fetching selected alerts if alertid is appended*/
@staticmethod
def fetchAllAlerts():
    try: id = request.args['alertid']
    except Exception as _: id = None

    if not id:
        alert = User.query.all()
        return jsonify(users_schema.dump(alerts))
    alert = Alerts.query.get(id)
    return jsonify(user_schema.dump(alert))
  
/*fetching the alerts having the given status*/
@staticmethod
  def fetchAlertsByStatus():
    try: status = request.args['status']
    except Exception as _: status = None

    if not id:
        alert = User.query.all()
        return jsonify(users_schema.dump(alerts))
    alert = Alerts.query.get(status)
    return jsonify(user_schema.dump(alert))
  
  
