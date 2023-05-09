from copy import deepcopy
from os import path

from fastapi.testclient import TestClient

from app.main import app
from app.config import settings


client = TestClient(app)


def test_healthcheck():
    response = client.get(path.join(settings.API_BASE_STR, "healthcheck"))
    assert response.status_code == 200
    assert response.json() == {
        "status": "Healthy",
    }


def test_units_v1():
    """Hits a few endpoints:
    1. Create a new unit
    2. Get units
    3. Update unit
    4. Delete unit
    """
    new_unit = {
        "name": "foo",
        "abbreviation": "f",
        "base": 10,
        "exponent": 0,
    }

    # Create a new unit
    response = client.post(
        path.join(settings.API_V1_STR, "unit"),
        json=new_unit,
    )
    assert response.status_code == 201
    assert response.json() == new_unit

    # Get units
    response = client.get(path.join(settings.API_V1_STR, "units"))
    assert response.status_code == 200
    assert response.json() == [new_unit]

    # Update a unit
    updates = deepcopy(new_unit)
    updates["base"] = 2

    response = client.put(
        path.join(settings.API_V1_STR, "unit", new_unit["name"]),
        json=updates,
    )
    assert response.status_code == 200
    assert response.json() == updates

    # Get units to confirm the update
    response = client.get(path.join(settings.API_V1_STR, "units"))
    assert response.status_code == 200
    assert response.json() == [updates]

    # Delete a unit
    response = client.delete(
        path.join(settings.API_V1_STR, "unit", new_unit["name"])
    )
    assert response.status_code == 200

    # Get units to confirm the deletion
    response = client.get(path.join(settings.API_V1_STR, "units"))
    assert response.status_code == 200
    assert response.json() == []
