from flask_restful import Api
from flask import Flask
from flask_jwt import JWT
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'     #where we;re going to store our db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'Test'
api = Api(app)   


#we use a flask decorator to build our table in sqlachemy, before all any requests @ 'sqlite:///data.db' unless already exists
#db imported in closing __main__ check
@app.before_first_request
def create_tables():
    db.create_all()  #now don't have to manually create the table itself that we want to populate.

import os
os.chdir(r'C:\Users\Tom\Desktop\MyCodes\FlaskAPIsection6')

from Security_v3 import authenticate, identity
from resources.userfile import UserRegister
from resources.items import Item, ItemList
from resources.store import Store, StoreList

jwt = JWT(app, authenticate, identity)

api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister, '/register')


if __name__=='__main__':  
    from db import db
    db.init_app(app)         
    app.run(port=5000, debug=True)    