from flask import Blueprint, render_template
from jobplus.models import Job,Company


front = Blueprint('front', __name__)

@front.route('/')
def index():
    jobs = Job.query.order_by(Job.updated_at.desc()).limit(8)
    companys = Company.query.order_by(Company.updated_at.desc()).limit(8)
    return render_template('index.html',jobs=jobs,companys=companys)

