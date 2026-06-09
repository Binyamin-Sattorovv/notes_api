from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from database import Base, get_db, engine
from models import Note
import models
from schemas import NoteCreate, NoteResponse, NoteUpdate

from crud import create_note, read_note, update_note, delete_note, search_note


from fastapi import Query


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)


@app.post("/notes")
def create_notes(note: NoteCreate, db: Session=Depends(get_db)):
    
    return create_note(db, note.title, note.content)
    



@app.get("/notes")
def get_notes(skip: int = Query(0, ge=0), limit: int = Query(20, ge=1, le=100),search: str | None = None, db: Session = Depends(get_db)):
    
    return search_note(db, skip=skip, limit=limit, search=search)



@app.put("/notes/{note_id}")
def update_tasks(note_id: int, note: NoteUpdate, db: Session=Depends(get_db)):
    
    note = update_note(db, note_id, note.title, note.content)
    
    if not note:
        
        raise HTTPException(status_code = 404, detail="Note not found")
    
    return note



@app.delete("/notes/{note_id}")
def delete_notes(note_id: int, db: Session=Depends(get_db)):
    
    note = delete_note(db, note_id)
    
    if not note:
        
        raise HTTPException(status_code = 404, detail="Note not found")
    
    return {"Message": "Note deleted!"}

    
    




