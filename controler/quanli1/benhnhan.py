from flask import  Blueprint, render_template, request
from database import SessionLocal
from models import HealthData
from model.quanli1.add import add_user

def benhnhan():
    return render_template('pages/benhnhan.html')

def add_benhnhan():
    name = request.form.get('name')
    phong= request.form.get('phong')
    addd = add_user(name)
    print(f"Tên Bệnh Nhân: {name}, Phòng: {phong}")
    return render_template('pages/index.html')

