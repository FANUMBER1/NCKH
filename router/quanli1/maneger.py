from flask import Blueprint, render_template
from controler.quanli1.maneger import maneger
from controler.quanli1.loaibenh import loaibenh,add_loaibenh
from controler.quanli1.khoa import khoa,add_khoa
from controler.quanli1.doctor import doctor,add_bacsi
from controler.quanli1.phongbenh import phongbenh1, add_room,delete_room
manegers = Blueprint('routers1',__name__)
manegers.route('/maneger')(maneger)

manegers.route('/sick')(loaibenh)
manegers.route('/sick',methods=['POST'])(add_loaibenh)

manegers.route('/department')(khoa)
manegers.route('/department',methods=['POST'])(add_khoa)

manegers.route('/doctor')(doctor)
manegers.route('/doctor',methods=['POST'])(add_bacsi)

manegers.route('/room')(phongbenh1)
manegers.route('/room/delete/<int:id>')(delete_room)
manegers.route('/room',methods=['POST'])(add_room)

