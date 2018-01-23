from flask import Blueprint, render_template
from jobplus.models import Job,Company


front = Blueprint('front', __name__)

@front.route('/')
def index():
    jobs = Job.query.order_by(Job.updated_at.desc()).limit(8)
    companys = Company.query.order_by(Company.updated_at.desc()).limit(8)
    return render_template('index.html',jobs=jobs,companys=companys)

from flask import request, current_app

#职位分页列表
@front.route('/job')
def joblist():
    # 获取参数中传过来的页数
    page = request.args.get('page', default=1, type=int)
    # 生成分页对象
    pagination = Job.query.paginate(
        page=page,
        per_page=current_app.config['INDEX_PER_PAGE'],
        error_out=False
    )
    return render_template('joblist.html', pagination=pagination)

#企业分页列表
@front.route('/company')
def joblist():
    # 获取参数中传过来的页数
    page = request.args.get('page', default=1, type=int)
    # 生成分页对象
    pagination = Company.query.paginate(
        page=page,
        per_page=current_app.config['INDEX_PER_PAGE'],
        error_out=False
    )
    return render_template('companylist.html', pagination=pagination)


