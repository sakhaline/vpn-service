class SiteService:
    def __init__(self, site_repo):
        self.site_repo = site_repo

    def get_site_by_id(self, data):
        return self.site_repo.get_site_by_id(data)

    def get_site_by_name(self, site_id):
        return self.site_repo.get_site_by_name(site_id)

    def get_site_list(self):
        return self.site_repo.get_site_list()

    def update_site(self, site_id, data):
        return self.site_repo.update_site(site_id, data)

    def create_site(self, site_id, data):
        return self.site_repo.create_site(site_id, data)

    def delete_site(self, site_id):
        return self.site_repo.delete_site(site_id)
