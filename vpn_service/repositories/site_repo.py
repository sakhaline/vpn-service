from ..models.sites import Site
from .base_repo import BaseRepository


class SiteRepository(BaseRepository):
    model = Site

    def get_site_by_id(self, site_id) -> Site:
        return self.get_by_id(site_id)

    def get_site_by_name(self, site_name: str) -> model:
        return self.db.session.execute(
            self.db.select.where(self.model.name == site_name)
        ).scalar()

    def get_site_list(self):
        return self.get_list()

    def create_site(self, data: dict):
        self.create(data)

    def update_site(self, site_id, data):
        return self.update(site_id, data)

    def delete_site(self, site_id):
        self.delete(site_id)
