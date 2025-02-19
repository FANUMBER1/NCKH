from flask import Blueprint, render_template
from controler.quanli1.benhnhan import benhnhan,add_benhnhan,benhnhan_ids
benhnhans = Blueprint('router2',__name__)
benhnhans.route('/benhnhan')(benhnhan)
benhnhans.route('/benhnhan/<int:id>')(benhnhan_ids)
benhnhans.route('/benhnhan', methods=['POST'])(add_benhnhan)
