from sqlalchemy import (
    Column,
    Integer,
    Text,
    String,
    ForeignKey,
    DateTime,
    
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

## Data Models defined below
"""
Idea
This class defines the data for an idea
"""
class Idea(Base):
    __tablename__ = 'ideas'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(Text)
    author = Column(String(255))
    category_id = Column(Integer, ForeignKey('categories.cat_id', name='fk_cat_id',
                                          onupdate='cascade', ondelete='RESTRICT'), nullable=False)
    category = relationship("Category", passive_deletes=True, passive_updates=True)
    created_at = Column(DateTime)

"""
Category
Provide seed data for categories
"""
class Category(Base):
    __tablename__ = 'categories'
    
    cat_id = Column(Integer, primary_key=True)
    cat_name = Column(String(50), nullable=False)
    
    def __init__(self, name):
        self.cat_name = name
    
class User(Base):
    
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    fname = Column(String(40), nullable=False)
    lname = Column(String(40), nullable=False)
    username = Column(String(40), nullable=False, unique=True)
    password = Column(String(42), nullable=False)
    email = Column(String(60), unique=True)

"""
Seed Data
Pre-populate database with this data

def populate():
    try:
        transaction.begin()
        db = DBSession()
        db.add_all(
            [
                Category('technology'),
                Category('agriculture')
            ]
        )
        transaction.commit()
    except IntegrityError:
        transaction.abort()
"""