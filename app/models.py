from pydantic import BaseModel
from typing import Optional

class AGetMinParams(BaseModel):
    P1: Optional[int] = None
    P2: Optional[int] = None

class AGetMaxParams(BaseModel):
    P1: int
    P2: int
    P3: int
    P4: int

class SaraneHazineRefahiParams(BaseModel):
    Y: float

class SaraneDarmanParams(BaseModel):
    Y: float

class HazineAeleMandiParams(BaseModel):
    YHamsar: float

class HazineOvladParams(BaseModel):
    Y1: float
    Y2: float
    TedadFarzamd: float

class SaraneTaminAtieParams(BaseModel):
    Y: float

class EidiParams(BaseModel):
    Y: float
