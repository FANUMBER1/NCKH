from flask import  Blueprint, render_template, request , redirect, url_for
from model.quanli1.khoa import get_all_khoa
from model.quanli1.doctor import get_all_doctor
from model.quanli1.loaibenh import get_all_sick
from model.quanli1.phongbenh import get_all_room, add_rooms, delete_rooms
def phongbenh():
    sicks = get_all_sick()
    doctor = get_all_doctor()
    khoa = get_all_khoa()
    phong = get_all_room()
    return render_template('pages/phongbenh.html',sicks=sicks,doctor=doctor,khoa=khoa,room = phong)
def phongbenh1():
    sicks = get_all_sick()
    doctor = get_all_doctor()
    khoa = get_all_khoa()
    phong = get_all_room()
    return render_template('pages/maneger.html',sicks=sicks,doctor=doctor,khoa=khoa,room = phong)

def delete_room(id):
    delete_rooms(id)
    return redirect(url_for('routers1.phongbenh1'))
def add_room():
    name = request.form.get('name')
    department = int(request.form.get('department'))
    note = request.form.get('note')
    addd = add_rooms(name,department,note)
    print(f"Tên Bệnh Nhân: {name}, ")
    return redirect(url_for('routers1.phongbenh1'))
