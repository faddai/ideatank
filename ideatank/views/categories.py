from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound

from ..models import DBSession, Category

@view_config(route_name='categories', renderer='categories/list.mako')
def categories(req):
    
    db = DBSession()
    categories = db.query(Category).filter_by().all()
    
    if categories is None:
        return HTTPFound(location = req.route_url('ideas'))
    
    return dict(
        categories = categories,
        q = db.query(Category)
    )