from flask import  Blueprint, render_template, request
from database import SessionLocal
from models import HealthData
from model.quanli1.add import add_user
from model.quanli1.doctor import get_all_doctor
from model.quanli1.khoa import get_all_khoa
from model.quanli1.doctor import get_all_doctor
from model.quanli1.loaibenh import get_all_sick
from model.quanli1.add import benhnhan_id
def benhnhan_ids(id):
    sicks = get_all_sick()
    doctor = get_all_doctor()
    khoa = get_all_khoa()
    data = benhnhan_id(id)
    return render_template('pages/benhnhan.html',user = data, sicks=sicks,doctor=doctor,khoa=khoa)

def benhnhan():
    sicks = get_all_sick()
    doctor = get_all_doctor()
    khoa = get_all_khoa()
    return render_template('pages/benhnhan.html', sicks=sicks,doctor=doctor,khoa=khoa)

def add_benhnhan():
    name = request.form.get('name')
    phone= request.form.get('phone')
    address = request.form.get('address')
    relative= request.form.get('relative')
    job = request.form.get('job')
    sex = request.form.get('sex')
    active = 0
    note = "benh"
    department = int(request.form.get('department'))
    room= int(request.form.get('room'))
    sick = int(request.form.get('sick'))
    doctor= int(request.form.get('doctor'))
    addd = add_user(name)
    print(f"Tên Bệnh Nhân: {name}, Phòng: {phong}")
    return render_template('pages/index.html')

