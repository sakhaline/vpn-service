from flask import (Blueprint, request,  render_template,
                   redirect, url_for, abort)

from flask_login import login_required, current_user

from ..services.site_service import SiteService
from ..repositories.site_repo import SiteRepository
from ..extensions import db
from ..forms.sites import CreateSiteForm, UpdateSiteForm
from ..validators import invalid_url_handler


profile = Blueprint("profile", __name__, url_prefix='/profile')


@profile.route("/profile")
@login_required
def get_profile() -> str:
    sites = SiteService(SiteRepository(db)).get_user_site_list(current_user)
    context = {"username": current_user.username,
               "email": current_user.email,
               "sites": sites}
    return render_template("profile/profile.html", **context)


@profile.route("/site_create", methods=["GET", "POST"])
@login_required
def create_site():
    form = CreateSiteForm()
    if request.method == "POST":
        if form.validate_on_submit():
            SiteService(SiteRepository(db)).create_site(form.data,
                                                        current_user.id)
            return redirect(url_for("profile.get_profile"))
        invalid_url_handler()
    return render_template("sites/site_create.html", form=form)


@profile.route("/site_update/<int:site_id>", methods=["GET", "POST"])
def update_site(site_id):
    service = SiteService(SiteRepository(db))
    form = UpdateSiteForm()
    if request.method == "POST":

        if form.validate_on_submit():
            service.update_site(form.data, site_id=site_id)
            return redirect(url_for("profile.get_profile"))
        invalid_url_handler()

    site = service.get_site_by_id(site_id)
    context = {"form": form, "site": site, "site_id": site_id}
    return render_template("sites/site_update.html", **context)


@profile.route("/site_delete/<int:site_id>", methods=["GET", "POST"])
def delete_site(site_id):
    if request.method == "POST":
        SiteService(SiteRepository(db)).delete_site(site_id)
        return redirect(url_for('profile.get_profile'))
    return render_template('sites/site_confirm_delete.html', site_id=site_id)
