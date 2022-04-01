from typing import Optional
from pydantic import BaseModel


class Commission(BaseModel):
    id : Optional[int]
    name : str
    id_entity : int