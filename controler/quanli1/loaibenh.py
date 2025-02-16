from flask import  Blueprint, render_template, request , redirect, url_for
from flask import  Blueprint, render_template, request , redirect, url_for
from database import SessionLocal
from model.quanli1.loaibenh import add_sick,get_all_sick
from model.quanli1.khoa import add_1_khoa,get_all_khoa
from model.quanli1.doctor import add_doctor, get_all_doctor

def loaibenh():
    data1 = get_all_sick()
    data2 = get_all_khoa()
    data3 = get_all_doctor()
    return render_template('pages/maneger.html',sick=data1, khoa=data2, doctor = data3)

def add_loaibenh():
    name = request.form.get('name')
    addd = add_sick(name)
    print(f"Tên Bệnh Nhân: {name}, ")
    return redirect(url_for('routers1.loaibenh'))

