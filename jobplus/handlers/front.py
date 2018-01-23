from flask import Blueprint, render_template, flash, redirect, url_for
from jobplus.models import Job,Company, User
from jobplus.forms import RegisterForm, CompanyRegisterForm, LoginForm
from flask_login import login_required, login_user


front = Blueprint('front', __name__)

@front.route('/')
def index():
    jobs = Job.query.order_by(Job.updated_at.desc()).limit(8)
    companys = Company.query.order_by(Company.updated_at.desc()).limit(8)
    return render_template('index.html',jobs=jobs,companys=companys)

from flask import request, current_app



#企业分页列表
@front.route('/company')
def companylist():
    # 获取参数中传过来的页数
    page = request.args.get('page', default=1, type=int)
    # 生成分页对象
    pagination = Company.query.paginate(
        page=page,
        per_page=current_app.config['INDEX_PER_PAGE'],
        error_out=False
    )
    return render_template('companylist.html', pagination=pagination)


@front.route("/userregister", methods=["GET", "POST"])
def userregister():
    """
    用户注册
    """
    form = RegisterForm()
    post_url = url_for("front.userregister")
    if form.validate_on_submit():
        form.create_user()
        flash('注册成功，请登录！', 'success')
        return redirect(url_for('.login'))
    return render_template('register.html', form=form, post_url=post_url, topic="用户注册")


@front.route("/companyregister", methods=["GET", "POST"])
def companyregister():
    """
    企业注册
    """
    form = CompanyRegisterForm()
    post_url = url_for("front.companyregister")
    if form.validate_on_submit():
        form.create_user()
        flash('注册成功，请登录！', 'success')
        return redirect(url_for('.login'))
    return render_template('register.html', form=form, post_url=post_url, topic="企业注册")


@front.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.is_disable:
            flash('用户已经被禁用')
            return redirect(url_for('front.login'))
        else:
            login_user(user, form.remember_me.data)
            next = 'user.profile'
            if user.is_admin:
                next = 'admin.index'
            elif user.is_company:
                next = 'company.profile'
            return redirect(url_for(next))
    return render_template('login.html', form=form)

