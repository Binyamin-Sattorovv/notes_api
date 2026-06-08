from pydantic import BaseModel, Field


class NoteCreate(BaseModel):
    
    title: str = Field(..., description="Title")
    
    content: str = Field(..., description="Content")
    
    
    
class NoteResponse(NoteCreate):
    
    id: int = Field(..., description="Id")
    
    
    class Congig:
        
        from_attributes = True
        

    
    