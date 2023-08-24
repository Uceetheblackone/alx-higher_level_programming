#!/usr/bin/python3
"""
Contains the class definition of a State with a relationship to City.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_base import Base


class State(Base):
    """
    State class with a relationship to City.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        cascade="all, delete-orphan",
        backref="state"
    )
