from typing import Optional
from pydantic import BaseModel


class Charge_congressman(BaseModel):
    id : Optional[int]
    name : str