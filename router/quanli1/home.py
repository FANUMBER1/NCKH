from flask import Blueprint, render_template
from controler.quanli1.home import home
homes = Blueprint('router',__name__)
homes.route('/')(home)