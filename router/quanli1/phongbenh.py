from flask import Blueprint, render_template
from controler.quanli1.phongbenh import phongbenh
phongbenhs = Blueprint('router1',__name__)
phongbenhs.route('/phongbenh')(phongbenh)