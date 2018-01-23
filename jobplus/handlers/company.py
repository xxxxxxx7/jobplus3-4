from flask import request,redirect, abort, url_for
from flask import Blueprint, render_template, current_app
from flask import flash
from flask_login import login_required, current_user
from jobplus.models import Company, Job, db, Delivery
from jobplus.forms import CompanyProfileForm


company = Blueprint('company', __name__, url_prefix='/company')


@company.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    form = CompanyProfileForm(obj=current_user.company)
    form.name.data = current_user.username
    form.email.data = current_user.email
    if form.validate_on_submit():
        form.updated_profile(current_user)
        flash("企业信息更新成功", "success")
        return redirect(url_for("front.index"))
    return render_template('company/profile.html', form=form)
