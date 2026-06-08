from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABABE_URL = "postgresql://postgres:1234321@localhost:5432/notesdb"

engine = create_engine(DATABABE_URL)

SessionLocal = sessionmaker(
    
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

Base.metada.create_all()

def get_db():
    
    db = SessionLocal()
    
    try:
        
        yield db
        
    finally:
        
        db.close()
        
        