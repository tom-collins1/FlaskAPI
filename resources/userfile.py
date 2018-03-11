#See FlaskAPISection5LogginIN.py for notes

import sqlite3 as sql
from flask_restful import Resource, reqparse
from models.user import UserModel
#The user must be different from the resource (like item and item list was) we use to sign up
#use a request parser that accepts a username and password, parse the json going into the post request

#Now when we go to auth endpoint no user will exist, we will need to register first

class UserRegister(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('username', 
    type = str,
    required = True,
    help = 'This field cannot be blank')
    parser.add_argument('password', 
    type = str,
    required = True,
    help = 'This field cannot be blank')
    
    
    def post(self):
        data = UserRegister.parser.parse_args()
        
        if UserModel.find_by_username(data['username']):
            return {'message': 'User already exists'}, 400
        
        user = UserModel(**data)
        user.save_to_db()
        return {'message': 'User created successfully'}, 201
    
