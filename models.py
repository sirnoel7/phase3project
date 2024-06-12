from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    due_date = Column(Date)  # this ensures that the due_date is of type date
    status = Column(Boolean, default=False)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category')

def init_db():
    engine = create_engine('sqlite:///db/todo_list.db')
    Base.metadata.create_all(engine)
    return engine
