from flask import  Blueprint, render_template
from model.quanli1.home import User
from model.quanli1.khoa import get_all_khoa
from model.quanli1.doctor import get_all_doctor
from model.quanli1.loaibenh import get_all_sick
def home():
    users = User.get_all_users()
    sicks = get_all_sick()
    doctor = get_all_doctor()
    khoa = get_all_khoa()
    print('du lieu',users)
    return render_template('pages/index.html', users=users, sicks=sicks,doctor=doctor,khoa=khoa)
