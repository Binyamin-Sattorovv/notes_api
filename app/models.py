from sqlalchemy import Column, String, Integer, Boolean
from database import Base


class Note(Base):
    
    __tablename__ = "notes"
    
    id = Column(Integer, primary_key=True, index=True)
    
    title = Column(String, nullable=False, index=True)
    
    content = Column(String(500), nullable=False)
    
    