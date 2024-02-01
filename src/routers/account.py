from flask import (Blueprint, Response, redirect,
                   render_template, request, url_for)
from flask_login import current_user, login_required

from ..extensions import db
from ..forms.users import LoginUserForm, RegisterUserForm, UpdateUserForm
from ..repositories.user_repo import UserRepository
from ..services.user_service import UserService


account = Blueprint("account", __name__, url_prefix="/account")


@account.route("/register", methods=["GET", "POST"])
def register() -> Response | str:
    form = RegisterUserForm()
    if request.method == "POST":
        if form.validate_on_submit():
            UserService(UserRepository(db)).create_user(form.data)
        return redirect(url_for("account.login"))
    return render_template("account/register.html", form=form)


@account.route("/login", methods=["GET", "POST"])
def login() -> Response | str:
    form = LoginUserForm()
    if request.method == "POST":
        if form.validate_on_submit():
            UserService(UserRepository(db)).login(form.data)
        return redirect(url_for("profile.get_profile"))
    return render_template("account/login.html", form=form)


@account.route("/logout")
@login_required
def logout():
    UserService(UserRepository(db)).logout()
    return redirect(url_for("account.login"))


@account.route("/user_update", methods=["GET", "POST"])
@login_required
def update_user():
    form = UpdateUserForm()
    if request.method == "POST":
        print(form.data)
        if form.validate_on_submit():
            UserService(UserRepository(db)).update_user(current_user, form.data)
        return redirect(url_for("profile.get_profile"))
    return render_template("account/update.html", form=form)
