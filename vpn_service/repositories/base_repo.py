from typing import Any, List


class BaseRepository:
    model: Any = None

    def __init__(self, db) -> None:
        self.db = db

    def get_by_id(self, id: int) -> Any:
        return self.db.session.execute(
            self.db.select.where(self.model.id == id)
        ).scalar()

    def get_list(self) -> List[Any]:
        return self.db.session.execute(self.db.select(self.model)).scalars()

    def create(self, data: dict) -> None:
        obj = self.model(**data)
        self.db.session.add(obj)
        self.db.session.commit()

    def update(self, data: dict, id: int) -> Any | None:
        obj = self.get_by_id(id)
        if obj:
            for key, value in data.items():
                setattr(obj, key, value)
            self.db.session.commit()
            return obj
        else:
            return None

    def delete(self, id: int):
        obj = self.get_by_id(id)
        if obj:
            self.db.session.delete(obj)
            self.db.session.commit()
            return True
        else:
            return False
