from datetime import datetime

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from pyramid.response import Response

from ..models import DBSession, User

@view_config(route_name='new_user', renderer='users/new.mako')
def new(req):
    save_url = req.route_url('new_user')
    return {'save_url': save_url}
    
@view_config(route_name='login_user', renderer='users/login.mako')
def login(req):
    
    if "form.submitted" in req.params:
        username = req.params.get('username')
        password = req.params.get('password')        
        return Response("Login Form submitted, Username: %s, Password: %s" % (username, password))
        
    return dict(
        login_url = req.route_url('login_user')
        )