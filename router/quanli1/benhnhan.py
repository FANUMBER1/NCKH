from flask import Blueprint, render_template
from controler.quanli1.benhnhan import benhnhan,add_benhnhan
benhnhans = Blueprint('router2',__name__)
benhnhans.route('/benhnhan')(benhnhan)

benhnhans.route('/benhnhan', methods=['POST'])(add_benhnhan)
