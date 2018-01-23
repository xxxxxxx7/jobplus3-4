from flask import Blueprint, request, current_app, render_template
from jobplus.models import Job

Job = Blueprint('job', __name__, url_prefix='/jobs')


#职位分页列表
@job.route('/')
def joblist():
    # 获取参数中传过来的页数
    page = request.args.get('page', default=1, type=int)
    # 生成分页对象
    pagination = Job.query.paginate(
        page=page,
        per_page=current_app.config['INDEX_PER_PAGE'],
        error_out=False
    )
    return render_template('job/joblist.html', pagination=pagination)


@job.route('/<int:job_id>')
def detail(job_id):
    job = Job.query.get_or_404(job_id)
    return render_template('job/detail.html', job=job)