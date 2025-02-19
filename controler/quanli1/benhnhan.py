from flask import  Blueprint, render_template, request
from database import SessionLocal
from models import HealthData
from model.quanli1.add import add_user
from model.quanli1.doctor import get_all_doctor
from model.quanli1.khoa import get_all_khoa
from model.quanli1.doctor import get_all_doctor
from model.quanli1.loaibenh import get_all_sick


def benhnhan():
    sicks = get_all_sick()
    doctor = get_all_doctor()
    khoa = get_all_khoa()
    return render_template('pages/benhnhan.html',users=users, sicks=sicks,doctor=doctor,khoa=khoa)

def add_benhnhan():
    name = request.form.get('name')
    phong= request.form.get('phong')
    addd = add_user(name)
    print(f"Tên Bệnh Nhân: {name}, Phòng: {phong}")
    return render_template('pages/index.html')

