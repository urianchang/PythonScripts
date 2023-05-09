from typing import (
    Any,
    Dict,
    List,
    Optional,
)
from app.models.unit import Unit


class DatabaseSession:
    # Ideally we'd have a database connection
    # For now, we'll keep data in memory
    units: List[Unit] = []

    def __init__(self, seed: bool = False):
        if seed:
            self.units = self._make_units()

    @staticmethod
    def _make_units() -> List[Unit]:
        return [
            Unit(
                name="kilo",
                abbreviation="k",
                base=10,
                exponent=3,
            ),
            Unit(
                name="kibi",
                abbreviation="Ki",
                base=2,
                exponent=10,
            ),
        ]

    def get_units(self) -> List[Dict[str, Any]]:
        return [u.dict() for u in self.units]

    def add_unit(self, new_unit: Unit) -> Optional[Unit]:
        for unit in self.units:
            if unit.name == new_unit.name:
                return None
        self.units.append(new_unit)
        return new_unit

    def update_unit(self, updates: Unit) -> Optional[Unit]:
        for idx, unit in enumerate(self.units):
            if unit.name == updates.name:
                self.units[idx] = updates
                return updates
        return None

    def delete_unit(self, name: str) -> str:
        for idx, unit in enumerate(self.units):
            if unit.name == name:
                del self.units[idx]
                return "success"
        return f'Unit "{name}" not found'
