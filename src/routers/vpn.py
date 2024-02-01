from flask import Blueprint, render_template, render_template_string

from ..extensions import db
from ..repositories.site_repo import SiteRepository
from ..services.site_service import SiteService
from ..services.vpn_service import VPNService


vpn = Blueprint("vpn", __name__, url_prefix="/vpn")


@vpn.route("/<site_name>/<path:original_url>")
def proxy_site(site_name, original_url) -> str:
    vpn_service = VPNService(site_name, original_url)
    page = vpn_service.process_page()
    received_data_mb = vpn_service.calculate_site_stat()
    SiteService(SiteRepository(db)).update_site_stat(site_name,
                                                     received_data_mb)
    return render_template_string(str(page))


@vpn.route("/stat")
def get_stat():
    sites = SiteService(SiteRepository(db)).get_all_sites()
    return render_template("vpn/stat.html", sites=sites)
