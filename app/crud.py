from sqlalchemy.orm import Session

from models import Note


def create_note(db: Session, title: str, content: str):
    
    note = Note(title=title, content=content)
    
    db.add(note)
    
    db.commit()
    
    db.refresh(note)
    
    return note


def read_note(db: Session):
    
    return db.query(Note).all()


def get_note(db: Session, skip=0, limit=0):
    
    return(
        db.query(Note).offset(skip).limit(limit).all()
    )


def search_note(db: Session, search):
    
    return (db.query(Note).filter(Note.title.ilike(f"%{search}%")).all())
    
    

def update_note(db: Session, note_id: int, title: str, content: str):
    
    note = db.query(Note).filter(Note.id == note_id).first()
    
    if not note:
        
        return None
    
    note.title = title
    
    note.content = content
    
    db.refresh(note)
    
    db.commit()
    
    return note


def delete_note(db: Session, note_id: int):
    
    note = db.query(Note).filter(Note.id == note_id).first()
    
    if not note:
        
        return None
    
    db.delete(note)
    
    db.commit()
    
    return True

