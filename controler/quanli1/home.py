from flask import  Blueprint, render_template
from model.quanli1.home import User

def home():
    users = User.get_all_users()
    print('du lieu',users)
    return render_template('pages/index.html', users=users)
