from typing import List

from fastapi import APIRouter, HTTPException

from app.models.unit import Unit
from app.services.database import DatabaseSession


fake_db = DatabaseSession()


units_v1 = APIRouter()


@units_v1.get("/units", response_model=List[Unit])
async def get_units():
    return fake_db.get_units()


@units_v1.post("/unit", status_code=201)
async def add_unit(payload: Unit):
    result = fake_db.add_unit(payload)
    if result is None:
        raise HTTPException(
            status_code=404, detail=f'Unit "{payload.name}" already exists'
        )
    return result


@units_v1.put("/unit/{name}")
async def update_unit(name: str, payload: Unit):
    result = fake_db.update_unit(payload)
    if result is None:
        raise HTTPException(status_code=404, detail=f'Unit "{name}" not found')
    return result


@units_v1.delete("/unit/{name}")
async def delete_unit(name: str):
    result = fake_db.delete_unit(name)
    if result != "success":
        raise HTTPException(status_code=404, detail=result)
    return None
