from flask import  Blueprint, render_template
from model.quanli1.khoa import get_all_khoa
from model.quanli1.doctor import get_all_doctor
from model.quanli1.loaibenh import get_all_sick

def hoso():
    sicks = get_all_sick()
    doctor = get_all_doctor()
    khoa = get_all_khoa()

    return render_template('pages/hoSo.html',sicks=sicks,doctor=doctor,khoa=khoa)
