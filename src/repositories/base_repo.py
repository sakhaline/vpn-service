from typing import Any, List


class BaseRepository:
    model: Any = None

    def __init__(self, db) -> None:
        self.db = db

    def get_by_id(self, obj_id: int) -> Any:
        return self.db.session.execute(
            self.db.select(self.model).where(self.model.id == obj_id)
        ).scalar()

    def get_list(self) -> List[Any]:
        return self.db.session.execute(self.db.select(self.model)).scalars()

    def create(self, data: dict) -> None:
        obj = self.model(**data)
        self.db.session.add(obj)
        self.db.session.commit()

    def delete(self, obj_id: int) -> None:
        self.db.session.delete(self.get_by_id(obj_id))
        self.db.session.commit()
