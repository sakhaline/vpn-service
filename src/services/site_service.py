from flask import abort
from sqlalchemy.exc import IntegrityError


class SiteService:
    def __init__(self, site_repo):
        self.site_repo = site_repo

    def get_site_by_id(self, site_id):
        site = self.site_repo.get_site_by_id(site_id)
        if not site:
            abort(404, description="Not found")
        return site

    def get_all_sites(self):
        return self.site_repo.get_site_list()

    def get_user_site_list(self, user):
        return self.site_repo.get_user_site_list(user)

    def update_site(self, data, site_id):
        try:
            return self.site_repo.update_site(site_id,
                                              {"name": data["name"],
                                               "url": data["url"]})
        except IntegrityError:
            abort(400, 'Site already exists')

    def update_site_stat(self, site_name, received_data_mb):
        return self.site_repo.update_site_stat(site_name, received_data_mb)

    def create_site(self, data, user_id):
        try:
            return self.site_repo.create_site({"name": data["name"],
                                               "url": data["url"],
                                               "user_id": user_id})
        except IntegrityError:
            abort(400, 'Site already exists')

    def create_custom_url(self, data):
        return f"/{data["name"]}/{data["url"]}"

    def delete_site(self, site_id):
        return self.site_repo.delete_site(site_id)
