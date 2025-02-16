from database import SessionLocal
from models import Doctor
from sqlalchemy.orm import selectinload

def add_doctor(name: str, phone: str, department_id: int, position: str):
    with SessionLocal() as db:
        new_doctor = Doctor(
            name=name,
            phone=phone,
            department_id=department_id,
            position=position
        )
        db.add(new_doctor)
        db.commit()
        db.refresh(new_doctor)  # Cập nhật dữ liệu sau khi thêm vào DB
        return new_doctor

def get_all_doctor():
    with SessionLocal() as db:
        doctors = (
            db.query(Doctor)
            .options(
                selectinload(Doctor.users),
                selectinload(Doctor.department),
            )
            .all()
        )
        print(doctors)
    return doctors

