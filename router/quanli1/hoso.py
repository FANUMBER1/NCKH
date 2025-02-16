from flask import Blueprint, render_template
from controler.quanli1.hoso import hoso
hosos = Blueprint('routers',__name__)
hosos.route('/hoso')(hoso)