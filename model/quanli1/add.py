from database import SessionLocal
from models import HealthData
from models import User
from sqlalchemy.orm import selectinload

def add_user(name_user: str):
    """Thêm user mới vào database."""
    with SessionLocal() as db:
        new_record = User(name=name_user)
        db.add(new_record)
        db.commit()
        db.refresh(new_record)
        print(f"User ID: {new_record.id}")


def add_health_data(heart_rate: float, spo2: float, user_id: int):
    """Thêm dữ liệu sức khỏe vào database."""
    with SessionLocal() as db:
        new_record = HealthData(heartRate=heart_rate, spo2=spo2, user_id=user_id)
        db.add(new_record)
        db.commit()
        db.refresh(new_record)
        print(f"Inserted Health Data ID: {new_record.id}")

def benhnhan_id(id:int):
    with SessionLocal() as db:
        new_record = (db.query(User).filter(User.id == id)
        .options(
                selectinload(User.department),
                selectinload(User.doctor),
                selectinload(User.room),
                selectinload(User.sick),
            )
        .all())
        return new_record