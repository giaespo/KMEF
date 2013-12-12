#!/usr/bin/python3
from .core.models import Model
from .core.fields import StringField,PasswordField,ArrayField
from .core.plugin.injected import Persistent,FilterRights,FilterUsers
 


class User(Model):
    
    input={
           'user':StringField('key@Login.User',''),
           'session':StringField('key@Login.SessionId',''),
           }
           
    output={
    'Name':StringField('User.Name','',[Persistent]),
    'UserType':StringField('User.Type','',[Persistent]),
    }  


    

class Login(Model):
    
    input={
           'user':StringField('Login.User','',[Persistent]),
           'passwd':PasswordField('Password','')
           }
           
    output={
            'SessionId':StringField('Login.SessionId','',[Persistent]),
            }    


