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

/*Inserting the alert*/
@staticmethod
def post():
    alertid = request.json['alertid']
    userif = request.json['userid']
    alertprice = request.json['alertprice']
    status = request.json['status']
    
    alert = Alerts(alertid, userid, alertprice, status)
    db.session.add(alert)
    db.session.commit()

    return jsonify({
        'Message': f'User {alertid} {userid} inserted.'
    })

