from typing import Optional
from pydantic import BaseModel


class Congressman(BaseModel):
    id: Optional[int]
    name:str
    email:str
    password:str