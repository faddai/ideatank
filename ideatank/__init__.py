from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import DBSession

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('ideas-root', '/ideas')
    config.add_route('ideas', 'ideas/all')
    config.add_route('new_idea', '/ideas/new')
    config.add_route('view_idea', '/ideas/{id}')
    config.add_route('ideas_by_cat','/ideas/category/{cat_id}')    
    config.add_route('delete_idea', '/ideas/delete/{id}')
    config.add_route('new_user', 'users/new')
    config.add_route('login_user', 'users/login')
    config.add_route('categories','/categories')    
    
    
    config.scan()
    return config.make_wsgi_app()

