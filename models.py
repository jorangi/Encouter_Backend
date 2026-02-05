from sqlalchemy import Column, String, JSON, TIMESTAMP, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Unit(Base):
    __tablename__ = 'units'
    
    id = Column(String(50), primary_key=True)
    base_stat = Column(JSON, nullable=False)
    growth_stat = Column(JSON, nullable=False)
    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )