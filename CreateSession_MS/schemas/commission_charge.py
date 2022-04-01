from typing import Optional
from pydantic import BaseModel


class Commission_charge(BaseModel):
    id : Optional[int]
    name : str