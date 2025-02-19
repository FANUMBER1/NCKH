from flask import  Blueprint, render_template, request , redirect, url_for
from database import SessionLocal
from model.quanli1.khoa import add_1_khoa,get_all_khoa
from model.quanli1.loaibenh import add_sick,get_all_sick
from model.quanli1.doctor import add_doctor, get_all_doctor
from model.quanli1.phongbenh import get_all_room
def doctor():
    data1 = get_all_sick()
    data2 = get_all_khoa()
    data3 = get_all_doctor()
    data4= get_all_room
    return render_template('pages/maneger.html',sicks=data1, khoa=data2, doctor = data3, room= data4)

def add_bacsi():
    name = request.form.get('name')
    phone = request.form.get('phone')
    position = request.form.get('position')
    department = int(request.form.get('department'))
    addd = add_doctor(name,phone,department,position)
    return redirect(url_for('routers1.doctor'))

