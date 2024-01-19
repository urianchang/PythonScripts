from pydantic import BaseModel


class Unit(BaseModel):
    name: str
    abbreviation: str
    base: int
    exponent: int
