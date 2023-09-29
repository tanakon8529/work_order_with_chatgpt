from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)

class WorkOrderType(Base):
    __tablename__ = 'work_order_types'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    # Add more fields as needed

class WorkOrder(Base):
    __tablename__ = 'work_orders'

    id = Column(Integer, primary_key=True)
    work_order_number = Column(String, unique=True, nullable=False)
    created_by_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    assigned_to_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    room = Column(String)
    started_at = Column(DateTime)
    finished_at = Column(DateTime)
    type_id = Column(Integer, ForeignKey('work_order_types.id'), nullable=False)
    status = Column(String)
    # Add more fields as needed

    created_by = relationship('User', foreign_keys=[created_by_id])
    assigned_to = relationship('User', foreign_keys=[assigned_to_id])
    work_order_type = relationship('WorkOrderType')
