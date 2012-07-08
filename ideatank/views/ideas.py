from datetime import datetime

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from ..models import (
    DBSession, Idea, Category
    )

@view_config(route_name='ideas-root')
@view_config(route_name='home')
def home(req):
    return HTTPFound(location = req.route_url('ideas') )
    
@view_config(route_name='ideas', renderer='ideas/all.mako')
def all_ideas(req):
    """
    List all ideas in the system. You should perhaps consider
    pagination at this point. In case, this goes viral
    """
    ideas = DBSession.query(Idea).all()
    
    if ideas is None:
        return Response('<h2>No idea has been added.</h2>', content_type="text/html", status_int=500)
        
    return {'ideas': ideas}
    
@view_config(route_name='ideas_by_cat', renderer='ideas/ideas_by_cat.mako')
def ideas_by_category(req):
    cat_id = req.matchdict['cat_id']
    db = DBSession()
    ideas = db.query(Idea).filter_by(category_id = cat_id).all()
    return dict(
        ideas = ideas
    )

@view_config(route_name='view_idea', renderer='ideas/view_idea.mako')
def view_idea(req):
    id = req.matchdict['id']
    db = DBSession()
    idea = db.query(Idea).filter_by(id = id).one()
    
    if idea is None:
        ## Flash a message telling user that this idea isn't there
        msg = "Sorry, you are trying to view an idea that doesn't exist."
        return HTTPFound(location = req.route_url('ideas'))
    
    return dict(
        idea = idea,
        
    )

@view_config(route_name="new_idea", renderer="ideas/new.mako")
def new(request):
    
    if "form_submitted" in request.POST:
        db = DBSession()
        cat = Category()
        
        idea = Idea()
        idea.author = "Jacob Hikins"
        idea.title = req.params.get('title')
        idea.description = req.params.get('description')
        idea.created_at = datetime.now()
        idea.category_id = req.params.get('category')
        db.add(idea)
        #request.session.flash("warning;New Category is saved!")
        return HTTPFound(location = request.route_url("ideas"))
        
    return dict(save_url=request.route_url("new_idea"))

"""
@view_config(route_name="category_edit", renderer="category/edit.html")
def edit(request):
    """" category edit """"
    id = request.matchdict['id']
    dbsession = DBSession()
    category = dbsession.query(Category).filter_by(id=id).one()
    if category is None:
        request.session.flash("error;Category not found!")
        return HTTPFound(location=request.route_url("category_list"))        
    

    form = Form(request, schema=CategoryForm, obj=category)    
    if "form_submitted" in request.POST and form.validate():
        form.bind(category)
        dbsession.add(category)
        request.session.flash("warning;The Category is saved!")
        return HTTPFound(location = request.route_url("category_list"))

    action_url = request.route_url("category_edit", id=id)
    return dict(form=FormRenderer(form), 
                action_url=action_url)
"""

"""
Requires authorisation
"""
@view_config(route_name="delete_idea")
def delete(request):
    """delete idea"""
    id = request.matchdict['id']
    dbsession = DBSession()
    idea = dbsession.query(Idea).filter_by(id=id).first()
    if idea is None:
        request.session.flash("error;Idea not found!")
        return HTTPFound(location=request.route_url("ideas"))        
    
    try:
        transaction.begin()
        dbsession.delete(idea);
        transaction.commit()
        #request.session.flash("warning;The category is deleted!")
    except IntegrityError:
        pass
        # delete error
        #transaction.abort()
        #request.session.flash("error;The category could not be deleted!")
    
    return HTTPFound(location=request.route_url("category_list"))
