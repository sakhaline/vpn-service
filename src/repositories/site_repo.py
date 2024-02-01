from ..models.sites import Site
from .base_repo import BaseRepository


class SiteRepository(BaseRepository):
    model = Site

    def create_site(self, data: dict):
        self.create(data)

    def get_site_list(self):
        return self.get_list()

    def get_site_by_id(self, site_id):
        return self.get_by_id(site_id)

    def get_site_by_name(self, site_name):
        return self.db.session.execute(
            self.db.select(self.model).where(self.model.name == site_name)
        ).scalar()

    def update_site(self, site_id, data):
        site = self.get_by_id(site_id)
        site.name = data["name"]
        site.url = data["url"]
        self.db.session.commit()
        return site

    def delete_site(self, site_id):
        self.delete(site_id)

    def get_user_site_list(self, user):
        return self.db.session.execute(
            self.db.select(self.model).where(self.model.user_id == user.id)
        ).scalars()

    def update_site_stat(self, site_name, received_data_mb):
        site = self.get_site_by_name(site_name)
        site.data_received += received_data_mb
        site.page_visits += 1
        self.db.session.commit()
