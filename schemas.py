from pydantic import BaseModel

class POISchema(BaseModel):
    nome:str
    x:int
    y:int

    class Config:
        from_attributes = True