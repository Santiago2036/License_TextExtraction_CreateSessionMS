from typing import Optional
from pydantic import BaseModel


class Entity(BaseModel):
    id: Optional[int]
    name_entyti:str