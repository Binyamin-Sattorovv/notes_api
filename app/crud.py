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



def search_note(db: Session, skip=0, limit=20, search=None):
    query = db.query(Note)

    if search:
        query = query.filter(Note.title.ilike(f"%{search}%"))

    return query.offset(skip).limit(limit).all()
    

def update_note(db: Session, note_id: int, title: str, content: str):
    
    note = db.query(Note).filter(Note.id == note_id).first()
    
    if not note:
        
        return None
    
    note.title = title
    
    note.content = content
    
    db.commit()
    
    db.refresh(note)
    
    
    return note


def delete_note(db: Session, note_id: int):
    
    note = db.query(Note).filter(Note.id == note_id).first()
    
    if not note:
        
        return None
    
    db.delete(note)
    
    db.commit()
    
    return {"deleted": True}

