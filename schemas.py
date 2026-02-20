from pydantic import BaseModel

class POISchema(BaseModel):
    nome:str
    x:int
    y:int

    class Config:
        from_attributes = True

class CoordSchema(BaseModel):
    x:int
    y:int
    d_max:float

    class Config:
        from_attributes = True