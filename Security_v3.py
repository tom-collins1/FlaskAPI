#See v2 for notes 

import os
os.chdir(r'C:\Users\Tom\Desktop\MyCodes\FlaskAPIsection6')
from models.user import UserModel


from werkzeug.security import safe_str_cmp


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password,password):                                                 
        return user
        
#payload is the contents of the JWT token which we can authenicate on users who match to the payload.
def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)